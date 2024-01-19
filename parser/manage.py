import csv


def get_csv(link: str):
    print(f"START PARSING {link}")

    with open("result.csv", mode="w") as f:
        # reader = csv.reader(f)
        return f


if __name__ == "__main__":
    get_csv("https://books.toscrape.com/catalogue/category/books/travel_2/index.html")
