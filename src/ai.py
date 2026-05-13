import os
from openai import OpenAI
from pydantic import BaseModel
from typing import List

class EnglishWord(BaseModel):
    word: str
    word_type: str
    ipa: str
    meaning_vi: str
    examples: List[str]
    usage_context: str
    mindset: str

class AIEngine:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"

    def generate_daily_word(self, level: str = "Intermediate") -> EnglishWord:
        prompt = f"""
        Generate a new English word for an {level} learner.
        Include:
        - The word and its type (noun, verb, etc.)
        - IPA pronunciation.
        - Meaning in Vietnamese.
        - 3 example sentences.
        - Usage context (When to use this word).
        - Mindset/Nuance (How to think about this word vs synonyms).
        
        Return the result in JSON format.
        """
        
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert English teacher."},
                {"role": "user", "content": prompt}
            ],
            response_format=EnglishWord
        )
        
        return response.choices[0].message.parsed
