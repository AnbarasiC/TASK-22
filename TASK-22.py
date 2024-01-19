"""Using Python Selenium Automation and the URL https://www.instagram.com/guviofficial/
kindly do the following mentioned tasks:
1) Use either Relative or Absolute XPATH only for the task.
2) Extract the total number of Followers and Following from the URL mentioned above."""

from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new Chrome browser instance
driver=webdriver.Chrome()

# Wait for the profile to load
driver.implicitly_wait(10)

# Open the URL
driver.get("https://www.instagram.com/guviofficial/")

#Maximize the window
driver.maximize_window()

#Extract the total number of Followers
followers=driver.find_element(By.XPATH,"//span[contains(text(),'124K')]")
print("The total number of Followers: ",followers.text)

#Extract the total number of Following
following=driver.find_element(By.XPATH,"//span[@class='html-span xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x1hl2dhg x16tdsg8 x1vvkbs'][normalize-space()='4']")
print("The total number of Following: ",following.text)

# Close the browser
driver.quit()