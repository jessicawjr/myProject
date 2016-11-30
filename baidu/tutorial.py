from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



TIMEOUT = 30


class Baidu(object):
    def __init__(self, driver):
        self.driver = driver

    def open_baidu(self):
        self.driver.get("http://www.baidu.com")

    def open_news_baidu(self):
        self.driver.get("http://news.baidu.com")

    def go_to_login(self):
        self.driver.find_element_by_link_text("登录").click()

    def close_login(self):
        wait = WebDriverWait(self.driver, TIMEOUT)
        elem = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.close-btn")))
        elem.click()

    def get_current_url(self):
        return self.driver.current_url

# if __name__=="__main__":
#     bd = Baidu(webdriver.Firefox())
#     bd.open_baidu()
#     print(bd.get_current_url())
#     bd.open_news_baidu()
#     print(bd.get_current_url())
#     bd.go_to_login()
#     print(1)
#     bd.close_login()
#     print(2)
