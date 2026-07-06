import requests
from bs4 import BeautifulSoup
import time
import sys
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('login_attempts.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class FacultyLoginRetry:
    def __init__(self, max_retries=10, retry_delay=2):
        self.url = "http://www.science.kln.ac.lk:8080/(S(mypjl5mftiignykvvzalnjkv))/sfkn.aspx"
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def login_with_retry(self, username):
        """Attempt login with automatic retries"""
        attempt = 0
        
        logger.info(f"Starting login attempts for username: {username}")
        
        while attempt < self.max_retries:
            attempt += 1
            print(f"\n{'='*60}")
            print(f"[Attempt {attempt}/{self.max_retries}] Logging in with username: {username}")
            print(f"{'='*60}")
            logger.info(f"Attempt {attempt}/{self.max_retries}")
            
            try:
                # First, get the login page
                print("→ Fetching login page...")
                response = self.session.get(self.url, timeout=10)
                response.raise_for_status()
                
                # Parse the page to get form fields
                soup = BeautifulSoup(response.content, 'html.parser')
                
                # Try to find the username/student ID input field
                # Adjust the field name based on actual form
                login_data = {
                    'txtUserName': username,  # Adjust field name as needed
                }
                
                # Submit login form
                print("→ Submitting login form...")
                login_response = self.session.post(
                    self.url, 
                    data=login_data,
                    timeout=10
                )
                login_response.raise_for_status()
                
                # Check if login was successful
                if self.is_login_successful(login_response):
                    print(f"\n{'='*60}")
                    print(f"✓ LOGIN SUCCESSFUL on attempt {attempt}!")
                    print(f"{'='*60}\n")
                    logger.info(f"Login successful on attempt {attempt}")
                    return True
                else:
                    print(f"✗ Login attempt {attempt} failed")
                    logger.warning(f"Login failed on attempt {attempt}. Retrying in {self.retry_delay}s...")
                    print(f"→ Waiting {self.retry_delay} seconds before retry...")
                    time.sleep(self.retry_delay)
                    
            except requests.exceptions.Timeout:
                print(f"✗ Timeout on attempt {attempt}")
                logger.error(f"Timeout on attempt {attempt}")
                print(f"→ Waiting {self.retry_delay} seconds before retry...")
                time.sleep(self.retry_delay)
                
            except requests.exceptions.ConnectionError as e:
                print(f"✗ Connection error on attempt {attempt}: {e}")
                logger.error(f"Connection error on attempt {attempt}: {e}")
                print(f"→ Waiting {self.retry_delay} seconds before retry...")
                time.sleep(self.retry_delay)
                
            except requests.exceptions.RequestException as e:
                print(f"✗ Network error on attempt {attempt}: {e}")
                logger.error(f"Network error on attempt {attempt}: {e}")
                print(f"→ Waiting {self.retry_delay} seconds before retry...")
                time.sleep(self.retry_delay)
                
            except Exception as e:
                print(f"✗ Unexpected error: {e}")
                logger.error(f"Unexpected error: {e}")
                time.sleep(self.retry_delay)
        
        print(f"\n{'='*60}")
        print(f"✗ LOGIN FAILED after {self.max_retries} attempts")
        print(f"{'='*60}\n")
        logger.error(f"Login failed after {self.max_retries} attempts")
        return False
    
    def is_login_successful(self, response):
        """Check if login was successful by looking for indicators in response"""
        response_text = response.text.lower()
        
        # Check for logout link (indicates successful login)
        if "logout" in response_text or "sign out" in response_text:
            return True
        
        # Check for error messages that indicate failure
        error_indicators = [
            "invalid username",
            "incorrect",
            "login failed",
            "invalid credentials"
        ]
        
        for indicator in error_indicators:
            if indicator in response_text:
                return False
        
        # If page content changed significantly, likely successful
        if len(response.text) > 5000:  # Successful login pages are usually larger
            return True
        
        return False

def main():
    print("\n" + "="*60)
    print("Faculty of Science Login Retry System")
    print("University of Kelaniya")
    print("="*60 + "\n")
    
    # Get username from command line or user input
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        username = input("Enter your student number (username): ").strip()
    
    if not username:
        print("Error: Username cannot be empty")
        logger.error("Empty username provided")
        return
    
    # Get custom retry settings
    try:
        max_retries = int(input("Enter maximum retry attempts (default 10): ") or "10")
        retry_delay = int(input("Enter delay between retries in seconds (default 2): ") or "2")
    except ValueError:
        max_retries = 10
        retry_delay = 2
    
    # Create login handler and attempt login
    login_handler = FacultyLoginRetry(max_retries=max_retries, retry_delay=retry_delay)
    success = login_handler.login_with_retry(username)
    
    if success:
        print("You can now access the faculty system!")
    else:
        print("Please try again or contact IT support.")

if __name__ == "__main__":
    main()
