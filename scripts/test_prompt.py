from app.ai.prompts.chat_prompt import chat_prompt

messages = chat_prompt.invoke(
    {
        "context": """
Employees receive 20 paid leaves annually.
""",
        "question": "How many paid leaves do employees get?",
    }
)

for message in messages.messages:
    print(message)