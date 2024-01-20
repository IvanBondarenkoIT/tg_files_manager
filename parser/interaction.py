from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
from parse_pattern import book_xpath


class BookScraper:
    def __init__(self, start_url):
        self.start_url = start_url
        self.books_data = []

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def scrape_books(self):
        self.driver.get(self.start_url)

        while True:
            books_links = self.driver.find_elements(
                By.XPATH, book_xpath.book_name_xpath
            )

            for book_link in books_links:
                book_record = {}
                book_record["Book link"] = book_link.get_attribute("href")
                print(f"Book link:{book_link.get_attribute('href')}")

                book_link.click()

                for book_characteristic in book_xpath.book_characteristics:
                    (
                        book_characteristic_name,
                        book_characteristic_xpath,
                    ) = book_characteristic

                    book_characteristic_value = self.driver.find_element(
                        By.XPATH, book_characteristic_xpath
                    )

                    book_record[
                        book_characteristic_name
                    ] = book_characteristic_value.text

                    print(
                        f"{book_characteristic_name}:{book_characteristic_value.text}"
                    )

                self.books_data.append(book_record)

                self.driver.back()

            next_page_button = None
            try:
                next_page_button = self.driver.find_element(
                    By.XPATH, "/html/body/div/div/div/div/section/div[2]/div/ul/li[2]/a"
                )
            except:
                pass
                # raise Exception(err)

            if next_page_button:
                next_page_button.click()
            else:
                break

    def save_to_csv(self, csv_filename):
        with open(csv_filename, "w") as file:
            writer = csv.writer(file)

            for book in self.books_data:
                print(book)

                writer.writerow(
                    [
                        f"{book_characteristic}:{book_value}"
                        for book_characteristic, book_value in book.items()
                    ]
                )
                # for book_characteristic in book:
                #     value = book[book_characteristic]
                #     print(book_characteristic, value)
                #     writer.writerow([book_characteristic, value])
                # writer.writerow(
                #     [
                #         f"Book link: {book['book_link']}",
                #         f"Book publishing: {book.get('book_publishing', '')}",
                #         # Add other fields as needed
                #     ]
                # )


if __name__ == "__main__":
    scraper = BookScraper(
        # "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
        "https://books.toscrape.com/catalogue/category/books/politics_48/index.html"
    )
    scraper.scrape_books()
    scraper.save_to_csv("books.csv")
