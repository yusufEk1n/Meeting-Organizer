var btnAdd = document.getElementById("btnAdd");
var closeAdd = document.getElementsByClassName("closeAdd")[0];
var btnEdit = document.getElementsByClassName("btnEdit");
var closeEdit = document.getElementsByClassName("closeEdit");

/* Yeni toplantı ekle butonuna tıklandığında modalı açar */
btnAdd.onclick = function() {
  var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

/* modalın sağ üstündeki X butonuna tıklandığında modalı kapatır */
closeAdd.onclick = function() {
  var modal = document.getElementById("myModal");
  modal.style.display = "none";
}

/* Sayfada herhangi bir toplantı düzenlenmek istendiğinde ilgili modalı açar */
for (var i = 0; i < btnEdit.length; i++) {
  btnEdit[i].onclick = function () {
    var id = this.getAttribute("data-id");
    var modal = document.getElementById("edit" + id);
    modal.style.display = "block";
  }
}

/* Düzenlenen toplantının modalında sağ üstündeki X butonuna tıklandığında modalı kapatır */
for (var i = 0; i < closeEdit.length; i++) {
  closeEdit[i].onclick = function () {
    var id = this.getAttribute("data-id");
    var modal = document.getElementById("edit" + id);
    modal.style.display = "none";
  }
}

/* Sayfada herhangi bir yere tıklandığında açık olan modalları kapatır */
window.onclick = function (event) {
  if (event.target.className === "modal") {
    event.target.style.display = "none";
  }
}