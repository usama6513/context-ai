from agents import Agent, Runner , function_tool
from my_config import config
from typing_extensions import TypedDict

class MyDataType(TypedDict):
    num1 : str
    num2 : str
    num3 :  str

@function_tool
async def fetch_weather(city : str) -> str:
    """
    fetch weather according given city

    Args:
    city: city for weather
    """
    return f"the weather in {city} is sunny with 45c"


simpe_agent = Agent(
    name="Assistant",
    instructions="You are helpfull assistant",
    #tools=[fetch_weather],
    output_type= MyDataType
    
)


result = Runner.run_sync(
    starting_agent=simpe_agent,
    input="dear can you tell me the factorial three multiply factorial five is what",
    run_config=config,
    

    )

print("Result>>>>", result.final_output)
print("Result Type>>>",type(result.final_output))