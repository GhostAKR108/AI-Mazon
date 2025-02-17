from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS
import re
import random

app = Flask(__name__)
CORS(app) # This line enables CORS for all routes.


@app.route('/scrape', methods=['POST'])  
def scrape():
    data = request.get_json()
    url = data.get('url')
    # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    # proxies_list = ["128.199.109.241:8080","113.53.230.195:3128","125.141.200.53:80","125.141.200.14:80","128.199.200.112:138","149.56.123.99:3128","128.199.200.112:80","125.141.200.39:80","134.213.29.202:4444"]
    # proxies = {'https': random.choice(proxies_list)}
    if not url:
        return jsonify({"error": "URL is required"}), 400
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "DNT": "1",  # Do Not Track Request Header
        "Connection": "keep-alive",
    }
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, "lxml")
    productTitle = soup.find("span", attrs={"id": "productTitle"}).text.strip()

    prices = soup.find_all("span", class_="a-price-whole")
    productPrice = prices[0].text.strip()

    # savings = soup.find_all("span", class_=re.compile("savingsPercentage"))
    # productDiscount = savings[0].text.strip()

    table = soup.find('table', class_="a-normal a-spacing-micro")
    productfeats = table.find_all('tr')
    # productfeat = []
    # for elements in productfeats:
    #     productfeat.append(elements.text)
    productfeat = "\n".join([elements.text.strip() for elements in productfeats])

    aboutlist = soup.find('ul', class_="a-unordered-list a-vertical a-spacing-mini")
    aboutpoints = aboutlist.find_all('li')
    # aboutfeat = []

    # for points in aboutpoints:
    #     aboutfeat.append(points.text)
    aboutfeat = "\n".join([point.text.strip() for point in aboutpoints])

    reviewlist = soup.find('ul', class_="a-unordered-list a-nostyle a-vertical review-views celwidget")
    reviewpoints = reviewlist.find_all('li')
    # reviews = []

    # for review in reviewpoints:
    #     reviews.append(review.text)
    reviews = "\n".join([review.find('div', class_='a-expander-content reviewText review-text-content a-expander-partial-collapse-content').find('span').text.strip() for review in reviewpoints])


    # print(productTitle)
    # print(productPrice)
    # print(productfeat)
    # print(aboutfeat)
    # print("***************************************************")
    # print("**********************REVIEWS**********************")
    # print("***************************************************")
    # print(reviews)

    urlgpt = "http://localhost:1234/v1/completions"

    prompt = f"""Summarize the product details and user reviews for an Amazon product.

    Product Name: {productTitle}
    Product Price: {productPrice}
    Product Features: {productfeat}
    Product Info: {aboutfeat}
    Product Reviews: {reviews}

    Give the product summary in the following format:

    1. Product Name
    2. Product Price
    3. Product Info and Features
    4. Product Review Summary
"""

    data = {
        "prompt": prompt,
        "temperature": 0.7
    }
    try:
        llm_response = requests.post(urlgpt, json=data)  # Set timeout to prevent long waiting
        llm_response.raise_for_status()  # Raise an exception for bad status codes

        # Extract the generated answer from the response
        response_json = llm_response.json()

        # Access the 'text' from the first choice
        answer = response_json["choices"][0]["text"]
        answer = answer.strip()
    
    except requests.RequestException as e:
        answer = f"data: Error communicating with LLM: {e}\n\n"

    # Return the final JSON response with all information
    # return Response(stream_with_context(generate()), content_type='text/event-stream')
    return jsonify({'productinfo': answer})



if __name__ == '__main__':
    app.run(port = 5000)

