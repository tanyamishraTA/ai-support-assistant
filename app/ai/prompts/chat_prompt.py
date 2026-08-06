from langchain_core.prompts import ChatPromptTemplate

from app.ai.prompts.system_prompt import SYSTEM_PROMPT


chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            SYSTEM_PROMPT,
        ),
        (
            "human",
            "{question}",
        ),
    ]
)