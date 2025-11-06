# Weather App - Flask Web Application
from flask import Flask, render_template, request, jsonify
import json
import os
from pathlib import Path
import requests
from datetime import datetime, timezone

app = Flask(__name__)

# Use absolute path for config file
CONFIG_FILE = Path(os.path.dirname(os.path.abspath(__file__))) / 'config.json'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_weather(city, api_key, units='metric'):
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }
    try:
        resp = requests.get(BASE_URL, params=params, timeout=10)
        if resp.status_code == 401:
            error_msg = resp.json().get('message', 'Unknown error')
            raise RuntimeError(
                f"API Key error: {error_msg}\n"
                "Please check your API key in config.json"
            )
        elif resp.status_code == 404:
            raise RuntimeError(f"City not found: {city}")
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        if "Connection refused" in str(e):
            raise RuntimeError("Network error: Please check your internet connection")
        raise RuntimeError(f"Failed to fetch weather data: {str(e)}")

@app.route('/')
def index():
    # Serve the HTML file from templates folder
    try:
        return render_template('index.html')
    except:
        # Fallback: read index.html directly if template not found
        html_path = Path(__file__).parent / 'index.html'
        if html_path.exists():
            with open(html_path, 'r', encoding='utf-8') as f:
                return f.read()
        return "Error: HTML file not found", 404

@app.route('/api/weather', methods=['GET'])
def weather_api():
    try:
        city = request.args.get('city', '')
        units = request.args.get('units', 'metric')
        
        if not city:
            return jsonify({'error': 'City parameter is required'}), 400
        
        cfg = load_config()
        api_key = cfg.get('OPENWEATHER_API_KEY')
        
        if not api_key or api_key == 'YOUR_API_KEY_HERE':
            return jsonify({'error': 'API key not configured. Please check config.json'}), 500
        
        data = get_weather(city, api_key, units=units)
        
        # Format the response
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        wind = data.get('wind', {})
        sys_info = data.get('sys', {})
        
        temp_unit = '°C' if units == 'metric' else '°F' if units == 'imperial' else 'K'
        speed_unit = 'm/s' if units == 'metric' else 'mph' if units == 'imperial' else 'm/s'
        
        result = {
            'city': data.get('name'),
            'description': weather.get('description', 'N/A').capitalize(),
            'temperature': f"{main.get('temp', 'N/A')} {temp_unit}",
            'feels_like': f"{main.get('feels_like', 'N/A')} {temp_unit}",
            'humidity': f"{main.get('humidity', 'N/A')}%",
            'pressure': f"{main.get('pressure', 'N/A')} hPa",
            'wind_speed': f"{wind.get('speed', 'N/A')} {speed_unit}",
        }
        
        if sys_info.get('sunrise') and sys_info.get('sunset'):
            try:
                sunrise = datetime.fromtimestamp(sys_info['sunrise'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                sunset = datetime.fromtimestamp(sys_info['sunset'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
                result['sunrise'] = sunrise
                result['sunset'] = sunset
            except (ValueError, TypeError):
                pass
        
        return jsonify(result)
        
    except RuntimeError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

