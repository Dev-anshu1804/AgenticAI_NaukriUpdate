from logger import logger


class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        """Click on a locator."""
        logger.info("Clicking element")
        locator.click()

    def fill(self, locator, text):
        """Clear and fill a textbox."""
        logger.info(f"Entering value: {text}")
        
        locator.fill(text)