#This will not run on online IDE
import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/MEDITIVE-Bluetooth-Digital-Analyzer-Composition/dp/B0867ZRT5B/ref=sr_1_9?crid=2KY7QJ1DP34Z7&dib=eyJ2IjoiMSJ9.hPaRpiOvPxQBYGhnomSWpFNqA36K5aV2tghXpbFnHTXtaQ5vhxNdk1I5yuTBYYDC-NticqPLwQDVWsSbHI1jqtPjj44zFhizFIApV-QFpRxMHAh34Bqm-p5D0H0LQhgSLdeGOU1bZn1apRptXYhVVmNNi72mmCnw9fRNL0YoEfWhgLU0HbmrKrqs5ThShRGAJV_xYeDeWYtA1XeGmbS8BkBpf0fjOfUwNr8N45L_A5o2H8Tlg1uectBmUYQ885bYJX59djhsAEPlDPA877Iq-IU3wyiUEWo6Ht2z6O1CcVj0zOftOM2ICv6K6DbFy9_SW1Rhcu6ej_eWmmGk6a4IaybHSUcmc4TZTghYV_DGztyjGXRm-0_7wGO0A2apxWvrRA5AfmMcg5kDRwd8lTXxvtki6Ah5P_qkHft3OXq_xEDukFTTcYqqGgwoN0w1WXEu.Xqo21YbByKDjaOshcsNV-0EMAprtrR0t6D4gd9XheEI&dib_tag=se&keywords=weighing+scale+for+body+weight&qid=1739213460&sprefix=%2Caps%2C303&sr=8-9"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",  # Do Not Track Request Header
    "Connection": "keep-alive",
}
r = requests.get(URL, headers=headers)
soup = BeautifulSoup(r.content, "lxml")
productTitle = soup.find("span", attrs={"id": "productTitle"}).text.strip()

prices = soup.find_all("span", class_="a-price-whole")
productPrice = prices[0].text.strip()

savings = soup.find_all("span", class_=re.compile("savingsPercentage"))
# productDiscount = savings[0].text.strip()

table = soup.find('table', class_="a-normal a-spacing-micro")
productfeats = table.find_all('tr')
productfeat = []
for elements in productfeats:
    productfeat.append(elements.text)

aboutlist = soup.find('ul', class_="a-unordered-list a-vertical a-spacing-mini")
aboutpoints = aboutlist.find_all('li')
# aboutfeat = []

# for points in aboutpoints:
#     aboutfeat.append(points.text)

product_infoman = "\n".join([point.text.strip() for point in aboutpoints])


reviewlist = soup.find('ul', class_="a-unordered-list a-nostyle a-vertical review-views celwidget")
reviewpoints = reviewlist.find_all('li')
reviews = []

for review in reviewpoints:
    reviews.append(review.text)


# print(productTitle)
# print(productPrice)
# print(productfeat)
# print(aboutfeat)
# print("***************************************************")
# print("**********************REVIEWS**********************")
# print("***************************************************")
# print(reviews)
# print(productDiscount)
# soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
# print(soup.prettify())
def summarize(product_info):

    urlgpt = "http://localhost:1234/v1/completions"

    prompt = f"""You will be given information about a certain product on Amazon.
    You have to summarize the info in concise manner that only highlights the features
    and no other nonsense. 
    The information about the product is: {product_info}"""

    data = {
        "prompt": prompt
    }

    try:
        # Send the request to the server
        response = requests.post(urlgpt, json=data)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Extract the generated answer from the response
        response_json = response.json()

        # Access the 'text' from the first choice
        answer = response_json["choices"][0]["text"]

        return answer.strip()  # Strip unnecessary spaces or newlines

    except requests.exceptions.RequestException as e:
        print(f"Error communicating with the server: {e}")
        return None
    except KeyError as e:
        print(f"Error parsing the response: Missing key {e}")
        return None
    
generated_answer = summarize(product_infoman)
print(generated_answer)