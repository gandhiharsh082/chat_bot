import os
import openai

# Set OpenAI API key
openai.api_key = "REPLACE_TO_API_KEY"

# Define start and restart sequences for conversation
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

# Initialize prompt
prompt = ""

# Function to call the OpenAI API
def callAPI(prompt):
  response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0,
      max_tokens=100,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
      stop=["\n"]
  )
  return response.choices[0].text
