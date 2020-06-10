from selenium.webdriver import Chrome

# User Prompts for future logging in 
email_ = str(input("Enter your USERNAME: "))
password_ = str(input("Enter your PASSWORD: "))

# store base url
# initialize webdriver exe path
base_url = "https://www.coursera.org/?authMode=login"
driver = Chrome(executable_path="D:\Python\AutoSubmission\chromedriver.exe")
# force open in maximised window
driver.maximize_window()
driver.implicitly_wait(10) # assuming that the login screen will appear after x seconds; x = 10
driver.get(base_url)  # load in browser window
# check if correct webpage is loaded, assertionerror wil be raised if mismatch
assert "Coursera" in driver.title

# Find HTML/CSS element to insert username and password
email = driver.find_element_by_name("email")
password = driver.find_element_by_name("password")
login = driver.find_element_by_tag_name("button")

# Execute autofill
email.send_keys(email_)
password.send_keys(password_)
# Execute click
login.click()











driver.close()  # exit browser / terminate driver
