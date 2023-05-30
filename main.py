from flask import Flask, render_template, request
import api
app = Flask(__name__)
# create  route
@app.route("/")
# Display the index page 
def index():
    return render_template('index.html')
# Get the question from the front end using the POST method   
@app.route("/getAnswer" ,methods=['GET','POST'])
def getAnswer():
    start_sequence = "\nA:"
  # Verify the method 
    if(request.method == 'POST'):
       # Verify api header content type 
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            #  Data is stored in a json variable from the frontend javascript API
            json = request.json
            # print(json['prompt'])
            # The prompt is retrieved from the json file. An open AI prompt that sends an answer back
            # prompt like Q: How many squigs are in a bonk?\nA:  
            # The Q: stands for question, and the A: stands for Answer . 
            prompt=json['prompt']+start_sequence
            # print(prompt)
            # openai api call 
            response = api.callAPI(prompt)
            json_response = {
                "answer": response,
                "prompt":prompt+response
            }
            # print(json_response)
            # return an  object 
            return json_response
        else:
            #return  content_type is not application/json 
            json_response = {
                "answer": "Something went wrong",
            }
            return json_response
        # prompt = request.form.get('prompt')

    else:
          #return  when request not POST 
        json_response = {
            "answer": "Something went wrong",
        }
        return json_response
app.run(debug=True)



