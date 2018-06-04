from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome('/home/aniket/Documents/chromedriver')
browser.get('https://www.facebook.com/')
assert "Facebook" in browser.title
ele= browser.find_element_by_id("email")
ele.send_keys('your email ID')
ele=browser.find_element_by_id("pass")
ele.send_keys('facebook password')
ele.send_keys(Keys.RETURN)



