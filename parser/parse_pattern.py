import csv

characteristics_file = "characteristics_xpath.csv"


class BookParsePattern:
    def __init__(self):
        self.book_link = ""
        self.book_characteristics = []

    def read_csv_with_characteristics(self):
        with open(characteristics_file, "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            for row_number, row in enumerate(csv_reader):
                key, value = row
                if row_number == 0:
                    self.book_link = value
                else:
                    self.book_characteristics.append({key: value})


if __name__ == "__main__":
    book = BookParsePattern()
    book.read_csv_with_characteristics()
    print(book.book_link)
    print(book.book_characteristics)
