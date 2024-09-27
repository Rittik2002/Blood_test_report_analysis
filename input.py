import os
import PyPDF2
from crewai import Crew, Process
from agent import analyst, researcher, advisor
from task import create_tasks

# Function to extract the text from the first two pages of a PDF
def extract_pdf_text(pdf_file):
    with open(pdf_file, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        content = ""
        # Loop over the first two pages or less if unavailable
        for page_num in range(min(2, len(reader.pages))):
            content += reader.pages[page_num].extract_text()
    return content

# Function to prompt the user for the blood test PDF file
def prompt_for_pdf_report():
    pdf_file = input("Please provide the path to your PDF report: ")
    if not os.path.isfile(pdf_file):
        raise FileNotFoundError(f"File not found: {pdf_file}")
    return pdf_file

# Obtain the path to the PDF report
pdf_report = prompt_for_pdf_report()

# Extract the text from the PDF report's first two pages
extracted_text = extract_pdf_text(pdf_report)

# Create tasks based on the extracted text
assigned_tasks = create_tasks(extracted_text)

# Initialize the crew with the required agents and process configuration
crew_setup = Crew(
    agents=[analyst, researcher, advisor],
    tasks=assigned_tasks,
    process=Process.sequential
)

# Begin the task execution process using the extracted blood test data
execution_result = crew_setup.kickoff(inputs={'blood_test_data': extracted_text})
print(execution_result)
