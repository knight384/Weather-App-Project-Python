# How to Start the Weather App

## Quick Start (Easiest Method)

1. **Open Terminal in Cursor:**
   - Press `Ctrl + `` (backtick) or go to View → Terminal

2. **Navigate to the weather_app folder:**
   ```powershell
   cd weather_app
   ```

3. **Start the server:**
   ```powershell
   python run_server.py
   ```
   OR
   ```powershell
   python app.py
   ```

4. **You should see:**
   ```
   Starting Weather App Server...
   Server will be available at: http://localhost:5000
   * Running on http://127.0.0.1:5000
   ```

5. **Open your browser and go to:**
   ```
   http://localhost:5000
   ```

## Alternative: Double-click Method

1. Double-click `start.bat` file in the weather_app folder
2. A terminal window will open showing the server starting
3. Open your browser to `http://localhost:5000`

## Troubleshooting

- **"Connection Refused" error**: Make sure the Flask server is running (check terminal)
- **"Port already in use"**: Another program is using port 5000. Close it or change the port in app.py
- **"Module not found"**: Run `pip install -r requirements.txt` first

## Important Notes

- Keep the terminal window open while using the app
- The server must be running for the app to work
- Press Ctrl+C in the terminal to stop the server

