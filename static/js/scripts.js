async function getText() {
    // POST request using fetch()
    let question = "";
    let question_html;
    let answer_html;
    let restart_sequence = "\n\nQ: ";
    let input = $('#input_question').val();
    $('#input_question').val('')
    question = restart_sequence + input;
    if (localStorage.getItem('prompt')) {
        myobj_deserialized = JSON.parse(localStorage.getItem('prompt'))
        question = myobj_deserialized.prompt + question;
    }
    if (input) {

        question_html = `<div class="media media-chat media-chat-reverse">
        <div class="media-body">
            <p>${input}</p>
        </div>
    </div>
`;
        $('#chat-content').append(question_html);
        let scrolle = document.getElementById('chat-content');
        scrolle.scrollTop = scrolle.scrollHeight;
        // console.log(question);
        let body = {
            prompt: String(question),
        }
        const response = await fetch("http://127.0.0.1:5000/getAnswer", {
            // Adding method type
            method: "POST",
            // Adding body or contents to send
            body: JSON.stringify(body),
            // Adding headers to the request
            headers: {
                "Content-type": "application/json"
            }
        })
        const data_api = await response.json();
        // console.log(data_api);
        answer_html = `
        <div class="media media-chat">
        <img class="avatar" src="https://media.istockphoto.com/id/1010001882/vector/%C3%B0%C3%B0%C2%B5%C3%B1%C3%B0%C3%B1%C3%B1.jpg?s=612x612&w=0&k=20&c=1jeAr9KSx3sG7SKxUPR_j8WPSZq_NIKL0P-MA4F1xRw="
            alt="...">
        <div class="media-body">
            <p>${data_api.answer}</p>
        </div>
    </div>
        `;
        $('#chat-content').append(answer_html);

        let data = {
            prompt: data_api.prompt,
        }
        myObj_serialized = JSON.stringify(data);
        localStorage.setItem('prompt', myObj_serialized);

        let scrolle1 = document.getElementById('chat-content');
        scrolle1.scrollTop = scrolle1.scrollHeight;
    }
}
$(window).on('beforeunload', function () {
    localStorage.clear();
});



