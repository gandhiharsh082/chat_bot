import os
import openai
openai.api_key = "REPLACE_TO_API_KEY"
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
prompt = ""
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



