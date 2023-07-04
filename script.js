document.getElementById('sendbutton').addEventListener('click', function(){
    var userText = document.getElementById('userinput').value;
    //clear the input field
    document.getElementById('userinput').value = "";
    //add user text to chatbox
    document.getElementById('chatbox').innerHTML += "User: " + userText + "<br>";

    //send user text to backend
    fetch('/get_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'message': userText }),
    })
    .then(response => response.json())
    .then(data => {
        //add bot's response to chatbox
        document.getElementById('chatbox').innerHTML += "Bot: " + data['message'] + "<br>";
    });
});
