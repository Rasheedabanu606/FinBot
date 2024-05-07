import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit_scrollable_textbox as stx


from doc_processing import process_pdf,vectordb,box,justnames
from tool_list import repl
from agent import agent_init

#masterlist=[]
temp=[]



load_dotenv()

def main():
    # app config
    st.set_page_config(page_title="Fin bot", page_icon="🤖")
    st.title("Fin bot")

    files = st.file_uploader(label="Upload your pdfs here", accept_multiple_files=True,type="pdf")

    # if "pdf_text" not in st.session_state:
    #             # Parse PDF and extract text
    #             st.session_state.pdf_text = parse_pdf(uploaded_file)


    if(files != None):
        paths,names=process_pdf(files)
        vectordb(paths,names)
        y = box() 
        tools = repl(y)
        agent=agent_init(tools)
        agend = getmemyagent()
    #tools_updated=yahoo(tools)


    #query = st.text_input(label="Enter query here")





    #answer = agent_init(tools, query)
    #st.info("{}".format(answer['output']))




    # session state
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = [
            AIMessage(content="Hello, I am  Finbot. How can I help you?"),
        ]







        
    # conversation
    for message in st.session_state.chat_history:
        if isinstance(message, AIMessage):
            with st.chat_message("AI"):
                # message.content.replace("$", "\$")
                # st.markdown(message.content)
                m = message.content
                #st.text(m)
                stx.scrollableTextbox(m)
                #st.latex(st.markdown(''':black[m]'''))
                
        elif isinstance(message, HumanMessage):
            with st.chat_message("Human"):
                st.write(message.content)

    # user input
    #questions = ask_questions(st.session_state.pdf_text)
    user_query = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        st.session_state.chat_history.append(HumanMessage(content=user_query))

        with st.chat_message("Human"):
            st.markdown(user_query)

        with st.chat_message("AI"):
            #response = st.write_stream(get_response(user_query))
            #response=st.info("{}".format(get_response(user_query)['output']))
            #st.info("{}".format(agent.run(user_query)['output']))
            response=agent.run(user_query)
            #c=st.empty()
            #latex_expression = response
            # response.replace("$", "\$")
            # st.markdown(response)
            #r = response
            #st.latex(st.markdown(''':black[r]'''))
            #st.latex(st.markdown(fr':black[{r}]'))
            #with st.container():
            stx.scrollableTextbox(response)
            #st.text(response)
            #response=st.write(agent.run(user_query))
            #st.text(get_response(user_query, st.session_state.chat_history))
            #response =get_response(user_query, st.session_state.chat_history)
            #gen_to_str = ' '.join(str(item) for item in response)
            #st.text(type(gen_to_str))
            #response=get_response(user_query, st.session_state.chat_history)
        
        st.session_state.chat_history.append(AIMessage(content=response))

##############################################
# if query is not None and query != "":
#             with st.spinner(text="In progress..."):
#                 answer = agent_init(tools, query)
#                 st.info("{}".format(answer['output']))
#                 #st.write(agent.run(user_question))

if __name__ == "__main__":
    main()