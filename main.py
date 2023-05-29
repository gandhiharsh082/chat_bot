from flask import Flask, render_template, request
import api
app = Flask(__name__)
@app.route("/")
def index():
    return render_template('index.html')
@app.route("/getAnswer" ,methods=['GET','POST'])
def getAnswer():
    start_sequence = "\nA:"
    if(request.method == 'POST'):
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            # print(json['prompt'])
            prompt=json['prompt']+start_sequence
            # print(prompt)
            response = api.callAPI(prompt)
            json_response = {
                "answer": response,
                "prompt":prompt+response
            }
            # print(json_response)
            return json_response
        else:
            json_response = {
                "answer": "Something went wrong",
            }
            return json_response
        # prompt = request.form.get('prompt')

    else:
        json_response = {
            "answer": "Something went wrong",
        }
        return json_response
app.run(debug=True)



