from llm.llm_helper import llm

prompt = "Explain in one sentence what an AI agent is."

result = llm.invoke(prompt)

print(result.content)
