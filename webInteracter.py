from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# store base url
# initialize webdriver exe path
base_url = "https://www.coursera.org"
driver = webdriver.chrome("D:/Python/AutoSubmission/chromedriver.exe")
# force open in maximised window
driver.maximise_window()
driver.implicitly_wait(10) # wait 10s before launch for error handling on laggy devices
driver.get(base_url) # load in browser window
# check if correct webpage is loaded, assertionerror wil be raised if mismatch
assert "coursera" in driver.title

driver.close() # exit browser / terminate driver









