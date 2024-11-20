"""Getting relevant information from API and Emailing it to ourselves
"""
## 1. Import modules, request for pulling content from the web, and emailsender to send email
import requests
from EmailSender import send_email

## 2. Get API Key and endpoint url from the newsapi website and save them in a variable
API_KEY = "enter API Key here"

## 8. Make the endpoint dynamic by using variables to access features. In this case, we limit the language to english, the result to 20 and topic to an input variable
## Review the api documentation to see what can be changed or added to end point
lang = "en"
result = "20"
topic = input("Type in the Topic: ")

## 9. Made the endpoint more readable
url = (f"https://newsapi.org/v2/everything"
       f"?q={topic}"
       f"&sortBy=popularityAt"
       f"&apiKey={API_KEY}"
       f"&language={lang}"
       f"&pageSize={result}")

## 3. Use the get method to save the endpoint's response
response = requests.get(url)

## 4. Convert response to JSON for better accessibility.
api_content = response.json()

## 5. Created an empty string variable to store the news once it is accessed
news = ""

## 6. Access API article dictionary with for loop. Got the key with help of debugger.
for article in api_content["articles"]:
    ## 7. Store the title, URL and description from the api to news variable. Use Concatenation.
    ## Sometimes api gives none type objects or "[removed]" content, which breaks the program, so use if-else conditionals to filter them out
    if article["title"] is not None and article["description"] is not None and article["title"] != "[Removed]":
        news= news + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"


## 10. Send email of this news to yourself
send_email(f"My daily News on {topic}", news)
print("Email Sent")