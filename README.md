
# The Chat GPT with no-brain

A Chat-bot that reply your question and calculations 


## Technical Details:-

####  Languages : 
`Python3` `HTML5` `CSS3` `JavaScript`

#### Frameworks :
`Flask` `Bootstrap 4`
## Installation

`Fork` the repository, this will make a copy of this project in your account.

Clone the repository by running below command

```bash
https://github.com/gandhiharsh082/chat_bot.git
```

Open the folder by running below command

```bash
cd chat_bot
```

Install dependencies

```bash
pip install -r requirements.txt
```
open api.py.text file

Replace  REPLACE_TO_API_KEY to   `API_KEY`

Run app.py using below command to start Chat-Bot

```bash
python main.py
```

Note:- You must be on python version 3.

Navigate to URL "http://localhost:5000/"
- Now, You should be able to view the chat page.

## How to get API KEY

 - Step 1 : Go to the OpenAI website (https://openai.com) and click on the "Get started" button or navigate directly to the OpenAI API page (https://www.openai.com/api/).
 - Step 2 : Click on the "Sign up" button to create an account. If you already have an account, you can log in instead.
 - Step 3 : Navigate to the API page or click on your account settings, where you may find a section for API access or settings.
 - Step 4 : In the API section, you should see options to create or manage your API keys. Click on the appropriate button to generate a new API key. 


## API Reference

#### OPEN AI

```http
  POST Request
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |
| `model` | `string` |total tokens must be below the model’s maximum limit |
| `temperature` | `interger` |Setting temperature to 0 will make the outputs mostly deterministic, but a small amount of variability may remain |
| `max_tokens` | `interger` |The model is better at inserting longer completions|
| `top_p` | `interger` |The "top_p" parameter is particularly useful for controlling the randomness and fluency of the generated text|
| `frequency_penalty` | `interger` |It allows you to adjust the model's tendency to reuse certain words or phrases|

its return string in object


#### Screenshot 

![Logo](screenshot.png)

