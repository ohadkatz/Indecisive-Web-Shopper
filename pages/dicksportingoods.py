"""
Indecisive Web Shopper
Author: Ohad Katz
"""
import platform
from os import getcwd, path
from .locator import Locator
from .base_element import BaseElement
from .base_page import BasePage


class DSPPage(BasePage):
    url = "https://www.dickssportinggoods.com/"
