from news_ext import *
from news_scrap import *
from news_nlp import *
import time
# Console Display
print("Welcome You will now see the latest technology articles in the New York Times...")
print("Extracting article hyperlinks...")
time.sleep(2)
print("Retrieving summaries...")
print()
time.sleep(2)

# Gets all the latest URL's from the NY Times Technology Section. (see news_extract.py for more detail)
content_string = get_content_string(my_url)
starts, ends = find_occurrences(content_string)
url_list = get_all_urls(starts, ends, content_string)

for url in url_list:
    print("Article URL: " + str(url))
    article_summary = summarize_article(url)
    find_sentiment(article_summary)
    print("------------------------------------------------")
    time.sleep(7)  # Allows user to get through all the text.

print()
print("The articles have been successfully extracted!")
print("In total, we were able to extract " + str(len(url_list)) + " different articles!")
