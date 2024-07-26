from selenium_driverless import webdriver
from selenium_driverless.types.by import By
import asyncio

# Proxy Settings
proxy = "http://<User Name>:<Password>.<Host Name>:<Port>"


# This code will start a new instance each time a request is sent to the website; if you run it in a single tab without
# closing the instance, the scraping speed will be influenced; you may test it yourself.
# You can test this code on other Kasada Based antibot websites as well,this solution is properly in bypassing Kasada antibot.

async def main():
    # Read postal codes from CSV
    links = ['https://www.realestate.com.au/']
    count = 1  # Initialize the count for requests
    for link in links:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless=new')  # Use headless mode
        options.add_argument('--disable-gpu')  # Disable GPU acceleration
        # Start a new browser instance for each request
        async with (webdriver.Chrome(
                options=options) as driver):  # This should be called within the main loop otherwise,
            # the error "FileNotFoundError: [WinError 206] The filename or extension is too long" will occur.
            await driver.set_single_proxy(proxy)  # set the proxy
            # You can use your logic and the inner loop to scrape whatever you want.
            # START YOUR CODE:

            await driver.quit()  # this will close the chrome instance when the page will be scraped.


if __name__ == '__main__':
    asyncio.run(main())
