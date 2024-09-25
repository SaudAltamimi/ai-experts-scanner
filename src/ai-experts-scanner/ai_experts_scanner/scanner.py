from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatPerplexity
from dotenv import load_dotenv
from .search.tools import search_company_info, search_person_info
from .data.schema import CompanyData, Person

load_dotenv()

# Set up the LLM and extraction chains
llm = ChatAnthropic(model="claude-3-5-sonnet-20240620",streaming=True, temperature=0)

company_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in extracting information about key people in companies. "
               "Extract relevant information from the given text about the company and its key people. "
               "Focus on identifying names and roles of key executives and founders."),
    ("human", "Company: {company_name}\n\nInformation: {text}")
])

person_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an expert in analyzing information about key people in companies. "
               "Extract relevant {info_type} information about the person from the given text. "
               "Provide a concise summary focusing on details that would be valuable for making investment decisions."),
    ("human", "Person: {person_name}\nCompany: {company_name}\nInformation type: {info_type}\n\nInformation: {text}")
])

company_extraction_chain = company_prompt | llm.with_structured_output(CompanyData)
person_extraction_chain = person_prompt | llm

def analyze_company_key_people(company_name: str) -> CompanyData:
    '''Main function to orchestrate the process'''
    company_info = search_company_info(company_name)
    company_data = company_extraction_chain.invoke({"company_name": company_name, "text": company_info})
    
    for person in company_data.key_people:
        background_info = search_person_info(person.name, company_name, "background")
        importance_info = search_person_info(person.name, company_name, "importance to company")
        
        background = person_extraction_chain.invoke({
            "person_name": person.name,
            "company_name": company_name,
            "info_type": "background",
            "text": background_info
        })
        importance = person_extraction_chain.invoke({
            "person_name": person.name,
            "company_name": company_name,
            "info_type": "importance to company",
            "text": importance_info
        })
        
        person.background = background
        person.importance = importance
    
    return company_data