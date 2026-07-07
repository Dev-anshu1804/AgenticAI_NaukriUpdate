from logger import logger
from pom.base_page import BasePage


class ProfilePage(BasePage):

    def open_profile(self):
        """Open the user's profile page."""

        logger.info("Opening profile page...")

        self.click(
            self.page.get_by_role(
                "link",
                name="View profile"
            )
        )

    def update_profile_name(self, name):
        """Update the profile name."""

        logger.info(f"Updating profile name to '{name}'")

        # Click Edit icon
        self.click(
            self.page.locator("em.edit")
        )

        # Name textbox
        name_textbox = self.page.get_by_role(
            "textbox",
            name="Enter Your Name"
        )

        self.fill(name_textbox, name)

        # Save button
        self.click(
            self.page.get_by_role(
                "button",
                name="Save"
            )
        )

        logger.info("Profile name updated successfully.")

    def get_profile_name(self):
        """Read the current profile name."""

        logger.info("Reading profile name...")

        # Open edit popup again
        self.click(
            self.page.locator("em.edit")
        )

        name = self.page.get_by_role(
            "textbox",
            name="Enter Your Name"
        ).input_value()

        logger.info(f"Current profile name: {name}")

        return name