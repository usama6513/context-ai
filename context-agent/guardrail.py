from pydantic import BaseModel
from agents import (
    Agent,
    GuardrailFunctionOutput,
    InputGuardrailTripwireTriggered,
    RunContextWrapper,
    input_guardrail,
    Runner
)
from my_config import config

@input_guardrail
async def math_guardrail(
    context: RunContextWrapper, agent: Agent, input: str 
) -> GuardrailFunctionOutput:
    print(f"guardrail is running with {input}")
    return GuardrailFunctionOutput(
        output_info="",
        tripwire_triggered=False
    )

agent = Agent(  
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail]
)

result = Runner.run_sync(agent,"Hello, can you help me solve for x with quadratic formula, breaking middle term and also completing square method: x^2 +5x +6 ?",run_config=config )
print("result>>>",result.final_output)