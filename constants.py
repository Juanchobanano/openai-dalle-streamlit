import os

OPEN_AI_API = os.environ.get(
    "OPEN_AI_API",
    None)
assert OPEN_AI_API is not None, "OPEN_AI_API environment variable is not set"
