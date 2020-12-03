"""
Indecisive Web Shopper

Base Page
Author: Ohad Katz
"""
import platform
from os import getcwd, path


class BasePage(object):

    url = None

    def __init__(self, driver):
        self.driver_version = driver

    def go(self):
        self.driver.get(url)

