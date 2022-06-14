# Basics from documentation. 

# Here is an html doc, be using as an example througn out this. 

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# running this 'three sisters' doc throgh bs4 gives us a BeautifulSoup object, which represents the doc as a nested data structure. 

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())


# Here are some simple ways to navigate that data structure. 

print(soup.title) # prints the whole title tag

print(soup.title.name) # only title name i.e 'title' here 

print(soup.title.string) # title given in the doc 'The Dormouse"s story'

print(soup.title.parent.name) # gives the one step ahead 'head' here
print(soup.title.parent.string) # gives the one step ahead 'head' value

print(soup.title.parent) # gives the one step ahead 'head' tag


print(soup.p) # shows the first <p> in teh body

print(soup.p['class']) # shows the class value in <p>

print(soup.a) # shows first <a> tag 

print(soup.find_all('a')) # shows all <a> tags present in doc

print(soup.find(id='link3')) # shows where id = 'link3' in whole doc. 

# loop through all the similar tags in the doc. 

for link in soup.find_all('a'): # prints all the links in the <a> tags find the doc.
    print(link.get('href'))

# print all <p> paragraphs. without tags

for paras in soup.find_all('p'):
    print(paras.string)

for paras in soup.find_all('p'):
    print(paras['class'])

# Common is to get text from the doc.

print(soup.get_text())
