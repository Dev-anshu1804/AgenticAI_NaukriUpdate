import os

from dotenv import load_dotenv
from autogen import (
    AssistantAgent,
    UserProxyAgent,
    register_function
)

from scripts.profile_automation import ProfileAutomation

load_dotenv()

llm_config = {
    "model": "gpt-4o-mini",
    "api_key": os.getenv("OPENAI_API_KEY")
}

# -----------------------------------------------------
# Playwright Automation
# -----------------------------------------------------

automation = ProfileAutomation()


# -----------------------------------------------------
# Tool Functions
# -----------------------------------------------------

def update_profile_name(name: str) -> str:
    """Update the Naukri profile name."""

    automation.run({
        "action": "update_profile_name",
        "value": name
    })

    return f"Profile name updated to '{name}'"


def validate_profile_name(expected_name: str) -> str:
    """Validate the Naukri profile name."""

    result = automation.run({
        "action": "validate_profile_name",
        "value": expected_name
    })

    if result:
        return "Validation Passed"

    return "Validation Failed"


# -----------------------------------------------------
# Planner
# -----------------------------------------------------

planner = AssistantAgent(
    name="Planner",
    llm_config=llm_config,
    system_message="""
You are the Planner.

Create a plan for updating and validating the
Naukri profile.

Do not execute any tool.
"""
)


# -----------------------------------------------------
# Executor
# -----------------------------------------------------

executor = AssistantAgent(
    name="Executor",
    llm_config=llm_config,
    system_message="""
You are the Executor.

Whenever the Planner asks to update the profile,
call the update_profile_name tool.

Do not explain.

Use the tool.
"""
)


# -----------------------------------------------------
# Tool Executor
# -----------------------------------------------------

tool_executor = UserProxyAgent(
    name="ToolExecutor",
    human_input_mode="NEVER",
    code_execution_config=False,
)


# -----------------------------------------------------
# Validator
# -----------------------------------------------------

validator = AssistantAgent(
    name="Validator",
    llm_config=llm_config,
    system_message="""
You are the Validator.

Whenever validation is requested,
call the validate_profile_name tool.

Do not explain.

Use the tool.
"""
)


# -----------------------------------------------------
# Register Tools
# -----------------------------------------------------

register_function(
    update_profile_name,
    caller=executor,
    executor=tool_executor,
    name="update_profile_name",
    description="Update the user's Naukri profile name."
)

register_function(
    validate_profile_name,
    caller=validator,
    executor=tool_executor,
    name="validate_profile_name",
    description="Validate the user's Naukri profile name."
)