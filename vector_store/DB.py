from langchain_community.vectorstores import Chroma
from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

docs = []

from langchain_core.documents import Document

embedding_model = MistralAIEmbeddings(
    model="mistral-embed"
)

vectorstore = Chroma.from_documents(
  documents = docs,
  embedding = embedding_model,
  persist_directory = "chroma_db"
)

result = vectorstore.similarity_search("What is used for data analysis?",k = 2)

for r in result:
  print(r.page_content)
  print(r.metadata)

retriver = vectorstore.as_retriever()

docs = retriver.invoke("Explain deep learning")

for d in docs:
  print(d.page_content)