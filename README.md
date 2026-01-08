# Amazon Price Tracker & Email Notifier

A smart automation bot built with Python and Selenium that monitors Amazon product prices in real-time and sends an email alert when the price drops below your target budget.

## Features

* **Real-Time Tracking:** Scrapes live pricing data from Amazon.
* **Smart Cleaning:** Converts raw text (e.g., `₹ 1,499.00`) into usable numbers (`1499`) for calculation.
* **Anti-Bot Evasion:** Uses Random Delays and User-Agent headers to act like a human.
* **Email Alerts:** Integrates with Gmail (SMTP) to send instant notifications.
* **Robust Error Handling:** Uses `WebDriverWait` to handle slow internet or loading issues.

## Tech Stack

* **Python 3.x**
* **Selenium WebDriver** (Automation)
* **SMTP Library** (Email Notification)

## How to Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Amazon-Price-Tracker.git](https://github.com/YOUR_USERNAME/Amazon-Price-Tracker.git)
    cd Amazon-Price-Tracker
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Email:**
    * Open the script and locate the `SENDER_EMAIL` section.
    * Generate a **Google App Password** (Don't use your real Gmail password).
    * *Note: For security, never push your real passwords to GitHub.*

4.  **Run the Bot:**
    ```bash
    python amazon_notifier.py
    ```

## Logic Breakdown

The bot follows this decision-making process:
1.  **Visit URL:** Opens the product page using Chrome.
2.  **Extract:** Finds the price element using Class Selectors.
3.  **Clean:** Removes currency symbols (`₹`) and commas to convert text to integer.
4.  **Compare:** Checks `if current_price <= my_budget`.
5.  **Notify:** If true, sends an email via SMTP. If false, waits for the next cycle.

## Disclaimer
This project is for **educational purposes only**. Web scraping may violate Amazon's Terms of Service. Use responsibly and do not overload their servers with rapid requests.

---
**Created by Shubham-s** | *Built during Python Automation Training*
