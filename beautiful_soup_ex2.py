import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

opener = req.build_opener()
opener.addheaders = [('User-agent', UserAgent().ie)]
req.install_opener(opener)

base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
quote = rep.quote_plus('호랑이')
url = base + quote

print('Request URL : {}'.format(url))

res = req.urlopen(url)
# print(res)

savePath = 'C:/Users/Steve/Documents/imgdown'

# try:
#     if not (os.path.isdir(savePath)):
#         os.makedirs(os.path.join(savePath))
# except OSError as e:
#     print("folder creation failed.")
#     print("folder name : {}".format(e.filename))

#     raise RuntimeError("System Exit!")
# else:
#     print("folder is created!")

soup = BeautifulSoup(res, "html.parser")
# print(soup.prettify())

# img_list = soup.select('div.tile_item > div.photo_bx > div.thumb > a > img')
# print(img_list)

# for i, img in enumerate(img_list, 1):
#     print(img, i)
#     fullFileName = os.path.join(savePath, savePath + str(i) + '.png')
#     print(fullFileName)
#     req.urlretrieve(img['data-source'], fullFileName)

img_list2 = soup.find_all("a", class_=".link_thumb")
print(img_list2)

for v in img_list2:
    img_t = v.find('img')
    fullFileName = os.path.join(savePath, savePath + str(v) + '.png')
    print(img_t.attrs['src'])
    req.urlretrieve(img_t.attrs['src'], fullFileName)

print("download suceeded")