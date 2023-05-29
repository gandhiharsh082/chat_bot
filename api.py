import openai
openai.api_key ="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"
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
prompt= ""
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
