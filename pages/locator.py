"""
Author: Ohad Katz

"""
# This namedtuple allows us to generate object locators for
# Selenium which are made up of a By (Path like XSS/CSS_Selector/etc.)
from collections import namedtuple

Locator = namedtuple("Locator", ["by", "value"])

