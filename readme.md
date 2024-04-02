# CrewAI Project: Requirements Gathering and User Story Creation

This project demonstrates the usage of the CrewAI framework to automate the process of requirements gathering and user story creation for a software development project. It showcases the collaboration between AI agents in a crew to efficiently capture user requirements, analyze them, and generate user stories.

## Project Overview

The project consists of three main components:

1. **Agents**: The AI agents involved in the requirements gathering and user story creation process. There are two types of agents:
   - Project Manager: Responsible for overseeing the entire process, gathering initial requirements from the user, creating user stories, and seeking user approval.
   - Business Analyst: Responsible for analyzing the user requirements, extracting key details, and providing insights to support the project team.

2. **Tasks**: The specific tasks assigned to the agents. Each task has a clear description, expected output, and associated agent. The tasks include:
   - Initial Requirements Gathering
   - Extract and Categorize Requirements
   - Identify User Actions and Goals
   - Identify Distinct Features
   - Create User Stories
   - User Approval

3. **Crew**: The collaborative group of agents working together to achieve the set of tasks. The crew is configured with a hierarchical process flow, where the Project Manager agent coordinates the crew and delegates tasks to the Business Analyst agents.

## Getting Started

To run the CrewAI project, follow these steps:

1. Install the required dependencies:
```
pip install crewai
```
2. Clone the project repository:
```
git clone https://github.com/your-username/crewai-project.git
```
3. Navigate to the project directory:
```
cd crewai-project
```
4. Run the `main.py` script:
```
python main.py
```
5. Observe the crew execution process, including the interactions between agents, task outputs, and the final user stories.

## Project Structure

The project has the following structure:
```
crewai-project/
│
├── agents.py
├── tasks.py
├── main.py
└── README.md
```
- `agents.py`: Contains the definition of the AI agents (Project Manager and Business Analyst) and their attributes.
- `tasks.py`: Defines the tasks assigned to the agents, including their descriptions, expected outputs, and associated agents.
- `main.py`: The main script that brings together the agents, tasks, and crew configuration to initiate the execution process.
- `README.md`: This file, providing an overview of the project and instructions for running it.

## Customization

You can customize the project according to your specific requirements:

- Modify the agent roles, goals, and backstories in `agents.py` to align with your project's needs.
- Adjust the task descriptions, expected outputs, and associated agents in `tasks.py` to match your project's requirements gathering and user story creation process.
- Configure the crew settings in `main.py`, such as the process flow, LLM, and verbosity, to suit your preferences.

## Acknowledgements

This project utilizes the CrewAI framework, which provides a powerful and flexible way to create collaborative AI systems. We would like to thank the CrewAI team for their excellent work and support.

If you have any questions or need further assistance, please don't hesitate to reach out.

Happy requirements gathering and user story creation with CrewAI!