from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from langchain.messages import HumanMessage,SystemMessage,AIMessage
llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=1000,
    temperature=0.7,
    huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN")
)
model=ChatHuggingFace(llm=llm)  
print("Please select the mode your bot want to be:")
print("1. Funny assistant")
print("2. Professional assistant")
print("3. Sarcastic assistant")
print("4. Friendly assistant")
print("5. Helpful assistant")
print("6. Expert assistant")
print("7. Wise assistant")
print("8. Creative assistant")
print("9. Funny assistant")
mode=input("Enter your mode: ")
if mode=="1":
    messages=[SystemMessage(content="You are a funny assistant")]
 elif mode=="2":
    messages=[SystemMessage(content="You are a professional assistant")]
 elif mode=="3":
    messages=[SystemMessage(content="You are a sarcastic assistant")]
 elif mode=="4":
    messages=[SystemMessage(content="You are a friendly assistant")]
 elif mode=="5":
    messages=[SystemMessage(content="You are a helpful assistant")]
 elif mode=="6":
    messages=[SystemMessage(content="You are an expert assistant")]
 elif mode=="7":
    messages=[SystemMessage(content="You are a wise assistant")]
 elif mode=="8":
    messages=[SystemMessage(content="You are a creative assistant")]
 elif mode=="9":
    messages=[SystemMessage(content="You are a funny assistant")]
while True:
    prompt=input(f"You: ")
    messages.append(HumanMessage(content=prompt))
    if prompt=="exit":
        break
    resp=model.invoke(messages)
    messages.append(AIMessage(content=resp.content))
    print("Bot: ",resp.content)
