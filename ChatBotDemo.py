import streamlit as st
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

#-----------------------
# page config
#-----------------------
st.set_page_config(page_title="C++ RAG CHATBOT")
st.title("C++ RAG CHATBOT")
st.write("Ask any questions related to C++ introduction.")

#-----------------------
# Load environment variables
#-----------------------
#load_dotenv()  

#----------------------
# Load documents and create embeddings
#----------------------

@st.cache_resource 
def load_vectorstore():
    #load Document
    loader=TextLoader("Cpp.txt",encoding="utf-8")
    documents=loader.load()

    #split Text
    text_splitter=RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=20
    )
    final_documents=text_splitter.split_documents(documents)
#Embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-V2")
    
    db = FAISS.from_documents(final_documents, embeddings)
    return db

db=load_vectorstore()
query = st.text_input("Enter your question for Attention Mechanism : ")
if query:
    docx = db.similarity_search(query)
    st.subheader("retrieved Context:")
    for i, doc in enumerate(docx):
        print(docx[i].page_content)
        st.markdown(f"result {i+1}")
        st.write(doc.page_content)