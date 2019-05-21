import nltk
from textblob import TextBlob
import requests
from bs4 import BeautifulSoup

positive = 0
negative = 0
neutral = 0
url = requests.get("https://www.imdb.com/title/tt0944947/reviews", timeout = 5)
soup = BeautifulSoup(url.content, "html.parser")
soup.prettify()
review = soup.find_all("div",attrs = {"class" : "text show-more__control"})
for text_1 in review:
    print(text_1.text)
    blob1 = TextBlob(text_1.text)
    x = blob1.sentiment.polarity

    if x < 0:
        print("Negative review")
        negative = negative + 1
    elif x > 0:
        print("Positive review")
        positive = positive + 1
    else:
        print("Neutral review")
        neutral = neutral + 1

print("Positive reviews are : ", positive)
print("Negative reviews are : ", negative)
print("Neutral reviews are : ", neutral)    
