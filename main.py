from pytrends.request import TrendReq
import openai
import newsapi
from google.cloud import texttospeech
import os
from dotenv import load_dotenv
from openai import OpenAI


from openai_utils import rephrase_text
from text_to_speech import text_to_speech

# Load the environment variables from .env file
load_dotenv()

# Access the NewsAPI key
newsapi_key = os.getenv('NEWSAPI_KEY')

# Initialize PyTrends
pytrends = TrendReq()

# Get top trending topics
trending = pytrends.trending_searches(pn='united_states')
top_topic = trending.iloc[0, 0]
print(f"Top Trending Topic: {top_topic}")

# Initialize News API
news_api = newsapi.NewsApiClient(api_key=newsapi_key)

# Search for news
news_articles = news_api.get_everything(q=top_topic)

# Select a news article
selected_article = news_articles['articles'][0]['content']
print('article', selected_article)

rephrased_article = selected_article
# Rephrase the article (this would need an AI model like GPT-3)
# rephrased_article = rephrase_text(selected_article)
# print("Rephrased Article:", rephrased_article)

text_to_speech(rephrased_article, top_topic.replace(" ", "_")
)
# Initialize Google Cloud Text-to-Speech
# client = texttospeech.TextToSpeechClient()
# synthesis_input = texttospeech.SynthesisInput(text=rephrased_article)

# # Perform Text-to-Speech
# response = client.synthesize_speech(
#     input=synthesis_input,
#     voice=texttospeech.VoiceSelectionParams(
#         language_code="en-US",
#         ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL),
#     audio_config=texttospeech.AudioConfig(
#         audio_encoding=texttospeech.AudioEncoding.MP3))

# # Save the audio to a file
# with open("output.mp3", "wb") as out:
#     out.write(response.audio_content)
#     print("Audio content written to file 'output.mp3'")
