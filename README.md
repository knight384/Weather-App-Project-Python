Weather App — OpenWeatherMap

Project Title: Weather App — OpenWeatherMap
Submitted by: Anish Choudhary
Internship Role: Virtual Intern
Organization: Hack Culprit
Project Duration: 1st October 2025 – 31st October 2025
Project Repository: https://github.com/knight384/Weather-App-Project-Python.git

1. Executive Summary

This project implements a simple, user-friendly Weather Application with both a web interface and a command-line interface (CLI). It fetches live current weather data using the OpenWeatherMap API and displays temperature, humidity, pressure, wind speed, and sunrise/sunset details. The project demonstrates full-cycle software development: requirements analysis, implementation, testing, documentation, and deployment preparation.

(Repository contains the web and CLI implementations and instructions.) 
GitHub

2. Problem Statement

Many users want an easy way to get reliable, current weather information for any city without needing complex installations. This project provides a lightweight, cross-platform solution (web + CLI) that allows users to quickly fetch and view current weather conditions.

3. Project Objectives

Gain practical exposure to full-cycle software development.

Build a working weather app that consumes an external API.

Use version control and collaborative tools effectively.

Produce professional documentation and a clean project structure.

4. Development Approach

The project followed a four-stage approach:

Requirement Analysis & Planning — Defined scope, chosen OpenWeatherMap API, and decided on Flask for the web front-end + a Python CLI.

Development — Implemented app.py (Flask web app) and main.py (CLI), created templates and a simple front-end.

Testing & Debugging — Manual testing for various cities and unit checks for response parsing; handled API error cases.

Documentation & Packaging — Wrote README, included requirements.txt, and provided example configuration.

Repository files (app, CLI, template, example config) confirm this structure. 
GitHub

5. Tools & Technologies
Category	Tools / Technologies Used
Programming	Python, HTML
Frameworks	Flask
API	OpenWeatherMap (Current Weather Data)
Tools	Git, GitHub, VS Code
Files	requirements.txt, config.json.example, templates/index.html
6. Installation & Setup

Prerequisites: Python 3.8 or newer, pip.

Clone the repository

git clone <your-repo-clone-url>
cd Weather-App-Project-Python


Install dependencies

pip install -r requirements.txt


Configure API key

Copy the example config file and add your OpenWeatherMap API key:

cp config.json.example config.json


Edit config.json and replace the placeholder YOUR_API_KEY_HERE with your API key.

Keep config.json private (do not commit your real API key). The repository contains config.json.example to demonstrate the format. 
GitHub

7. Key Features

Web interface (Flask) to search weather by city.

CLI interface for quick terminal lookups.

Support for multiple units: Celsius (metric), Fahrenheit (imperial), Kelvin (standard).

Displays detailed weather: temperature, humidity, pressure, wind speed, sunrise/sunset.

Small, modular codebase suitable for extension. 
GitHub

8. Usage
Web Interface (recommended)

Start the Flask server:

python app.py


or

python run_server.py


Open your browser and navigate to http://localhost:5000, then enter a city name and click Search. 
GitHub

Command Line Interface

Run the CLI to fetch weather from terminal:

python main.py --city "London" --units metric


Options

--city or -c : City name (required)

--units : metric, imperial, or standard

--key : API key (optional; uses config.json by default)

--verbose or -v : Enable verbose output

Examples

python main.py --city "New York" --units imperial
python main.py -c "Tokyo" --units metric -v


(Commands and options are provided by the repository scripts.) 
GitHub

9. Project Structure
Weather-App-Project-Python/
├── app.py              # Flask web application
├── main.py             # CLI application
├── config.json         # API key configuration (should be created locally)
├── config.json.example # Example config file
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates for web app
│   └── index.html
├── index.html          # Standalone HTML file
├── run_server.py
└── README.md


This structure is taken directly from the repository. 
GitHub

10. Demonstration

Video is uploaded in the drive

11. Challenges Encountered

Working within free API rate limits and handling API failures gracefully.

Sanitizing user input for different city name formats.

Designing a simple, responsive front-end quickly using minimal CSS/HTML.

12. Scope for Future Enhancements

Add forecast (multi-day) support using the weather API's forecast endpoints.

Add caching to reduce API requests and handle rate limits.

Add unit tests and CI pipeline for automated checks.

Deploy the app to a cloud provider or platform-as-a-service.

Add localization for different languages and formats.

13. Conclusion

This project demonstrates practical application development skills by integrating an external API with both web and CLI clients. It reinforces good practices like separating configuration from code and documenting setup steps for reproducibility.

14. Acknowledgements

Thanks to the Hack Culprit team for the internship opportunity and guidance. Thanks to OpenWeatherMap for the accessible weather API used in this project.

15. License

This project is distributed under the MIT License.
