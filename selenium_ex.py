from selenium import webdriver

# web browser setting
browser = webdriver.Chrome('./webdriver/chromedriver.exe')

# waiting time
browser.implicitly_wait(5)

# window size
browser.set_window_size(1920,1200)

# page move
browser.get('http://daum.net')

# Page Content
# print("Page Content: {}".format(browser.page_source))

# Session ID
print("Session ID: {}".format(browser.session_id))

# Title
print("Title: {}".format(browser.title))

#Current URL
print("URL: {}".format(browser.current_url))

# Cookie
print("Cookie: {}".format(browser.get_cookie))

element = browser.find_element_by_css_selector('div.inner_search > input.tf_keyword')

element.send_keys('방탄소년단')
element.submit()

browser.save_screenshot('C:/Users/Steve/Documents/sc1.png')

browser.get_screenshot_as_file('C:/Users/Steve/Documents/sc2.png')

browser.quit()