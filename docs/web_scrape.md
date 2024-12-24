## Setup
- [lxml](https://lxml.de/)
    - Library or processing XML and HTML in python
- [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/)
    - Library for pulling data out of HTML and XML files

```bash
pip install lxml
pip install bs4 # Beautiful Soup
```

## Grabbing HTML elements
!!! example "Usage"
    [Beautiful Soup HTML Tree Navigation](https://beautiful-soup-4.readthedocs.io/en/latest/#navigating-the-tree)
    ```python
    # Get web page html content
    response = requests.get("page_url")
    raw_html = response.text
    # This returns the html content for the webpage
    # similar to what we see on inspecting the webpage
    # The above content is returned as an unstructured string

    # Convert the unstructured string to a structured html content
    structured_html = bs4.BeautifulSoup(raw_html, "lxml")

    # Get all elements for a tag
    tag_elements = structured_html.tag_name
    tag_elements.contents
    # This returns a list of all occurences of the tag in the page

    # Get all elements for an id
    tag_elements = structured_html.select("#id_name")
    
    # Get all elements for a class
    # If the class name has a space, replace it with a dot in the select statement
    tag_elements = structured_html.select(".class_name")
    # Get attributes and children for each element
    for tag_element in tag_elements:
        tag_element.attrs
        tag_element.contents   # same as list(tag_element.children)

    # Get any elements named <tag2> that are within an element named <tag1>
    tag_elements = structured_html..select('div span')

    # Get any elements named <span> that are directly within an element named <div>, with no other element in between
    tag_elements = structured_html..select('div > span')

    # Get the content of the first occurence of the tag
    tag_content = tag_elements[0].getText()
    ```

??? abstract "Sample Code"
    ```python
    import requests
    import bs4
    import re

    response = requests.get("https://en.wikipedia.org/wiki/Sholay")
    raw_html = response.text

    structured_html = bs4.BeautifulSoup(raw_html, "lxml")
    tag_elements = structured_html.title
    # returns [<title>Sholay - Wikipedia</title>]

    tag_content = tag_elements.contents[0]
    # tag_elements[0].getText() and tag_elements[0].text also return the same result as above
    # returns 'Sholay - Wikipedia'

    # Get list of all items with class "mw-heading"
    class_elements = structured_html.select(".mw-heading")
    for textval in class_elements:
        print(textval.text)
    ```