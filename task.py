from agent import analyst,researcher,advisor
from crewai import Task

def create_tasks(raw_text):
    analyze_blood_test_task = Task(
        description=f'You have to analyze the blood test report from the following text: "{raw_text}"',
        expected_output='A summary of the blood test results.',
        agent=analyst,
        async_execution=False,
    )

    find_articles_task = Task(
        description='Search for health articles based on the blood test analysis.',
        expected_output='A list of relevant health articles with links.',
        agent=researcher,
        context=[analyze_blood_test_task],  # Uses the analysis as input context
        async_execution=False,
    )

    provide_recommendations_task = Task(
        description='Provide health recommendations based on the articles found.',
        expected_output='Health recommendations with links to the articles.',
        agent=advisor,
        context=[find_articles_task], # Uses articles as input context
        async_execution=False,
    )
    
    return [analyze_blood_test_task, find_articles_task, provide_recommendations_task]