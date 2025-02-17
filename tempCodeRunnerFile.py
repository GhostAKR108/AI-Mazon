productTitle = soup.find("span", attrs={"id": "productTitle"}).text.strip()

# prices = soup.find_all("span", class_="a-price-whole")
# productPrice = prices[0].text.strip()

# savings = soup.find_all("span", class_=re.compile("savingsPercentage"))
# # productDiscount = savings[0].text.strip()

# table = soup.find('table', class_="a-normal a-spacing-micro")
# productfeats = table.find_all('tr')
# productfeat = []
# for elements in productfeats:
#     productfeat.append(elements.text)

# aboutlist = soup.find('ul', class_="a-unordered-list a-vertical a-spacing-mini")
# aboutpoints = aboutlist.find_all('li')
# aboutfeat = []

# for points in aboutpoints:
#     aboutfeat.append(points.text)

# reviewlist = soup.find('ul', class_="a-unordered-list a-nostyle a-vertical review-views celwidget")
# reviewpoints = reviewlist.find_all('li')
# reviews = []

# for review in reviewpoints:
#     reviews.append(review.text)