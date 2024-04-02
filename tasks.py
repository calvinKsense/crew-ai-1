from crewai import Task
from textwrap import dedent
from tools import ChatToolset

class ProjectManagerTasks:
    @staticmethod
    def initial_requirements_gathering(user_input):

        return Task(
            description=dedent(
                f"""\
            Gather initial requirements from the user through an interactive conversation. when the user communicates their requirements to you, make a carful note of each and every requirement in the user's summary and take extra care that nothing is missed. After the user has given you all of their requirements, provide the user with a clear and complete summary and confirm with the user that the summary accurately captures their requirements. Iterate with the user until they explicitly approve your summary of their requirements."""
            ),
            expected_output=dedent(
                f"""\
            A well-written and detailed summary of the user's requirements, organized into clear sections. The summary should be easy to understand and serve as a reliable reference for the development team. Aim for a summary that captures all essential aspects of the user's requirements."""
            ),
            async_execution=False,
            tools=ChatToolset.tools(),
            context=[],
        )

    @staticmethod
    def user_approval(user_stories):
        return Task(
            description=dedent(
                f"""\
                Present the compiled list of user stories to the user for their review and approval. Present the full list of user stories to the user so they can review them. Be prepared to make any necessary revisions based on the user's feedback. If the user requests a revision, make the revision and then present the revised list of user Stories the user again. Iterate on the stories until the user is fully satisfied and grants final approval. The task is not over until the user grants final approval for the full list of user stories."""
            ),
            expected_output=dedent(
                f"""\
                A user-approved list of user stories that accurately represent the user's requirements and expectations. The output should include the revised user stories (if any changes were made based on user feedback) and a clear indication that the user has granted final approval. If multiple rounds of revisions were needed, document the changes made in each iteration. The user must provide their final positive approval on the full list of user stories. The user must have no more revisions before the task can end."""
            ),
            async_execution=False,
            tools=ChatToolset.tools(),
            context=[user_stories],
        )

class BusinessAnalystTasks:
    @staticmethod
    def extract_and_categorize_requirements(initial_user_summary):
        return Task(
            description=dedent(
                f"""\
                Thoroughly analyze the provided summary of the user's requirements. Extract all the individual requirements mentioned in the summary, ensuring that each requirement is unambiguous, clear, specific, independent, testable and user focused. Categorize the requirements based on their type (functional or non-functional). Create a markdown table with columns for the requirement statement and its category."""
            ),
            expected_output=dedent(
                f"""\
                A well-structured markdown table with the following columns:
                ---
                | Requirement | Category |
                |-------------|----------|
                | [clear, user focused requirement statement] | [functional or non-functional] |
                | [clear, user focused requirement statement] | [functional or non-functional] |
                ---
                The table should include all the requirements extracted from the summary, with each requirement placed in its own row. The finished table must contain all requirements represented in the user's original summary! Take extra care that none are missed. Ensure that the categorization is accurate and consistent."""
            ),
            async_execution=True,
            context=[initial_user_summary],
        )

    @staticmethod
    def identify_user_actions_and_goals(initial_user_summary):
        return Task(
            description=dedent(
                f"""\
                Analyze the provided summary to identify all the actions that users need to perform while interacting with the system. For each action, determine the specific user role performing the action and their goal or objective behind it. Create a markdown table with columns for the user action, user role, and user goal."""
            ),
            expected_output=dedent(
                f"""\
                    A well-organized markdown table with the following columns:
                ---
                | User Action | User Role | User Goal |
                |-------------|-----------|-----------|
                | Action 1 | User Role 1 | Goal 1 |
                | Action 2 | User Role 2 | Goal 2 |
                ---
                The table should capture all the significant user actions mentioned in the summary, along with their corresponding user roles and goals. Aim for around 10-15 user actions, covering the main interactions users will have with the system."""
            ),
            async_execution=True,
            context=[initial_user_summary],
        )

    @staticmethod
    def identify_distinct_features(initial_user_summary):
        return Task(
            description=dedent(
                f"""\
                Review the provided summary and identify all the distinct features or functionalities mentioned. Each feature should be a self-contained unit of functionality that delivers value to the users. Aim to create a list of features that collectively cover all the key aspects of the system described in the summary. Ensure that the features are clearly defined and avoid overlap between them."""
            ),
            expected_output=dedent(
                f"""\
                    A bullet point list of distinct features, where each bullet point represents a single feature. For example:
                ---
                - Feature 1: Description of feature 1
                - Feature 2: Description of feature 2
                - ...
                ---
                The list should include around 8-12 features, striking a balance between granularity and comprehensiveness. Each feature description should be concise yet informative, providing a clear understanding of what the feature entails and the value it brings to the users."""
            ),
            async_execution=True,
            context=[initial_user_summary],
        )

    @staticmethod
    def create_user_stories(initial_user_summary, result1, result2, result3):
        return Task(
            description=dedent(
                f"""\
                Analyze the markdown tables provided by the business analyst agents, which contain extracted requirements, user actions, goals, and distinct features. Synthesize this information to create a comprehensive set of user stories. Each user story should follow the format: 'As a [type of user], I want to [perform some action] so that I can [achieve some goal or benefit]'. Ensure that the user stories cover all the essential requirements and features identified in the markdown tables"""
            ),
            expected_output=dedent(
                f"""\
                A numbered list of user stories, with each story written in the specified format:
                ---
                1. As a [type of user], I want to [perform some action] so that I can [achieve some goal or benefit]
                    a. [clear, specific, and unambiguous requirement for this story]
                    b. [clear, specific, and unambiguous requirement for this story]
                    c. [clear, specific, and unambiguous requirement for this story]
                2. ...
                    a. ...
                ---
                 The list of user stories should fully capture all of the user's requirements.Ensure that the stories are concise yet descriptive, providing a clear understanding of the user's perspective and needs. Under each user story, include a bullet point list of the specific requirements associated with that story. The requirements should be unambiguous, clear, specific, independent, testable and user focused. Requirements should not be repeated in multiple user stories. All of the user's requirements should be repersented in the list of user stories. All features should be represented in the list of user stories. Each user story should center around a well defined user action."""
            ),
            async_execution=False,
            context=[
                initial_user_summary,
                result1,
                result2,
                result3,
            ],
        )
