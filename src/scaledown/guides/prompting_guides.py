"""
Model-specific prompting guides for optimizing prompts.
"""

# Meta/Llama Prompting Guide
LLAMA_GUIDE = {
    "name": "Llama",
    "source": "Meta AI",
    "url": "https://www.llama.com/docs/how-to-guides/prompting/",
    "tips": [
        {
            "title": "Be Clear and Concise",
            "description": "Use clear, concise language in your prompts. Avoid jargon and technical terms that might confuse the model.",
            "example": {
                "before": "Could you please kindly help me create a detailed analysis of the quarterly financial report that includes all of the important metrics and insights for the executive team, if you don't mind?",
                "after": "Analyze quarterly financial report. Include key metrics and insights for executives."
            }
        },
        {
            "title": "Use Explicit Instructions",
            "description": "Detailed, explicit instructions produce better results than open-ended prompts.",
            "example": {
                "before": "Tell me about quantum computing.",
                "after": "Explain quantum computing principles to me like I'm a computer science undergraduate. Focus on qubits, superposition, and quantum gates."
            }
        },
        {
            "title": "Use Stylistic Instructions",
            "description": "You can control the style of response with explicit stylistic instructions.",
            "example": {
                "before": "Write about climate change.",
                "after": "Explain this to me like a topic on a children's educational network show teaching elementary students."
            }
        },
        {
            "title": "Apply Formatting Instructions",
            "description": "Specify the format you want the answer in.",
            "example": {
                "before": "List the top factors affecting climate change.",
                "after": "List the top factors affecting climate change. Use bullet points."
            }
        },
        {
            "title": "Apply Chain of Thought",
            "description": "For complex reasoning, ask the model to think step by step.",
            "example": {
                "before": "What is 25 × 16 + 12 × 4?",
                "after": "Calculate 25 × 16 + 12 × 4 step by step, showing your reasoning for each step."
            }
        }
    ],
    "transformations": [
        {"pattern": r"Could you please\s+", "replacement": ""},
        {"pattern": r"I would like you to\s+", "replacement": ""},
        {"pattern": r"If you don't mind,\s+", "replacement": ""},
        {"pattern": r"It would be great if you could\s+", "replacement": ""},
        {"pattern": r"kindly\s+", "replacement": ""},
        {"pattern": r"Please\s+", "replacement": ""},
        {"pattern": r"\s+if possible", "replacement": ""},
        {"pattern": r"Can you\s+", "replacement": ""},
        {"pattern": r"Would you be able to\s+", "replacement": ""}
    ]
}

# Claude Prompting Guide
CLAUDE_GUIDE = {
    "name": "Claude",
    "source": "Anthropic",
    "url": "https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview",
    "tips": [
        {
            "title": "Be Clear and Direct",
            "description": "Be clear and specific about what you want Claude to do.",
            "example": {
                "before": "I'm wondering if you might be able to tell me a bit about AI ethics?",
                "after": "Explain the three most important principles of AI ethics."
            }
        },
        {
            "title": "Use Examples (Multishot Prompting)",
            "description": "Include 3-5 diverse, relevant examples to show Claude exactly what you want.",
            "example": {
                "before": "Analyze this customer feedback and categorize the issues.",
                "after": "Analyze this customer feedback and categorize the issues. Here's an example:\n<example>\nInput: The new dashboard is a mess! It takes forever to load, and I can't find the export button. Fix this ASAP!\nCategory: UI/UX, Performance\nSentiment: Negative\nPriority: High\n</example>"
            }
        },
        {
            "title": "Let Claude Think (Chain of Thought)",
            "description": "For complex problems, ask Claude to work through its reasoning step by step.",
            "example": {
                "before": "Is 17077 a prime number?",
                "after": "Think through whether 17077 is a prime number step by step."
            }
        },
        {
            "title": "Use XML Tags",
            "description": "Structure your prompt with XML tags to clearly separate different components.",
            "example": {
                "before": "Summarize the following text: Climate change is a global challenge...",
                "after": "<context>Climate change is a global challenge...</context>\n<task>Summarize the above text in 3 bullet points.</task>"
            }
        },
        {
            "title": "Give Claude a Role (System Prompts)",
            "description": "Assign Claude a specific role to frame its perspective and expertise.",
            "example": {
                "before": "Explain how to create a REST API.",
                "after": "You are an experienced software engineering mentor. Explain how to create a REST API to a junior developer."
            }
        }
    ],
    "transformations": [
        {"pattern": r"I'm wondering if you might be able to\s+", "replacement": ""},
        {"pattern": r"I was hoping you could\s+", "replacement": ""},
        {"pattern": r"Could you possibly\s+", "replacement": ""},
        {"pattern": r"If it's not too much trouble,\s+", "replacement": ""},
        {"pattern": r"When you get a chance,\s+", "replacement": ""}
    ]
}

