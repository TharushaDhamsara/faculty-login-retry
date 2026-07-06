# Step-by-Step Setup Guide

## For Windows Users

### Step 1: Install Python
1. Download Python from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT:** Check the box "Add Python to PATH"
4. Click "Install Now"
5. Wait for installation to complete

### Step 2: Download the Project
- Go to your repository on GitHub
- Click the green "Code" button
- Click "Download ZIP"
- Extract the ZIP file to a folder (e.g., Desktop)

### Step 3: Open Command Prompt in Project Folder
- Navigate to the extracted folder
- Right-click inside the folder
- Select "Open in Terminal" or "Open Command Prompt here"

### Step 4: Install Dependencies
Type this command and press Enter:
```bash
pip install -r requirements.txt
```

### Step 5: Run the Script
Type this command and press Enter:
```bash
python login_retry.py
```

Or use the batch file:
```bash
run.bat
```

---

## For Mac Users

### Step 1: Install Python
1. Python usually comes pre-installed on Mac
2. Open Terminal (Applications > Utilities > Terminal)
3. Check if Python is installed:
   ```bash
   python3 --version
   ```

### Step 2: Download the Project
- Go to your repository on GitHub
- Click the green "Code" button
- Click "Download ZIP"
- Extract the ZIP file

### Step 3: Navigate to Project Folder
Open Terminal and type:
```bash
cd Downloads/faculty-login-retry
```
(Adjust path if you extracted to a different location)

### Step 4: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 5: Run the Script
```bash
python3 login_retry.py
```

Or use the shell script:
```bash
bash run.sh
```

---

## For Linux Users

### Step 1: Install Python and pip
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

### Step 2: Download the Project
- Go to your repository on GitHub
- Click the green "Code" button
- Click "Download ZIP"
- Or use Git:
  ```bash
  git clone https://github.com/TharushaDhamsara/faculty-login-retry.git
  ```

### Step 3: Navigate to Project Folder
```bash
cd faculty-login-retry
```

### Step 4: Install Dependencies
```bash
pip3 install -r requirements.txt
```

### Step 5: Run the Script
```bash
python3 login_retry.py
```

Or use the shell script:
```bash
bash run.sh
```

---

## Verification Steps

After installation, verify everything is working:

### Check Python Installation
```bash
python --version
```
(Should show version 3.6 or higher)

### Check Required Packages
```bash
pip list
```
(Should show `requests` and `beautifulsoup4`)

### Test the Script
```bash
python login_retry.py
```
(Should prompt for student number)

---

## Quick Reference Commands

| Task | Command |
|------|---------|
| Install packages | `pip install -r requirements.txt` |
| Run script (interactive) | `python login_retry.py` |
| Run with student number | `python login_retry.py EG2019001` |
| View logs | Open `login_attempts.log` file |
| Update packages | `pip install --upgrade -r requirements.txt` |

---

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| "Python is not recognized" | Reinstall Python and check "Add Python to PATH" |
| "No module named requests" | Run `pip install -r requirements.txt` |
| "Permission denied" (Linux/Mac) | Run `sudo` before commands or use `chmod +x run.sh` |
| Script won't start | Check that you're in the correct folder |

---

## Getting Help

1. Check the `login_attempts.log` file for detailed errors
2. Make sure you have an active internet connection
3. Verify the university server is online
4. Contact your university IT support

---

**Ready to use! Follow the steps above for your operating system.**
