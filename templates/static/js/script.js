var modal = document.getElementById("myModal");

var btn = document.getElementById("myBtn");

var span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
  modal.style.display = "block";
}

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

var btnEdits = document.getElementsByClassName("btnEdit");
var closeEdits = document.getElementsByClassName("closeEdit");

for (var i = 0; i < btnEdits.length; i++) {
  btnEdits[i].onclick = function () {
    var id = this.getAttribute("data-id");
    var modal = document.getElementById("edit" + id);
    modal.style.display = "block";
  }
}

for (var i = 0; i < closeEdits.length; i++) {
  closeEdits[i].onclick = function () {
    var id = this.getAttribute("data-id");
    var modal = document.getElementById("edit" + id);
    modal.style.display = "none";
  }
}

window.onclick = function (event) {
  if (event.target.className === "modal") {
    event.target.style.display = "none";
  }
}