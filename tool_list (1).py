from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
#from langchain_community.tools.yahoo_finance_news import YahooFinanceNewsTool
import streamlit as st


def repl(y):

    

    python_repl = PythonREPL()
    repl_tool = Tool(
        name="python_repl",
        description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
        func=python_repl.run,
    )

    y.append(repl_tool)

    return y

# def yahoo(y):
#     yahoo_1 = YahooFinanceNewsTool()
#     # yahoo_tool = Tool(
#     #     name="yahoo",
#     #     description="A tool for fetching and displaying news articles from Yahoo Finance.",
#     #     func=yahoo.run,
#     # )

#     y.append(yahoo_1)

#     return y


