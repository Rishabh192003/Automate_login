from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

services_obj = Service("C:/Users/rj054/OneDrive/Documents/Custom Office Templates/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=services_obj)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
sleep(2)


Username = driver.find_element(By.ID, "username")
Username.send_keys("aryanggg@gmail.com")

Password = driver.find_element(By.ID, "password")
Password.send_keys("rijygn#")



login_btt = driver.find_element(By.XPATH, "//button[@class='btn__primary--large from__button--floating']")
sleep(1)
login_btt.click()


WebDriverWait(driver, timeout=10).until(
    lambda x: x.execute_script("return document.readyState === 'complete'")
)

username_error_messages = ["Please enter a valid username."]
password_error_messages = ["Wrong email or password. Try again or create an account"]



username_errors = driver.find_elements(By.ID, "error-for-username")
password_errors = driver.find_elements(By.ID, "error-for-password")


username_error_texts = [e.text.strip() for e in username_errors if e.text.strip()]
password_error_texts = [e.text.strip() for e in password_errors if e.text.strip()]


print("Username Errors:", username_error_texts)
print("Password Errors:", password_error_texts)


if any(error in username_error_texts for error in username_error_messages):
    print("[!] Login failed: Invalid Username")
if any(keyword in text for text in password_error_texts for keyword in password_error_messages):
    print("[!] Incorrect Password")
elif not username_errors and not password_errors :
    print("[+] Login successful")

sleep(2)
driver.close()
