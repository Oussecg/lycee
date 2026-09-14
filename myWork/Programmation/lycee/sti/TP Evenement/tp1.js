function inputStyle(elementId, elementCss) {
  document.getElementById(elementId).style = elementCss;
}

function changeSelect(elementId) {
  document.getElementById("p").innerHTML = "Votre niveau est " + document.getElementById(elementId).value;
}