# OpenAI/GPT Prompting Guide
GPT_GUIDE = {
    "name": "GPT",
    "source": "OpenAI",
    "url": "https://platform.openai.com/docs/guides/prompt-engineering",
    "tips": [
        {
            "title": "Write Clear and Specific Instructions",
            "description": "Use clear and specific instructions, and be explicit about what you want.",
            "example": {
                "before": "Tell me about France.",
                "after": "Provide a brief overview of France, including its geography, population, government, and two major historical events."
            }
        },
        {
            "title": "Use Delimiters",
            "description": "Use delimiters to clearly indicate distinct parts of the input.",
            "example": {
                "before": "Summarize the text: France is a country in Western Europe...",
                "after": "Summarize the text delimited by triple backticks:\n```France is a country in Western Europe...```"
            }
        },
        {
            "title": "Use Few-Shot Prompting",
            "description": "Provide examples of successful executions of the task you want performed.",
            "example": {
                "before": "Classify this review: 'The food was amazing!'",
                "after": "Classify the sentiment of the following reviews as positive, negative, or neutral.\n\nReview: 'The service was terrible.'\nSentiment: negative\n\nReview: 'The food was amazing!'\nSentiment:"
            }
        },
        {
            "title": "Specify the Steps",
            "description": "Break down complex tasks into a sequence of steps.",
            "example": {
                "before": "Write a blog post about renewable energy.",
                "after": "Write a blog post about renewable energy by following these steps:\n1. Start with an attention-grabbing introduction\n2. Explain what renewable energy is\n3. Discuss 3 common types of renewable energy\n4. Provide statistics on renewable energy adoption\n5. Conclude with future prospects"
            }
        },
        {
            "title": "Ask the Model to Evaluate Its Response",
            "description": "Ask the model to check whether its response meets the requirements.",
            "example": {
                "before": "Solve this math problem: If x² + 5x + 6 = 0, what is x?",
                "after": "Solve this math problem: If x² + 5x + 6 = 0, what is x? After providing your solution, verify that your answer is correct by substituting it back into the original equation."
            }
        }
    ],
    "transformations": [
        {"pattern": r"Can you\s+", "replacement": ""},
        {"pattern": r"Please\s+", "replacement": ""},
        {"pattern": r"I'd like you to\s+", "replacement": ""},
        {"pattern": r"Could you\s+", "replacement": ""},
        {"pattern": r"Would you mind\s+", "replacement": ""}
    ]
}

# Add all guides to a dictionary for easy lookup
PROMPTING_GUIDES = {
    "llama": LLAMA_GUIDE,
    "claude": CLAUDE_GUIDE,
    "gpt": GPT_GUIDE,
    "openai": GPT_GUIDE,  # Alias
}

# Map model names to their respective guide
MODEL_TO_GUIDE = {
    # Llama models
    "llama-2": "llama",
    "llama-3": "llama",
    "llama-2-7b": "llama",
    "llama-2-13b": "llama",
    "llama-2-70b": "llama",
    "llama-3-8b": "llama",
    "llama-3-70b": "llama",
    
    # Claude models
    "claude-3-opus": "claude",
    "claude-3-sonnet": "claude",
    "claude-3-haiku": "claude",
    "claude-3-5-sonnet": "claude",
    "claude-2": "claude",
    
    # GPT models
    "gpt-3.5-turbo": "gpt",
    "gpt-4": "gpt",
    "gpt-4o": "gpt",
    "gpt-4-turbo": "gpt",
    "gpt-3.5": "gpt",
}

def get_guide_for_model(model_name):
    """Get the appropriate prompting guide for a given model.
    
    Args:
        model_name: Name of the model
        
    Returns:
        The prompting guide dict or None if not found
    """
    # Convert to lowercase for case-insensitive matching
    model_key = model_name.lower()
    
    # Direct match for guide name
    if model_key in PROMPTING_GUIDES:
        return PROMPTING_GUIDES[model_key]
    
    # Match for specific model name
    if model_key in MODEL_TO_GUIDE:
        guide_key = MODEL_TO_GUIDE[model_key]
        return PROMPTING_GUIDES[guide_key]
    
    # Try to match part of the name
    for prefix, guide in MODEL_TO_GUIDE.items():
        if model_key.startswith(prefix):
            return PROMPTING_GUIDES[guide]
    
    # Default to None if no match found
    return None