function sendMsg(){
    let msg = document.getElementById("msg").value;
    let chatBox = document.getElementById("chat");

    chatBox.innerHTML += "<b>You:</b> " + msg + "<br>";

    fetch("/chat",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({message:msg})
    })
    .then(res => res.json())
    .then(data => {
        chatBox.innerHTML += "<b>Bot:</b> " + data.reply + "<br><br>";
    });

    document.getElementById("msg").value = "";
}
