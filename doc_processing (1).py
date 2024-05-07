import streamlit as st
from io import BytesIO
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain.agents import Tool,load_tools
from langchain.chains import RetrievalQA
from langchain_core.pydantic_v1 import BaseModel, Field
import os
#masterlist = []
tools = []


def justnames(docs):
    names = []
    for d in docs:
        u = d.name.split('.')[0]
        names.append(u)
    return names    ## retrieving names and storing them in a file for future use


def process_pdf(files):

    paths = []
    
    names = justnames(files) # we send our input files of bytesIO type to this function to just retrieve their names
    for f in files:
        n = f.name.split('.')[0]
        f.seek(0)
        with open("{}.pdf".format(n), mode="wb") as doc:
            doc.write(f.read())
            paths.append(os.path.abspath("{}.pdf".format(n)))
        # #if(n not in masterlist):   
        #     f.seek(0)
        #     with open("{}.pdf".format(n), mode="wb") as doc:
        #         doc.write(f.read())
        #         paths.append(os.path.abspath("{}.pdf".format(n)))
        #     masterlist.append(n)
    # Create a collapsible sidebar
    # with st.sidebar:
    #     st.title("Library")
    
        # List of files
        # for file in masterlist:
        #         st.write(file)
    return paths, names

def vectordb(l,noun):
        
    


    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")


    for id,road in enumerate(l):  # l is the list with paths 
        loader = PyPDFLoader(road)
        pages = loader.load_and_split()
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        docs = text_splitter.split_documents(pages)
        embeddings = OpenAIEmbeddings()
        retriever = FAISS.from_documents(docs, embeddings).as_retriever()
        t = toolbox(llm, retriever, noun[id])  ## function call to the function in toolkit.py
        print(f"tool appeded{t}")
        
        
        tools.append(t)


def box():
    return tools 


        
class DocumentInput(BaseModel):
    question: str = Field()


def toolbox(model, context, n):
        
        
        print(f"\n\n{n}\n\n")
    # tools.append(
        t = Tool(
            args_schema=DocumentInput,
            name=n,
            description="searches and returns relevant excerpts when you want to answer questions about {}".format(n),
            func=RetrievalQA.from_chain_type(llm=model, retriever=context),
        )

        return t



    

