"""
Indecisive Web Shopper
Base Element Page
Author: Ohad Katz
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


class BaseElement(object):
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator
        self.web_element = None

    def find(self):
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located(self.locator)
        )
        self.web_element = element
        return None

    def click(self):
        self.web_element.click()
