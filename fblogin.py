from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Chrome('location of your chrome driver')
browser.get('https://www.facebook.com/')
assert "Facebook" in browser.title
elem= browser.find_element_by_id("email")
elem.send_keys('your email ID')
elem=browser.find_element_by_id("pass")
elem.send_keys('your facebook password')
elem.send_keys(Keys.RETURN)



