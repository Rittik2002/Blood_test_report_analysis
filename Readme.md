# Blood Test Analysis System
This system analyzes a blood test report, searches the internet for related articles, and provides personalized health recommendations. It leverages generative AI models and search tools to deliver comprehensive and relevant results.

## Project Overview
The system performs the following tasks:

 - Analyze a blood test report: Extracts  relevant insights from the report.
 - Search the internet for health articles: Finds articles based on the analysis.
 - Provide health recommendations: Uses the articles to give actionable advice.

## How I Approached the Task

- Breaking Down the Process:

    - First, I divided the system into three core functionalities: analyzing the report, finding articles, and providing recommendations.
    - I designed each functionality to be handled by a dedicated agent (Blood Test Analyst, Article Researcher, Health Advisor), ensuring clear separation of responsibilities.
- Agent-Based Design:

    - I utilized CrewAI's agent-based system, assigning each agent a specific role:
        - The Blood Test Analyst focuses on analyzing the report and providing key insights.
        - The Article Researcher uses the analysis to search the internet for relevant health articles.
        - The Health Advisor processes both the analysis and the articles to deliver recommendations.
    - Each agent is configured with memory to keep track of the context and ensure smooth execution.
- Task Sequencing:

    - The tasks are executed sequentially to ensure that each agent can use the output of the previous task.
    - For example, the researcher uses the analyst’s findings to conduct targeted research, and the advisor uses the research findings to generate recommendations.
- Integration of PDF Text Extraction:

    - Since blood test reports are often provided as PDFs, I integrated PyPDF2 to extract text from the first two pages of the report.

## Steps to Run the Code

- Step 1: Clone the Repository
```
    git clone <https://github.com/Rittik2002/Blood_test_report_analysis_crewAI>
    cd <repository-folder>
```

- Step 2: Install Dependencies
```
    pip install -r requirements.txt
```

- Step 3: Set Up API Keys
Create a .env file in the project root and add your API keys:
```
    GOOGLE_API_KEY=<your-google-api-key>
    SERPER_API_KEY=<your-serper-api-key>
```

- Step 4: Run the Script
```
    python input.py
```

- Step 5: Upload a Blood Test Report
When prompted, provide the path to a PDF report (up to two pages will be extracted and processed).

- Step 6: Review the Results
The system will analyze the blood test, find relevant health articles, and provide personalized health recommendations.

## How It Works

- PDF Extraction: Prompts the user to upload a blood test report in PDF format. The text is extracted from the first two pages using PyPDF2.

- Task Creation: Three agents handle:

    - Blood Test Analyst: Evaluates the report for insights.
    - Article Researcher: Searches the web for relevant health articles.
    - Health Advisor: Recommends health advice based on the articles.
- Sequential Task Execution:

    - The analyst processes the blood test report.
    - The researcher searches for articles based on the analyst's findings.
    - The advisor uses the articles to generate health recommendations.
