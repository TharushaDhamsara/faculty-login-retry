# Faculty Login Retry System

Automated login retry system for Faculty of Science, University of Kelaniya information system. This tool continuously retries login until it succeeds, handling network failures gracefully.

**System URL:** http://www.science.kln.ac.lk:8080/(S(mypjl5mftiignykvvzalnjkv))/sfkn.aspx

## Features

✓ Automatic login retry mechanism  
✓ Customizable retry attempts and delays  
✓ Detailed logging of all attempts  
✓ Network error handling  
✓ Command-line and interactive modes  
✓ Easy to use  

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Step 1: Download Python (if not installed)
1. Go to https://www.python.org/downloads/
2. Download Python (version 3.8 or higher)
3. **Important:** During installation, check ✓ "Add Python to PATH"
4. Click Install

### Step 2: Clone or Download this Repository
```bash
# Using Git
git clone https://github.com/TharushaDhamsara/faculty-login-retry.git
cd faculty-login-retry

# OR manually download and extract the ZIP file
```

### Step 3: Install Required Packages
```bash
pip install -r requirements.txt
```

## How to Run

### Method 1: Interactive Mode (Easiest)
```bash
python login_retry.py
```
Then enter your student number when prompted.

### Method 2: Command Line Mode
```bash
python login_retry.py YOUR_STUDENT_NUMBER
```
Replace `YOUR_STUDENT_NUMBER` with your actual student ID.

### Example:
```bash
python login_retry.py EG2019001
```

## Usage

1. **Open Command Prompt/Terminal** in the project folder
2. **Run the script:**
   ```bash
   python login_retry.py
   ```
3. **Enter your student number** when prompted
4. **Customize retry settings** (or press Enter for defaults):
   - Maximum retry attempts (default: 10)
   - Delay between retries in seconds (default: 2)
5. **Wait** for the script to attempt login repeatedly
6. **Success!** Once logged in, you can access the faculty system

## Output

The script provides:
- **Real-time feedback** on each login attempt
- **Log file** (`login_attempts.log`) with detailed information
- **Visual indicators** (✓ for success, ✗ for failure)
- **Timing information** between retries

## Logs

All login attempts are saved in `login_attempts.log` file. You can view this file to see the history of all attempts.

## Troubleshooting

### Issue: "Python is not recognized"
- **Solution:** Reinstall Python and make sure to check "Add Python to PATH"
- **Verify:** Open Command Prompt and type `python --version`

### Issue: "No module named 'requests'"
- **Solution:** Run `pip install -r requirements.txt`
- **Verify:** Run `pip list` to see installed packages

### Issue: "Connection refused"
- **Solution:** The server might be down. Try again later or check your internet connection.

### Issue: "Still can't login after many attempts"
- Check if your student number is correct
- Verify your internet connection
- Check if the university server is online
- Contact IT support at the university

## Configuration

You can customize the retry behavior:

```python
# In login_retry.py
login_handler = FacultyLoginRetry(
    max_retries=20,      # Maximum number of retry attempts
    retry_delay=3        # Delay between retries in seconds
)
```

## Important Notes

⚠️ **Username Only:** This system uses only student number (username). Password is not required.

⚠️ **Network:** Ensure you have active internet connection before running.

⚠️ **Server Status:** The university server must be online for login to succeed.

## Support

If you encounter issues:
1. Check the `login_attempts.log` file for detailed error messages
2. Verify your student number is correct
3. Check your internet connection
4. Contact University IT support

## License

This project is provided as-is for educational purposes.

---

**Created for:** Faculty of Science, University of Kelaniya  
**Last Updated:** 2024
