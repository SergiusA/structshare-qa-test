import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/")

#task2.1 Broken Image + Screenshot proove
driver.find_element(By.XPATH, '/html/body/div[2]/div/ul/li[4]/a').click()
driver.get_screenshot_as_file('D:/test2.2.png')
time.sleep(3)

#task2.2 FileUpload
driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(1)
driver.find_element(By.ID, 'file-upload').send_keys('D:/test2.2.png')
time.sleep(2)
driver.find_element(By.ID, 'file-submit').click()
time.sleep(1)

#task2.3 Checkboxes, Change both values
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/input[1]').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/form/input[2]').click()
time.sleep(1)

#task2.4 Hover elements 2 -> 3 -> 1
driver.get('https://the-internet.herokuapp.com/hovers')
time.sleep(2)
action_hover = ActionChains(driver)
action_hover.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/img')).perform()
time.sleep(1)
action_hover.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/img')).perform()
time.sleep(1)
action_hover.move_to_element(driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/img')).perform()
time.sleep(1)

#task2.5 Add/Remove elements 1 -> 3 -> 2
driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
driver.find_element(By.CSS_SELECTOR, '.example > button:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.example > button:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.example > button:nth-child(1)').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/button[3]').click()
time.sleep(1)

#task2.6 Floating and Scroll
driver.get('https://the-internet.herokuapp.com/floating_menu')
time.sleep(1)
driver.execute_script('window.scrollTo(0,750);')
time.sleep(1)
driver.execute_script('window.scrollTo(0,450);')
time.sleep(1)

#task2.7 Login/Logout
driver.get('https://the-internet.herokuapp.com/login')
driver.find_element(By.ID, 'username').send_keys('tomsmith')
time.sleep(1)
driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, '.fa').click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, '.icon-2x').click()
time.sleep(3)

#Bonus task "0 is last symbol" for Key Press
driver.get('https://the-internet.herokuapp.com/key_presses')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="target"]').send_keys('aRm')
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="target"]').send_keys('Nr#%2mj0')
time.sleep(1)
a = driver.find_element(By.ID, 'result').text
if a == 'You entered: 0': 
    driver.find_element(By.ID, 'target').clear()
    time.sleep(1)
    driver.find_element(By.ID, 'target').send_keys('Success!')
else: 
    driver.find_element(By.ID, 'target').clear()
    time.sleep(1)
    driver.find_element(By.ID, 'target').send_keys('Something went wrong!')
time.sleep(3)

driver.quit