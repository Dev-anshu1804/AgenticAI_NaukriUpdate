import os

from dotenv import load_dotenv
from autogen import GroupChat, GroupChatManager

from agent import (
    planner,
    executor,
    validator,
    tool_executor,
    automation
)

load_dotenv()

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY")
}


def main():

    # Launch browser
    automation.start()

    # Login once
    automation.login()

    # Create Group Chat
    groupchat = GroupChat(
        agents=[
            planner,
            executor,
            tool_executor,
            validator
        ],
        messages=[],
        max_round=8
    )

    manager = GroupChatManager(
        groupchat=groupchat,
        llm_config=llm_config
    )

    # Start conversation
    planner.initiate_chat(
        manager,
        message="""
Update the Naukri profile name to 'Anshu Singh.'.

Then validate the profile name.

Finally report the result.
"""
    )

    # Close browser
    automation.close()


if __name__ == "__main__":
    main()