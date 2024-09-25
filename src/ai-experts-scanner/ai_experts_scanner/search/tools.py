from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatPerplexity
from dotenv import load_dotenv

load_dotenv()


# Set up Perplexity search
perplexity_chat =  ChatPerplexity(temperature=0, model="llama-3.1-sonar-small-128k-online")


def search_company_info(company_name: str) -> str:
    '''function to search for company'''
    query = "key executives and founders of {company_name}"
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in extracting information about key people in companies. "
               "Extract relevant information about the company and its key people. "
               "Focus on identifying names and roles of key executives and founders."),
    ("human", query)
    ])
    search_chain = prompt | perplexity_chat

    response = search_chain.invoke({"company_name": company_name})
    return response.content

def search_person_info(person_name: str, company_name: str, info_type: str) -> str:
    query = "{person_name} {company_name} {info_type}"
    prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in extracting information about key people in successful AI companies. "
               "Extract relevant information about that Person"),
    ("human", query)
    ])
    search_chain = prompt | perplexity_chat

    response = search_chain.invoke({
        "person_name": person_name,
        "company_name": company_name,
        "info_type": info_type, 
    })
    return response.content