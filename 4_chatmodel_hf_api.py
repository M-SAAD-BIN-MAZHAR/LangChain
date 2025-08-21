from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
load_dotenv()
llm=HuggingFaceEndpoint(
    repo_id='mistralai/Mistral-7B-Instruct-v0.3',
    task='text-generation'
)
model=ChatHuggingFace(llm=llm)
result=model.invoke('what is the capital of pakistan')
print(result.content)