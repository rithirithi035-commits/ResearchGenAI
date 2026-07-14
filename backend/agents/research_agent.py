from services.ollama_service import ask_ollama

def research_topic(topic):

    prompt = f"""
You are an expert AI Research Assistant.

Research the following topic:

{topic}

Return your answer in this format:

# Title

## Overview

## Key Concepts

## Advantages

## Challenges

## Real World Applications

## Future Scope

## Conclusion

Make the explanation beginner-friendly.
"""

    return ask_ollama(prompt)