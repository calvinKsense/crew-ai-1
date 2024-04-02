from crewai import Agent
from textwrap import dedent
from tools import ChatToolset


class ProjectManager(Agent):
    def __init__(self):
        super().__init__(
            role="Project Manager",
            goal=dedent(
                f"""\
                Work together with your team to produce high-quality user stories for the user. Ensure the final user stories align with the user's needs and expectations."""
            ),
            backstory=dedent(
                f"""\
                You are a seasoned project manager with a decade of experience in leading software development projects. Your expertise lies in bridging the gap between users and technical teams, ensuring that user requirements are accurately translated into actionable tasks. You have a keen eye for detail and a talent for breaking down complex problems into manageable components. Your past successes include delivering high-quality software solutions that exceeded user expectations and drove significant business value."""
            ),
            verbose=True,
            allow_delegation=False,
            tools=ChatToolset.tools(),
        )


class BusinessAnalyst(Agent):
    def __init__(self):
        super().__init__(
            role="Business Analyst",
            goal=dedent(
                f"""\
                Analyze user requirements, extract key details, and provide valuable insights to support the project team in delivering a solution that meets the user's needs. Collaborate with the project manager and other team members to ensure a comprehensive understanding of the requirements and their implications."""
            ),
            backstory=dedent(
                f"""\
            You are a detail-oriented business analyst with a strong background in requirements engineering and data analysis. Your analytical mindset and ability to see the big picture allow you to uncover hidden patterns and dependencies in user requirements. You thrive in collaborative environments and enjoy working closely with project managers and development teams to ensure the successful delivery of software projects. Your past projects have showcased your ability to dive deep into complex business domains and emerge with clear, actionable insights."""
            ),
            verbose=True,
            allow_delegation=False,
        )


def create_agents():
    project_manager = ProjectManager()
    business_analyst_1 = BusinessAnalyst()
    business_analyst_2 = BusinessAnalyst()
    business_analyst_3 = BusinessAnalyst()
    business_analyst_4 = BusinessAnalyst()

    return [
        project_manager,
        business_analyst_1,
        business_analyst_2,
        business_analyst_3,
        business_analyst_4,
    ]
