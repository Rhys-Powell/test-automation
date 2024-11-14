from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# Create an instance of FirefoxOptions
firefox_options = Options()

# Set any desired capabilities here
# firefox_options.add_argument('--headless')  # Example of a headless argument

# Initialize WebDriver with options
driver = webdriver.Firefox(options=firefox_options)
driver.quit()