from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
  api_key=os.environ.get("OPENAI_API_KEY"),
)

def rephrase_text(original_text):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a newspaper editor, skilled in writing article."},
                {"role": "user", "content": f"Rewrite the following text in a different way: {original_text}"}
            ]
        )
        rephrased_text = response.choices[0].text.strip()
        return rephrased_text
    except Exception as e:
        print("Error during text rephrasing:", e)
        return None
