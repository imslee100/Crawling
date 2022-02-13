from bs4 import BeautifulSoup

html = """
    <html>
        <head>
            <title></title>
        </head>
        <body>
            <h1>Hello</h1>
            <h2>There<h2>
            <p class="title"><b>The Dormouse's story</b></p>
            <p class="story">Once upon a time there were three little sisters
                <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
                <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
                <a data-test="test" data-io="link3" href="http://example.com/little" class="sister" id="link3">Title</a>   
            </p>
            <p class="story">
                story ...
            </p>
        </body>
    </html>
"""

# BS4 initialize
soup = BeautifulSoup(html, 'html.parser')

# Check type
# print ('soup', type(soup))
print ('prettify', soup.prettify())

# Tag Access
h1 = soup.html.body.h1
# print('h1',h1)

p1 = soup.html.body.p
# print('p1',p1)

p2 = p1.next_sibling.next_sibling.next_sibling.next_sibling
print('p2',p2)

# print('h1 >>', h1.string)
# print('p >>', p1.string)
# print(p2.next_element)

for v in p2.next_element:
    pass
    # print(v)

soup2 = BeautifulSoup(html, 'html.parser')

link1 = soup.find_all('a', limit=2)
# print('links',link1)

link2 = soup.find_all("a", class_='sister')
# print(link2)

link3 = soup.find_all("a",class_="sister")
# for t in link2:
#     print(t)

link4 = soup.find_all("a", id='link4')
# print(link4)

link5 = soup.find_all("a", string=["Elsie"])
# print(link5)

link6 = soup.find("a")

# print(link6)
# print(link6.string)
# print(link6.text)

link7 = soup.find("a",{"class":"sister","data-io":"link3"})
# print(link7)
# print(link7.text)
# print(link7.string)

link8 = soup.select_one('p.title > b')
# print(link8)
# print(link8.text)
# print(link8.string)

link9 = soup.select_one('a#link1')
# print(link9)
# print(link9.text)
# print(link9.string)

link10 = soup.select_one("a[data-test='test']")
# print(link10)
# print(link10.text)
# print(link10.string)

link11 = soup.select('p.story > a')
# print(link11)
# for n in link11:
#     print(n.text)
#     print(n.string)

link12 = soup.select('p.story > a:nth-of-type(2)')
# print(link12)

link13 = soup.select("p.story")
print(link13)