# enums.py
from enum import Enum

class MediaCategory(Enum):
    VIDEO = "video"
    AUDIO = "audio"
    TRANSCRIPT = "transcript"
    # Add more categories as needed

# Usage
media_type = MediaCategory.VIDEO
