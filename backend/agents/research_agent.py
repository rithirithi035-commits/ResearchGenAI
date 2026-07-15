from services.ollama_service import ask_ollama

def research_topic(topic):

    prompt = f"""
You are an expert AI Research Assistant.

Generate a well-structured research report on:

Topic: {topic}

Rules:
- Keep the total length between 400 and 600 words.
- Use simple English.
- Give clear headings.
- Use bullet points wherever appropriate.

Format:

# Title

## Introduction

## What is it?

## Key Features

## Advantages

## Disadvantages

## Real-world Applications

## Future Scope

## Conclusion
"""

    return ask_ollama(prompt)