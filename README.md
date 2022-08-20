# WebScraping
Web Scraping Learning Repo 

> List of Python libraries for Scraping.

- Requests
- lxml
- Beautifulsoup
- Selenium
- Scrapy

### Learning Through documentation.
> Here this repo consists of mostly learning process, through documentation which is publicly available. 

- [Documentation Link](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). 

### Beautiful Soup can be adapted to third party dependencies.
- python's html.parser BeautifulSoup(markup, "html.parser")
 Advantages (Decent speed, lenient), Disadvantages(slow as lxml, less lenient than html5lib)
- lxml's HTML parser 
    Advantage(Very fast, lenient), Disadvantages(External c dependency)
- lxml's XML parser BeautifulSoup(markup, "lxml-xml") or BeautifulSoup(markup, "xml")
 Advantages(Very fast), Disadvantages(External C dependency)
-html5lib BeautifulSoup(markup, "html5lib")
 Advantages(Extremely lenient, parses pages as web pages does, creates valid html5), Disadvantages(Veryslow, External python dependency)

> To parse a document. 

```python
from bs4 import BeautifulSoup

with open("index.html") as fp:
    soup = BeautifulSoup(fp, "html.parser")

soup = BeautifulSoup("<html>a web page</html>", "html.parser")
```

> First the document is converted to unicode, and HTML entities are converted to Unicode characters.