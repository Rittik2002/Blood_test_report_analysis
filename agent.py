import os
from crewai import Agent
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import SerperDevTool
load_dotenv()

SERPER_API_KEY= os.getenv('SERPER_API_KEY')

# inititlaize the tool for internet searching capabilities
search_tool = SerperDevTool()

# call gemini model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', verbose=True,temperature=0.5, google_api_key=os.getenv('GOOGLE_API_KEY'))

analyst = Agent(
    role='Blood Test Analyst',
    goal='Evaluate the blood test report to deliver key insights and identify any abnormalities or trends.',
    backstory='A medical expert specializing in blood test analysis.',
    memory=True,
    verbose=True,
    llm=llm,
    allow_delegation=False
)

researcher = Agent(
    role='Article Researcher',
    goal='Conduct targeted research for relevant health articles tied to the blood test findings.',
    backstory='An expert researcher proficient in finding health-related articles.',
    tools=[search_tool],
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False,
)

advisor = Agent(
    role='Health Advisor',
    goal='Offer actionable health advice grounded in the blood test results and research findings.',
    backstory='A health advisor with extensive knowledge in providing health advice.',
    verbose=True,
    memory=True,
    llm=llm,
    allow_delegation=False,
)
