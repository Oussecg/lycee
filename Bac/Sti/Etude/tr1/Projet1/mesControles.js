function GenererIp() {
	let ch = "";
	for (let i = 0; i < 4; i++) {
		ch += String(rd(0, 255));
		ch += ".";
	}
	ch = ch.substring(0, ch.length - 1);
	document.getElementById("ip").value = ch;
}

function rd(x, y) {
	let r = Math.round(Math.random() * y - x) + x;
	return r;
}

function Enregistrent() {
	let ip = document.getElementById("ip").value;
	if (ip === "") {
        alert("Yzi min blada !!!");
		return false;
	}

	let md = document.getElementById("mod").value;
    let nb = 0;
    for (let i = 0; i < md.length; i++) {
        if (md[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]){
            nb += 1
        }
    }

	if (!(md.length <= 20 && md != "" && "A" <= md[0] && md[0] <= "Z" && nb <= 1)) {
        alert("Yzi min blada !!!");
		return false;
	}
    
    let g = document.getElementsByName("st");
    if (! (g[0].checked || g[1].checked || g[2].checked)){
        alert("Yzi min blada !!!");
		return false;
    }

    let Cd = document.getElementById("Cd").value;
    if (!(1 <= Cd && Cd <= 40)){
        alert("Yzi min blada !!!");
		return false;
    }

    let Ad = document.getElementById("Ad").value;
    if (!(1 <= Ad && Ad <= 40)){
        alert("Yzi min blada !!!");
		return false;
    }
}

function AfficheDate(){
    let Da = new Date();
    let a = Da.getFullYear();
    let m = String(Da.getMonth() + 1);
    let d = String(Da.getDay());

    if (m.length != 2){
        m = "0" + m;
    }

    if (d.length != 2){
        d = "0" + d;
    }
    let ch = a + "-" + m + "-" + d;

    document.getElementById("Dm").value = ch;
}

function DateMission(){
    let Ip = document.getElementById("Ip1").value;
    
    let test = true;
    let i = 0;
    while (test && i < Ip.length){
        if (! (isNaN(Ip[i]) == false && 0 <= parseInt(Ip[i]) && parseInt(Ip[i]) <= 255 || Ip[i] == ".")  ){
            test = false
        } else{
            i += 1;
        }
    }

    if (! test){
        alert("Yzi min blada !!!");
        return false;
    }

    let Hd = document.getElementById("Hd").value;
    if (!(Hd)){
        alert("Yzi min blada !!!");
        return false;
    }

    let Ha = document.getElementById("Ha").value;
    if (!(Ha)){
        alert("Yzi min blada !!!");
        return false;
    }

    let dis = parseInt(document.getElementById("Dis").value);
    if (! (1 <= dis && dis <= 40) ){
        alert("Yzi min blada !!!");
        return false;
    }
}