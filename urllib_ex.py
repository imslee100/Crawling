import urllib.request as req

img_url = 'https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMjAxMTVfMjkw%2FMDAxNjQyMjM5MDcwMDM3.uacYC6kUCTfmK59vMQ3wfy9_4ISjBQPLgjjh40jVfoAg.N8GJkliORdChDSFq_d53TD9vSi6Q9yv8UiJeWTt5IX4g.JPEG.hjjaajj%2FKakaoTalk_20220114_205610981_02.jpg&type=sc960_832'
html_url = 'http://google.com'

save_path1 = 'C:/Users/Steve/Documents/test1.jpg'
save_path2 = 'C:/Users\Steve/Documents/index.html'

try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download Failed')
    print(e)
else:
    print(header1)
    print(header2)

    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    print('Download Succeed')