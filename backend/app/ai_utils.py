import openai
import os

openai.api_key = "Your_API_Key"


def analyze_sentiment(text):
    resp = openai.Completion.create(model="gpt-3.5-turbo", prompt=f"Classify sentiment as Positive, Neutral, Negative:\n{text}", max_tokens=10)
    return resp.choices.text.strip()

def extract_info(text):
    resp = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=f"Extract phone, alternate email, product, and requests from:\n{text}\nFormat as JSON.",
        max_tokens=50
    )
    return resp.choices.text.strip()

def generate_reply(text, sentiment, product):
    prompt = f"""Write a professional, contextual response to the following support email. Sentiment: {sentiment}, Product: {product}. Reply empathetically if sentiment is negative. Email:\n{text}"""
    resp = openai.Completion.create(model="gpt-3.5-turbo", prompt=prompt, max_tokens=200)
    return resp.choices.text.strip()
