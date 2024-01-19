from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(
#     By.XPATH,
#     "/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]",
# )
#
# article_count.click()
# print(article_count.text)

# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# # Find the "Search <input> by Name
# search = driver.find_element(By.NAME, value="search")
# # Sending keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
# driver.find_element(By.XPATH, "")

first_name_record = driver.find_element(By.XPATH, "/html/body/form/input[1]")
first_name_record.send_keys("Ivan")

last_name_record = driver.find_element(By.XPATH, "/html/body/form/input[2]")
last_name_record.send_keys("Bondarenko")

email_record = driver.find_element(By.XPATH, "/html/body/form/input[3]")
email_record.send_keys("EMAIL@gsdfg.dfg")

sing_in_button = driver.find_element(By.XPATH, "/html/body/form/button")
sing_in_button.click()

# driver.quit()
