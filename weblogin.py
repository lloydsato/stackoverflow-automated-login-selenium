from selenium import webdriver
import time

# defines the path for chrmium driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
# insert path to chrome driver
driver = webdriver.Chrome(PATH)

# open stackoverflow page
driver.get("https://stackoverflow.com")

# look for login button
login_button = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')

# click on login button
login_button.click()

time.sleep(3)

# find username field and enter email address for login
username = driver.find_element_by_xpath('//*[@id="email"]')
uname = input("Enter your username\n")
username.send_keys(uname)

# find password field and enter password for login
password = driver.find_element_by_xpath('//*[@id="password"]')
pwd = input("Enter your password\n")
password.send_keys(pwd)

# click on submit button
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
