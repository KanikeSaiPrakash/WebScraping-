import requests
from bs4 import BeautifulSoup
import csv
# making a get request.

req = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

print(req)

# print(req.content)

print(req.url)
print(req.status_code)

# parsing the html

soup = BeautifulSoup(req.content, 'html.parser')
# print(soup.prettify()) # to print the content beautifully using prettify.
# print(soup.get_text()) # to get the entire text of the page

print(soup.title)
print(soup.title.name)
print(soup.title.parent.name)


# entry content is the class, i.e has all  the content of the url.
div_soup = soup.find('div', class_='entry-content')
content = div_soup.find_all('p')

# print(content)

## -----------print only content of the page without tags-------
# for line in content:
#     print(line.text)

# -------------------------------------

s = soup.find('div', id='main')

# getting the left bar

leftbar = s.find('ul', class_='leftBarList')

#All the li under the above ul

content = leftbar.find_all('li')

# print(content)

# for lis in content:
#     print(lis.text)

## -------print the link i.e href in above whole document list------

# for link in soup.find_all('a'):
#     print(link.get('href'))

### ---------- print the links in only li given above----

links_in_leftbar = leftbar.find_all('a')

print('len of links in the given left bar', len(links_in_leftbar))

# for link in links_in_leftbar:
#     print(link.get('href'))


# --------------------------------------

#----------------Extracting IMAGES --------------------

image_list = []

images = soup.select('img')
for image in images: 
    src = image.get('src')
    alt = image.get('alt')
    image_list.append({'src': src, 'alt':alt})

print("len of images_list is ", len(image_list))

# for image in image_list:
#     print(image)

# ---------- scrape from multiple pages from same domain ---------

URL = 'https://www.geeksforgeeks.org/page/1/'

req = requests.get(URL)
soup = BeautifulSoup(req.text, 'html.parser')

titles = soup.find_all('div', attrs = {'class', 'head'})

print(titles[4].text)

# loop through the pages to get the titles.

URL = 'https://www.geeksforgeeks.org/page/'
 
for page in range(1, 10):
 
    req = requests.get(URL + str(page) + '/')
    soup = BeautifulSoup(req.text, 'html.parser')
 
    titles = soup.find_all('div', attrs={'class', 'head'})
 
    # for i in range(4, 19):
    #     if page > 1:
    #         print(f"{(i-3)+page*15}" + titles[i].text)
    #     else:
    #         print(f"{i-3}" + titles[i].text)


# ----------- Multiple urls : ------------------
URL = ['https://www.geeksforgeeks.org','https://www.geeksforgeeks.org/page/10/']
 
for url in range(0,2):
    req = requests.get(URL[url])
    soup = BeautifulSoup(req.text, 'html.parser')
 
    titles = soup.find_all('div',attrs={'class','head'})
    # for i in range(4, 19):
    #     if url+1 > 1:
    #         print(f"{(i - 3) + url * 15}" + titles[i].text)
    #     else:
    #         print(f"{i - 3}" + titles[i].text)

# ----------csv file ------------------------

URL = 'https://www.geeksforgeeks.org/page/'
 
soup = BeautifulSoup(req.text, 'html.parser')
 
titles = soup.find_all('div', attrs={'class', 'head'})
titles_list = []
 
count = 1
for title in titles:
    d = {}
    d['Title Number'] = f'Title {count}'
    d['Title Name'] = title.text
    count += 1
    titles_list.append(d)
 
filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['Title Number','Title Name'])
    w.writeheader()
     
    w.writerows(titles_list)