from agents import Agent, Runner,function_tool,RunContextWrapper
from my_config import config
from typing_extensions import TypedDict
from typing import Any
from dataclasses import dataclass


@dataclass
class UserInfo:
    name: str
    designation: str


local_context = UserInfo(name="Aryan",designation="Student")

local_context = {
     "name": "Aryan",
     "designation": "Student"
 }

@function_tool
async def fetch_date(wrapper:RunContextWrapper, city: str) -> str:
    """
    fetch date according given city

    Args:
    city: city for date
    """

    print("wrapper>>>>",wrapper)
    user_name = wrapper.context["name"]
    return f"Hi {user_name} the date in {city} is 27-07-2025"
    return f"the date in {city} is 27-07-2025"



simple_context_agent = Agent(
    name="Context Agent",
    instructions="You are helpfull assisatnt with local context",
    tools=[fetch_date]
)


result = Runner.run_sync(
    simple_context_agent,
    "What is date in karachi?",
    run_config=config,
    context=local_context   
    )


print("result>>>>",result.final_output)