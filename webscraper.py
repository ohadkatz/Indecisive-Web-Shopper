from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.amazon import AmazonPage
from pages.dicksportingoods import DSPPage
from pages.rei import REIPage

# Testing
chromeOptions = webdriver.ChromeOptions()
# This capability will help to not load Chrome Automation
chromeOptions.add_experimental_option("useAutomationExtension", False)
# Start screen at full resolution of display to avoid issues with elements
chromeOptions.add_argument("--start-maximized")
# To set all options set above, create a capabilities
capabilities = chromeOptions.to_capabilities()

browser = webdriver.Chrome(
    ChromeDriverManager().install(),
    options=chromeOptions,
    desired_capabilities=capabilities,
)


# Amazon First
amazon = AmazonPage(driver=browser)
amazon.go()


# REI Second
rei = REIPage(driver=browser)
rei.go()


# Dicks Last
dsp = DSPPage(driver=browser)
dsp.go()
