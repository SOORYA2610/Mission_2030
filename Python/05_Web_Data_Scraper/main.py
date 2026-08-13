import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

url = "https://books.toscrape.com/"
page_number = 1

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Title", "Price", "Availability"])

    while url:
        response = requests.get(url)
        print("Status Code:",response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("article", class_ = "product_pod")
        print("Books found:", len(books))

        for book in books:
            title = book.h3.a["title"]
            price = book.find("p", class_ = "price_color").text.replace("Â£", "£")
            availability = book.find("p", class_ = "instock availability").text.strip()

            writer.writerow([title, price, availability])

            print("\nTitle:", title)
            print("Price:", price)
            print("Availability:", availability)

        next_page = soup.find("li", class_ = "next")

        if next_page:
            next_url = next_page.a["href"]
            url = urljoin(url, next_url)
            print("Next page:", url)
        else:
            url = None

print("\nData saved to books.csv")