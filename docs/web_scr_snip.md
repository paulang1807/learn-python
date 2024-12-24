
```python
# Get names of cast from a wikipedia movie page
import requests
import bs4
import re

response = requests.get("https://en.wikipedia.org/wiki/Sholay")
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