from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import xlsxwriter
from io import BytesIO
import urllib.request as req

chrome_options = Options()
chrome_options.add_argument("--headless")


workbook = xlsxwriter.Workbook("C:/Users/Steve/Documents/crawling_result.xlsx")
worksheet = workbook.add_worksheet()

# Headless Mode
# browser = webdriver.Chrome('./webdriver/chromedriver.exe',options=chrome_options)

# Normal Mode
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

# Waiting Time
browser.implicitly_wait(5)

# Browser Size
browser.set_window_size(1920,1280)

# Go danawa notebook page
browser.get('http://prod.danawa.com/list/?cate=112758&15main_11_02')

# Wating Time
WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# Implicitly Wait
# time.sleep(5)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()

# Click Apple category checkbox
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH,'//*[@id="searchMaker1452"]'))).click()

# print('After Page Contents: {}'.format(browser.page_source))

time.sleep(3)

# Current Page
cur_page = 1

# Set num of page to crawl
target_crawl_num = 5

# Excel row count
ins_cnt = 1

while cur_page <= target_crawl_num:

    # Initialize bs4
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # print(soup.prettify())

    pro_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')

    print('','******')

    # Get List
    for v in pro_list:
        # print(v)

        # Skip AD section
        if not v.find('div', class_='ad_header'):
            # Tag Information
            # print('Name : {}, Img : {}, Price : {}'.format(v.select('p.prod_name > a'), v.select('a.thumb_link > img'), v.select('p.price_sect > a')))

            # product name, image, price
            # print(v.select('p.prod_name > a')[0].text.strip())
            # if v.select('a.thumb_link > img')[0]['src'] != '//img.danawa.com/new/noData/img/noImg_160.gif':
            #     print(v.select('a.thumb_link > img')[0]['src'])
            # else :
            #     print(v.select('a.thumb_link > img')[0]['data-original'])

            # print(v.select('p.price_sect > a')[0].text.strip())

            prod_name = v.select('p.prod_name > a')[0].text.strip()
            prod_price = v.select('p.price_sect > a')[0].text.strip()

            # if v.select('a.thumb_link > img')[0]['src'] != '//img.danawa.com/new/noData/img/noImg_160.gif':
            #    img_data = BytesIO(req.urlopen('http:'+v.select('a.thumb_link > img')[0]['src']).read())
            # else :
            #    img_data = BytesIO(req.urlopen('http:'+v.select('a.thumb_link > img')[0]['data-original']).read())

            worksheet.write('A%s'% ins_cnt, prod_name)
            worksheet.write('B%s'% ins_cnt, prod_price)
            # worksheet.insert_image('C%s'% ins_cnt, prod_name, {'image_data': img_data})

            ins_cnt += 1

        # print()

    # browser.save_screenshot('C:/Users/Steve/Documents/target_page{}.png'.format(cur_page))

    cur_page += 1

    if cur_page > target_crawl_num:
        print('Crawling Succeed.')
        break

    WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    del soup

    time.sleep(3)

# Quit Browser
browser.quit()

# Close Excel File
workbook.close()