# Selenium Python Setup Guide

This guide will help you set up a virtual environment and install Selenium for Python automation testing.

## Prerequisites

- **Ubuntu** (or any Linux distribution)
- **Python 3** (Ensure you have Python installed: `python3 --version`)
- **pip** (Python package manager: `pip --version`)
- **Google Chrome** (or any other browser you wish to automate)
- **ChromeDriver** (for Chrome automation)

## Step 1: Download and Install Google Chrome Stable

```bash
# Update package lists
sudo apt update

# Install dependencies
sudo apt install -y wget curl unzip

# Download Chrome from the official source
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install Chrome
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y

# Verify installation
google-chrome --version
```

## Step 2: Create a Virtual Environment

```bash
# Install virtual environment package if not already installed
sudo apt install -y python3-venv

# Create a virtual environment
python3 -m venv selenium-env

# Activate the virtual environment
source selenium-env/bin/activate
```

## Step 3: Install Selenium

```bash
pip install --upgrade pip
pip install selenium
```

## Step 4: Install WebDriver (ChromeDriver for Chrome)

```bash
# Download the latest ChromeDriver (ensure it matches your Chrome version)
wget https://storage.googleapis.com/chrome-for-testing-public/133.0.6943.141/linux64/chromedriver-linux64.zip

# Extract and move to /usr/local/bin
unzip chromedriver-linux64.zip
sudo mv chromedriver-linux64/chromedriver /usr/local/bin/
sudo chmod +x /usr/local/bin/chromedriver

# Verify installation
chromedriver --version
```

## Step 5: Run a Selenium Script

Create a Python script (e.g., `test.py`) with the following content:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Setup Chrome WebDriver
service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print("Page Title:", driver.title)

driver.quit()
```

Run the script:

```bash
python test.py
```

## Step 6: Deactivate Virtual Environment (When Done)

```bash
deactivate
```

Now your Selenium Python environment is ready! 🚀

