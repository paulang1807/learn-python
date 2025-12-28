
```python
# Return the title and contents of the website at the given url. Truncate to 500 characters 
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
url = "https://en.wikipedia.org/wiki/Sholay"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.string if soup.title else "No title found"
if soup.body:
    # Remove unwanted tags using decompose function
    # The following will remove the script, style, img and input tags from the body
    for tags_to_remove in soup.body(["script", "style", "img", "input"]):
        tags_to_remove.decompose()
    text = soup.body.get_text(separator="\n", strip=True)
else:
    text = ""
print((title + "\n\n" + text)[:500])
```
```python
# Get all links from a url
from bs4 import BeautifulSoup
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}
url = "https://en.wikipedia.org/wiki/Sholay"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
links = [link.get("href") for link in soup.find_all("a")]
print([link for link in links if link])
```
```python
# Get names of cast from a wikipedia movie page
import requests
import bs4
import re

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

response = requests.get("https://en.wikipedia.org/wiki/Sholay", headers=headers)
raw_html = response.text

structured_html = bs4.BeautifulSoup(raw_html, "lxml")
tag_elements = structured_html.select(".div-col")
for tag_element in tag_elements:
    for elements in tag_element.contents:
        if isinstance(elements, bs4.element.Tag):
            for element in elements.contents:
                if isinstance(element, bs4.element.Tag):
                    print(element.a.contents[0])
```
```python
# Get all movie poster images from a wikipedia page
import requests
import bs4
import re

response = requests.get("https://en.wikipedia.org/wiki/Sholay")
raw_html = response.text

structured_html = bs4.BeautifulSoup(raw_html, "lxml")

image_class_elements = structured_html.select(".mw-file-element")
image_link_dict = {}
image_suffix = 'poster.jpg'
# creat a dict with the image name and url
for image_src in image_class_elements:
    if re.search(r'(poster.jpg)$', image_src['src']):
        # find the first pattern match ending with 'poster.jpg' and not having '/'
        image_name = re.search(r'([^/]+)(?=poster.jpg)', image_src['src']).group() + image_suffix
        image_link_dict[image_name] = 'https:' + image_src['src']

# for all items in the dict, write file to disk
# Since we are writing images, we need to use binary mode
for key, value in image_link_dict.items():
    print(key, value)
    with open(key,'wb') as f:
        f.write(requests.get(value).content)
```
```python
# Get all unique author names from http://quotes.toscrape.com/
# Another sample url for practicing web scraping is http://books.toscrape.com/index.html

# Initialize variables
page_is_valid = True
authors = set()
page = 1


# If a page number does not exist, "No quotes found!" is dipalyed when trying to access the page
while page_is_valid:

    # Create page url dynammically based on the page number
    page_url = url+str(page)
    
    # Obtain Request
    res = requests.get(page_url)
    
    # If we try to access a page beyond the last page, "No quotes found!" is dipalyed
    if "No quotes found!" in res.text:
        break
    
    # Turn into Soup
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    # Add Authors to our set
    for name in soup.select(".author"):
        authors.add(name.text)
        
    # Go to Next Page
    page += 1

print(f"Unique list of authors:\n{authors}")
```