from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

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

# driver.get("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
driver.get("https://books.toscrape.com/catalogue/category/books/mystery_3/index.html")
# driver.find_element(By.XPATH, "")

# •	По окончанию парсинга выдаёт csv c товарами в котором написаны(
# Название,
# цена,
# ссылка,
# есть ли в наличии
# и их характеристики)


# /html/body/div/div/div/div/section/div[2]/ol/li/article/div[2]/p[1]
# /html/body/div/div/div/div/section/div[2]/ol/li/article/div[2]/p[1]
books_data = []

while True:
    books_links = driver.find_elements(
        By.XPATH, "/html/body/div/div/div/div/section/div[2]/ol/li/article/h3/a"
    )

    for book_link in books_links:
        print(f"Book name:{book_link.text}")
        book_link.click()
        book_description = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[2]/article/p"
        )
        print(book_description.text)

        books_data.append(
            {
                # "book_title": books_name_links[ind].text,
                # "book_author": book_author,
                "book_publishing": book_description.text,
                # "book_new_price": book_new_price,
                # "book_old_price": book_old_price,
                # "book_sale": book_sale,
                # "book_status": book_status
            }
        )

        driver.back()

    next_page_button = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div/section/div[2]/div/ul/li[2]/a"
    )
    if next_page_button:
        next_page_button.click()
    else:
        break

for book in books_data:
    with open("books.csv", "a") as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                f"Book name:{book['book_publishing']}",
                # f"Book price:{books_prices[ind].text}",
                # f"Book description:{book_description.text}",
            )
        )


# first_name_record.send_keys("Ivan")

# /html/body/div/div/div/div/section/div[2]/ol/li/article/h3/a
# /html/body/div/div/div/div/section/div[2]/ol/li/article/h3/a

# last_name_record = driver.find_element(By.XPATH, "/html/body/form/input[2]")
# last_name_record.send_keys("Bondarenko")
#
# email_record = driver.find_element(By.XPATH, "/html/body/form/input[3]")
# email_record.send_keys("EMAIL@gsdfg.dfg")
#
# sing_in_button = driver.find_element(By.XPATH, "/html/body/form/button")
# sing_in_button.click()

# driver.quit()
# /html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a
# [{'Book Name': '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1'}, {'Description': '/html/body/div/div/div[2]/div[2]/article/p'}, {'UPC': '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[1]/td'}, {'Product Type': '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[2]/td'}, {'Tax': '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[5]/td'}, {'Availability': '/html/body/div/div/div[2]/div[2]/article/table/tbody/tr[6]/td'}]
