from enum import Enum
from chatbot.memory import MongoChatbotMemory, BaseChatbotMemory, CustomMongoChatbotMemory


class MemoryType(str, Enum):
    """Enumerator with the Memory types."""
    BASE_MEMORY = "base-memory"
    MONGO_MEMORY = "mongodb-memory"
    CUSTOM_MEMORY = "custom-memory"


MEM_TO_CLASS = {
    "mongodb-memory": MongoChatbotMemory,
    "base-memory": BaseChatbotMemory,
    "custom-memory": CustomMongoChatbotMemory
}