"""
Indecisive Web Shopper
Author: Ohad Katz
"""
from selenium.webdriver.common.by import By
from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage


class AmazonPage(object):
    url = "https://www.amazon.com/"
