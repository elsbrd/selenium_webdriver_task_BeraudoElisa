from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
URL = r"https://www.wikipedia.org/"
english_link_locator = "js-link-box-en"
search_locator = "searchInput"
search_text = "New York city"

driver = webdriver.Chrome(executable_path="C:\\Users\\elisa\\Downloads\\chromedriver.exe")
driver.get(URL)
driver.minimize_window()
english_link_locator = driver.find_element(By.ID, english_link_locator)
english_link_locator.click()
input_box_element = driver.find_element(By.ID, search_locator)
input_box_element.send_keys(search_text)
input_box_element.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
