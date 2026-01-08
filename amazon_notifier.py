import time
import random 
import smtplib 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- 1. email setup ---
SENDER_EMAIL = "sender.email@gmail.com"       # add your mail
SENDER_PASSWORD = "your_app_password"         # Use App Password, NOT your real password (find on google if having problem).
RECEIVER_EMAIL = "receiver.email@gmail.com"   # Note receiver and sender can be same 


# --- 2. mail sending function ---
def send_notification(product_name, price, link):
    try:
        # Establish connection with Gmail Server (Port 587)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(SENDER_EMAIL, SENDER_PASSWORD)

        subject = f" Price Drop Alert: {product_name[:15]}..."
        body = f"Boss, Price is now Rs.{price}!\n\nLink: {link}"
        msg = f"Subject: {subject}\n\n{body}"
        # (utf-8 for emoji's adding if you like)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.encode('utf-8')) 
        server.quit()
        print(" >> Email Sent to you Successfully!")
        
    except Exception as e:
        print(f"   Email Error: {e}")

# --- 2. cleaning function for text ---
def get_clean_price(price_text):
    if not price_text: return 0
    clean_text = price_text.replace("₹", "").replace(",", "").strip()   # Remove currency symbols and commas
    if "." in clean_text: clean_text = clean_text.split(".")[0] # you can remove if condition it still work the same 
    try: return int(clean_text)
    except: return 0

# --- 3. chrome setup ---
options = Options()
# options.add_argument("--headless=new") # for demo only 
options.add_argument("--window-size=1920,1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10) # better wait (10 sec max)

products = [
    {"url": "https://www.amazon.in/Logitech-B170-Wireless-Mouse-Black/dp/B01J0XWYKQ", "budget": 1000}, 
    {"url": "https://www.amazon.in/TRIUMPH-Speed-Phantom-Booking-Ex-Showroom/dp/B0F53FKZ12", "budget": 240000}
]

print(" Starting Tracker with Email Notification...")

try:
    for item in products:
        link = item["url"]
        my_budget = item["budget"]
        driver.get(link)
        
        try:
            # Wait for elements to load 
            title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text.strip()
            price_elm = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "a-price-whole")))
            
            raw_price = price_elm.text
            actual_price = get_clean_price(raw_price) # cleaning function for if logic
            
            print(f"\nChecked: {title[:20]}... | Price: {actual_price}")
            
            # --- decision ---
            if actual_price <= my_budget:
                print("  Price is LOW! Sending Email...")
                send_notification(title, actual_price, link)
            else:
                print(f"   High Price (Wait for ₹{actual_price - my_budget} drop).")
                
        except Exception as e:
            print(f"   Skip: {e}")
            
        time.sleep(random.uniform(2, 5)) # make more human feel and less bot(Randomness prevents blocking)

except Exception as e:
    print(e)
finally:
    driver.quit()