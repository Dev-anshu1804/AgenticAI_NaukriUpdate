from playwright.sync_api import sync_playwright

from logger import logger
from pom.login_page import LoginPage
from pom.profile_page import ProfilePage


class ProfileAutomation:

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.login_page = None
        self.profile_page = None

    def start(self):
        logger.info("Launching browser...")

        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()

        self.login_page = LoginPage(self.page)
        self.profile_page = ProfilePage(self.page)

    def login(self):
        self.login_page.login()

    def run(self, task):

        action = task["action"]
        value = task["value"]

        if action == "update_profile_name":

            self.profile_page.open_profile()
            self.profile_page.update_profile_name(value)

        elif action == "validate_profile_name":

            actual = self.profile_page.get_profile_name()

            if actual == value:
                logger.info("✅ Validation Passed")
                return True

            logger.error("❌ Validation Failed")
            
            return False

    def close(self):

        logger.info("Closing browser")

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()