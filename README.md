# Weather App - OpenWeatherMap

A weather application with both CLI and Web interface that fetches current weather data using the OpenWeatherMap API.

## Features

- 🌤️ Get current weather for any city
- 🌡️ Support for multiple temperature units (Celsius, Fahrenheit, Kelvin)
- 💻 Command-line interface (CLI)
- 🌐 Beautiful web interface
- 📊 Detailed weather information (temperature, humidity, pressure, wind speed, sunrise/sunset)

## Requirements

- Python 3.8+
- OpenWeatherMap API key (free at https://openweathermap.org/api)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/knight384/Weather-App-Project-Python.git
cd Weather-App-Project-Python
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Setup API key:
   - Copy `config.json.example` to `config.json`
   - Replace `YOUR_API_KEY_HERE` with your actual API key from https://openweathermap.org/api

## Usage

### Web Interface (Recommended)

1. Start the Flask server:
```bash
python app.py
```
or
```bash
python run_server.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Enter a city name and click Search!

### Command Line Interface

```bash
python main.py --city "London" --units metric
```

Options:
- `--city` or `-c`: City name (required)
- `--units`: Temperature units - `metric` (Celsius), `imperial` (Fahrenheit), or `standard` (Kelvin)
- `--key`: API key (optional, uses config.json by default)
- `--verbose` or `-v`: Enable verbose output

Examples:
```bash
python main.py --city "New York" --units imperial
python main.py -c "Tokyo" --units metric -v
```

## Project Structure

```
Weather-App-Project-Python/
├── app.py              # Flask web application
├── main.py             # CLI application
├── config.json         # API key configuration (not in git)
├── config.json.example # Example config file
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates for web app
│   └── index.html
├── index.html          # Standalone HTML file
└── README.md           # This file
```

## Notes

- The app uses the OpenWeatherMap Current Weather Data API
- Free API keys may have rate limits
- Keep your `config.json` file private - it contains your API key
