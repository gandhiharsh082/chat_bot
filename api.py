import os
import openai
with open('API_KEY.text','r') as F:
  api = F.read()
openai.api_key =str(api)
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
prompt= ""
def callAPI(prompt):
  if(api == 'REPLACE_TO_API_KEY'):
      return "Please open API_KEY.text file and  replace REPLACE_TO_API_KEY to API KEY And Restart project"
  else:
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

