function showMessageBox() {
  document.getElementById("messageBoxOverlay").style.display = "flex";
  document.getElementById("messageText").textContent = "** This chart shows different temperature ranges and its effects on our body **";
}

function hideMessageBox() {
  document.getElementById("messageBoxOverlay").style.display = "none";
}
