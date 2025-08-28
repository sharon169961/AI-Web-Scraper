import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching Chrome browser...")
    
    # Path to the ChromeDriver executable
    chrome_driver_path = r"C:\Users\sharo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"

    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

    try:
        # Open the website
        driver.get(website)
        print("Page loaded...")
        
        # Allow the page to load completely
        time.sleep(5)
        
        # Get the HTML source of the page
        html = driver.page_source
        return html
    finally:
        # Close the browser
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body

    # Return the body content as a string, or an empty string if not found
    if body_content:
        return str(body_content)
    return ""

def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    # Remove all <script> and <style> elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Extract the text content and clean it up
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content

def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]
