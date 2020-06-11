import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get("https://www.computerhope.com/issues/ch001789.htm")
content = page.content

# Parse htm/html document and make it more organized
soup = BeautifulSoup(content, "html.parser")
prettify_html = soup.prettify()
# print(list(soup.children))
html = list(soup.children)[7]
body = list(html.children)[3]
# print(list(body.children))
# print(soup.find_all("article"))
div1 = list(body.children)[3]
div2 = list(div1.children)[5]

# Find headers --> Titles of our file types
title_list = soup.find_all("h2")
ext_list = soup.find("article").find_all("b")
# print(ext_list)

# Scraped into array
tags = [tag.get("id") for tag in title_list]
exts = [tag.text for tag in ext_list]
# print(exts)

#Output to .txt file

# Output to text file
def filename(name):
    return name

def create_txt(create_file, array):
    with create_file as f:
        for item in array:
            f.write("%s\n" % item)

create_txt((open(filename("tags.txt"), "w+")), tags)
create_txt((open(filename("extensions.txt"), "w+")), exts)

# Output to excel file(.csv)
def create_csv(name, filename, array):
    dict = {name: array}
    dataframe = pd.DataFrame(dict)
    dataframe.to_csv(filename)

create_csv("Catagories", "tags.csv", tags)
create_csv("Extensions", "extensions.csv", exts)
