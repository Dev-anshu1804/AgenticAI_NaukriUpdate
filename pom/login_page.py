import os
from dotenv import load_dotenv
from logger import logger
from pom.base_page import BasePage

load_dotenv()

EMAIL = os.getenv("NAUKRI_EMAIL")
PASSWORD = os.getenv("NAUKRI_PASSWORD")


class LoginPage(BasePage):

    URL = "https://www.naukri.com/"

    def login(self):
        logger.info("Opening Naukri")

        self.page.goto(self.URL)

        logger.info("Clicking Login")
        self.click(self.page.get_by_role("link", name="Login", exact=True))

        logger.info("Entering credentials")
        self.fill(self.page.get_by_role("textbox", name="Enter your active Email ID /"), EMAIL)
        self.fill(self.page.get_by_role("textbox", name="Enter your password"), PASSWORD)

        self.click(self.page.get_by_role("button", name="Login", exact=True))

        logger.info("Login successful")