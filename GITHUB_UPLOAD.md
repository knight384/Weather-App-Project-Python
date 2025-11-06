# How to Upload to GitHub

Follow these steps to upload your weather app to GitHub:

## Step 1: Create a GitHub Account (if you don't have one)

1. Go to https://github.com
2. Sign up for a free account

## Step 2: Create a New Repository on GitHub

1. Log in to GitHub
2. Click the **"+"** icon in the top right corner
3. Select **"New repository"**
4. Fill in:
   - **Repository name**: `weather-app` (or any name you like)
   - **Description**: "Weather app using OpenWeatherMap API"
   - **Visibility**: Choose Public or Private
   - **DO NOT** check "Initialize with README" (we already have files)
5. Click **"Create repository"**

## Step 3: Initialize Git in Your Project

Open terminal in Cursor (Ctrl + `) and run:

```powershell
cd weather_app
git init
```

## Step 4: Add Files to Git

```powershell
git add .
```

This adds all files except those in `.gitignore` (like `config.json` with your API key).

## Step 5: Make Your First Commit

```powershell
git commit -m "Initial commit: Weather app with CLI and web interface"
```

## Step 6: Connect to GitHub

Replace `YOUR_USERNAME` with your GitHub username:

```powershell
git remote add origin https://github.com/YOUR_USERNAME/weather-app.git
```

Or if you named your repository differently, use that name instead of `weather-app`.

## Step 7: Push to GitHub

```powershell
git branch -M main
git push -u origin main
```

You'll be prompted for your GitHub username and password (or use a Personal Access Token).

## Step 8: Verify

Go to your GitHub repository page and refresh - you should see all your files!

## Important Notes

✅ **Your API key is protected**: The `.gitignore` file excludes `config.json`, so your API key won't be uploaded.

✅ **Users need to create their own config.json**: They can copy `config.json.example` and add their own API key.

## If You Get Authentication Errors

If `git push` asks for authentication:

1. Go to GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate a new token with `repo` permissions
3. Use the token as your password when pushing

## Updating Your Repository

After making changes:

```powershell
git add .
git commit -m "Description of your changes"
git push
```

## Troubleshooting

- **"Repository not found"**: Check that the repository name and username are correct
- **"Authentication failed"**: Use a Personal Access Token instead of password
- **"config.json is tracked"**: Run `git rm --cached config.json` then commit again

