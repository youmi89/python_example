from pyhub.llm import UpstageLLM

api_key = ""
llm = UpstageLLM(api_key="")
reply = llm.ask("hello")
print(reply)
