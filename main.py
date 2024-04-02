from crewai import Crew, Process
from tasks import ProjectManagerTasks, BusinessAnalystTasks
from agents import create_agents
from dotenv import load_dotenv


def main():
    load_dotenv()
    # Create the agents
    (
        project_manager,
        business_analyst_1,
        business_analyst_2,
        business_analyst_3,
        business_analyst_4,
    ) = create_agents()

    # Define the tasks
    user_summary = ProjectManagerTasks.initial_requirements_gathering(user_input="")
    extract_requirements_task = BusinessAnalystTasks.extract_and_categorize_requirements(
        user_summary
    )
    identify_actions_goals_task = BusinessAnalystTasks.identify_user_actions_and_goals(
        user_summary
    )
    identify_features_task = BusinessAnalystTasks.identify_distinct_features(
        user_summary
    )
    user_stories = BusinessAnalystTasks.create_user_stories(
        user_summary, extract_requirements_task, identify_actions_goals_task, identify_features_task
    )
    user_approval_task = ProjectManagerTasks.user_approval(user_stories)

    # Assign tasks to agents
    user_summary.agent = project_manager
    extract_requirements_task.agent = business_analyst_1
    identify_actions_goals_task.agent = business_analyst_2
    identify_features_task.agent = business_analyst_3
    user_stories.agent = business_analyst_4
    user_approval_task.agent = project_manager

    # Create the crew
    crew = Crew(
        agents=[project_manager, business_analyst_1, business_analyst_2, business_analyst_3],
        tasks=[
            user_summary,
            extract_requirements_task,
            identify_actions_goals_task,
            identify_features_task,
            user_stories,
            user_approval_task,
        ],
        process=Process.sequential,
        full_output=True,
        verbose=True,
    )

    # Kick off the crew
    result = crew.kickoff()

    # Print the result
    print("Crew Execution Result:")
    print(result)

    # Print the usage metrics
    print("Crew Usage Metrics:")
    print(crew.usage_metrics)


if __name__ == "__main__":
    main()
