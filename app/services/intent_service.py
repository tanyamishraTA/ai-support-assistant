class IntentService:

    GREETINGS = {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
        "thanks",
        "thank you",
        "bye",
        "goodbye",
        "how are you",
        "ok",
        "okay",
        "what"
    }

    @classmethod
    def is_small_talk(cls, question: str) -> bool:

        question = question.strip().lower()

        return question in cls.GREETINGS