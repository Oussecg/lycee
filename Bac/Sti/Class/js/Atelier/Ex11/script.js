function Force() {
	let ch = document.getElementById("mp").value;
	let n1 = 0;
	let n2 = 0;
	let n3 = 0;
	for (let i = 0; i < ch.length; i++) {
		let c = ch[i].toUpperCase();
		if ("0" <= c && c <= "9") {
			n1++;
		} else if ("A" <= c && c <= "Z") {
			n2++;
		} else {
			n3++;
		}
	}
	let s = n1 * 2 + n2 * 3 + n3 * 5;
    if (ch == ""){
        document.getElementById("out").innerHTML = "";
		document.getElementById("out").style.color = "black";
		document.getElementById("mp").style.backgroundColor = "white";
    }
	else if (s > 30) {
		document.getElementById("out").innerHTML = "Forte";
		document.getElementById("out").style.color = "green";
		document.getElementById("mp").style.background = "green";
	} else if (20 < s){
        document.getElementById("out").innerHTML = "Moyen";
		document.getElementById("out").style.color = "orange";
		document.getElementById("mp").style.background = "orange";
    } else if (s < 20){
        document.getElementById("out").innerHTML = "Faible";
		document.getElementById("out").style.color = "red";
		document.getElementById("mp").style.background = "red";
    }
}
