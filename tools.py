from langchain.agents import tool


class ChatToolset:
    @tool
    def send_message(message: str):
        """Simulates sending a message to the user and waits for a response."""
        print(f"Agent says: {message}")
        user_response = input("User: ")
        return user_response

    @tool
    def follow_up(question: str):
        """Simulates a follow-up question to the user."""
        print(f"Agent asks: {question}")
        user_response = input("User: ")
        return user_response

    def tools():
        return [ChatToolset.send_message, ChatToolset.follow_up]
