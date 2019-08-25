document.getElementById('check').onclick = function () {
    check();
}

document.getElementById('register').onclick = function () {
    register();
}


function check() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('message').innerText = this.responseText;
        }
    };
    const user_name = document.getElementById('user_name').value;
    xhttp.open("GET", `http://127.0.0.1:5000/?name=${user_name}`, true);
    xhttp.send();
}

function register() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById('message').innerText = this.responseText;
        }
    };
    const user_name = document.getElementById('user_name').value;
    xhttp.open("POST", "http://127.0.0.1:5000/", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(`name=${user_name}`);
}