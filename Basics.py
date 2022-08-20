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

# -------------------------------------------Basics are done ------------------------

# Tag:
#  

soup1 = BeautifulSoup('<b class="boldest">Extremely bold</b>', "html.parser")
tag = soup1.b
print("type of tag", type(tag)) # type of tag

print(soup1.b.name) 

tag.name = "blockquote" # changing tag name by assigning a new value

print(tag)

# Attributes, can be accessed as dict

print(tag['class'])

# can access the dictionary directly as .attrs

print(tag.attrs)

# add, remove, modify tag's attibutes. as tag is a dictionary.

tag['class'] = 'verybold'

print(tag['class'])

tag['another_attribute'] = 1

print(tag)

# del 

del tag['class']
del tag['another_attribute'] 

print(tag)

print(tag.get('class'))

# multi values attributes. as a list.

# The most common multi valued attribute is 'class', that this 
# can have more than one css class, others include rel, rev, accept-charset, 
# headers, accesskey. 

css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')

print(css_soup.p['class'])


# not tall will gives the list as it has a space. 

id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
print(id_soup.p['id'])

# this can be disable 
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)

print(css_soup.p['class'])

# use get_attribute_list

print(css_soup.p.get_attribute_list('class'))

# for xml there are no multivalues lists


xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])

# you can configure this using multi_valued_attribute argument as 
# class is multi.
class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
print(xml_soup.p['class'])
