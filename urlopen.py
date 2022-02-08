from urllib import response
import urllib.request as req
from urllib.error import URLError, HTTPError

path_list = ["C:/Users/Steve/Documents/test1.jpg", "C:/Users/Steve/Documents/index.html"]

target_url = ["https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAyMTBfMjk0%2FMDAxNjEyOTExMjE3MDAw.mRBT1TknRdVJ1vvvNcFJ2yvG_iWCNsTcmNn3sovXAucg.Qgxsxr6_ncye6hnvV1hfRMW8FemyTZAHnYdtF9coVqQg.JPEG.erasw0715%2FNate%25A3%25DF20210207%25A3%25DF010331.jpg&type=sc960_832","https://google.com"]


for i, url in enumerate(target_url):
    try:
        response = req.urlopen(url)
        contents = response.read()
        print("--------------")
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code: {}'.format(response.getcode()))

        with open(path_list[i],'wb') as c:
            c.write(contents)
    except HTTPError as e:
        print("Download Failed.")
        print("HTTPError Code : ", e.code)
    except URLError as e:
        print("Download Failed.")
        print("URL Error Reason : ", e.reason)
    
    else:
        print()
        print("Download Succeed.")