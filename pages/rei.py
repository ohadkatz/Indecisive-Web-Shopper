"""
Indecisive Web Shopper
Author: Ohad Katz
"""
import platform
from os import getcwd, path
from selenium.webdriver.common.by import By
from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage


class REIPage(object):
    def __init__(self):
        self.driver_version = self.getDriver()
        self.url = "https://www.rei.com/"
