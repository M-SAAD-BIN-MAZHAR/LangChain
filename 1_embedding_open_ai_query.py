from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
embedding=OpenAIEmbeddings(model='text_embedding-3-large',dimensions=32)
result=embedding.embed_query('Saad')
print(str(result))
