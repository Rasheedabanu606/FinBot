from langchain.globals import set_debug,set_verbose
from langchain.agents import AgentType, initialize_agent
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import streamlit as st







def agent_init(reper):

    

    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")
    
    agent = initialize_agent(
        agent=AgentType.OPENAI_MULTI_FUNCTIONS,
        tools=reper,
        llm=llm,
        verbose=True,
)
    #set_debug(True)
    #set_verbose(True)
    #query = st.text_input(label="Enter query here")
    #return (agent({"input":query}))
    return agent
    #agent({"input": "what is cost of revenue?"})