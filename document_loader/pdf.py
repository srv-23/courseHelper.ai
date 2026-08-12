from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader("document_loader/test.pdf") 

docs = data.load()

splitter = RecursiveCharacterTextSplitter(
  chunk_size = 1000,
  chunk_overlap = 1
)

chunks = splitter.split_documents(docs)

print(chunks[0])