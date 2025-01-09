import os

OPEN_AI_API = os.environ.get(
    "OPEN_AI_API",
    "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")
assert OPEN_AI_API is not None, "OPEN_AI_API environment variable is not set"
