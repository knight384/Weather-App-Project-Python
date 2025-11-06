# Weather App - main.py
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests library is not installed.")
    print("Please install it using: pip install requests")
    sys.exit(1)

# Use absolute path for config file
CONFIG_FILE = Path(os.path.dirname(os.path.abspath(__file__))) / 'config.json'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def get_weather(city, api_key, units='metric', verbose=False):
    params = {
        'q': city,
        'appid': api_key,
        'units': units
    }
    try:
        if verbose:
            print(f"Attempting to fetch weather data for {city}...")
        resp = requests.get(BASE_URL, params=params, timeout=10)
        if verbose:
            print(f"Response status code: {resp.status_code}")
        if resp.status_code == 401:
            error_msg = resp.json().get('message', 'Unknown error')
            raise RuntimeError(
                f"API Key error: {error_msg}\n"
                "Please:\n"
                "1. Check if the API key is correct\n"
                "2. If the key is new, wait 2-4 hours for activation\n"
                "3. Visit https://home.openweathermap.org/api_keys to verify your key"
            )
        elif resp.status_code == 404:
            raise RuntimeError(f"City not found: {city}")
        resp.raise_for_status()
        return resp.json()
    except requests.RequestException as e:
        if "Connection refused" in str(e):
            raise RuntimeError("Network error: Please check your internet connection")
        if verbose:
            print(f"Full error response: {e.response.text if hasattr(e, 'response') else str(e)}")
        raise RuntimeError(f"Failed to fetch weather data: {str(e)}")

def pretty_print(data, units='metric'):
    name = data.get('name')
    main = data.get('main', {})
    weather = data.get('weather', [{}])[0]
    wind = data.get('wind', {})
    sys_info = data.get('sys', {})
    
    # Determine temperature unit
    # Use a stable degree sign; stdout is reconfigured to UTF-8 in main when possible
    temp_unit = '\N{DEGREE SIGN}C' if units == 'metric' else '\N{DEGREE SIGN}F' if units == 'imperial' else 'K'
    speed_unit = 'm/s' if units == 'metric' else 'mph' if units == 'imperial' else 'm/s'
    
    print(f"\nWeather for: {name}")
    print('Description:', weather.get('description', 'N/A').capitalize())
    print(f"Temperature: {main.get('temp', 'N/A')} {temp_unit}")
    print(f"Feels like: {main.get('feels_like', 'N/A')} {temp_unit}")
    print(f"Humidity: {main.get('humidity', 'N/A')}%")
    print(f"Pressure: {main.get('pressure', 'N/A')} hPa")
    print(f"Wind speed: {wind.get('speed', 'N/A')} {speed_unit}")
    
    if sys_info.get('sunrise') and sys_info.get('sunset'):
        try:
            sunrise = datetime.fromtimestamp(sys_info['sunrise'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            sunset = datetime.fromtimestamp(sys_info['sunset'], timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            print('Sunrise (UTC):', sunrise)
            print('Sunset (UTC):', sunset)
        except (ValueError, TypeError):
            print("Error: Invalid sunrise/sunset data")

def main():
    try:
        parser = argparse.ArgumentParser(description='Simple Weather CLI using OpenWeatherMap')
        parser.add_argument('--city', '-c', required=True, help='City name (e.g. London)')
        parser.add_argument('--units', choices=['metric','imperial','standard'], 
                          default='metric', help='Temperature units (default: metric)')
        parser.add_argument('--key', help='OpenWeatherMap API key (overrides config file)')
        parser.add_argument('--verbose', '-v', action='store_true', help='Enable verbose debug output')
        args = parser.parse_args()

        # Make Windows console print UTF-8 correctly when possible
        try:
            if hasattr(sys.stdout, 'reconfigure'):
                sys.stdout.reconfigure(encoding='utf-8')
        except Exception:
            pass

        cfg = load_config()
        api_key = args.key or cfg.get('OPENWEATHER_API_KEY')
        if not api_key or api_key == 'YOUR_API_KEY_HERE':
            raise ValueError('API key not provided. Put it in config.json or use --key argument.')

        data = get_weather(args.city, api_key, units=args.units, verbose=args.verbose)
        pretty_print(data, units=args.units)
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except RuntimeError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
