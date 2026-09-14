function IdPatient() {
	do {
		ch = "";
		for (let i = 0; i < 10; i++) {
			x = Math.round(Math.random() * 9);
			if (x % 2 === 0) {
				ch = String(x) + ch;
			} else {
				ch = ch + String(x);
			}
		}
	} while (parseInt(ch[0]) % 2 == 1 || parseInt(ch.length - 1) == 0);
	document.getElementById("IdPatient").value = ch;
}

function est_alpha(ch) {
	test = true;
	i = 0;
	while (i < ch.length && test) {
		if (
			("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z") ||
			ch[i] === " "
		) {
			i = i + 1;
		} else {
			test = false;
		}
	}
	return test;
}

function Patient() {
	nom = document.getElementById("nom").value;
	if (
		!(
			3 <= nom.length &&
			nom.length <= 20 &&
			est_alpha(nom) &&
			"A" <= nom[0].toUpperCase() &&
			nom[0].toUpperCase() <= "Z" &&
			"A" <= nom[nom.length - 1].toUpperCase() &&
			nom[nom.length - 1].toUpperCase() <= "Z"
		)
	) {
		alert("Ti wallah !!! Nom 8alit");
		return false;
	}

	pre = document.getElementById("pre").value;
	if (
		!(
			3 <= pre.length &&
			pre.length <= 20 &&
			est_alpha(pre) &&
			"A" <= pre[0].toUpperCase() &&
			pre[0].toUpperCase() <= "Z" &&
			"A" <= pre[pre.length - 1].toUpperCase() &&
			pre[pre.length - 1].toUpperCase() <= "Z"
		)
	) {
		alert("Ti wallah !!! Prénom 8alit");
		return false;
	}

	dateNais = new Date(document.getElementById("dateNaissance").value);
	dateNow = new Date();
	if (dateNais > dateNow) {
		alert("Ti wallah !!! 3lh ta3tini date Naissance 8alit");
		return false;
	}

	sexH = document.getElementById("h").checked;
	sexF = document.getElementById("f").checked;
	if (!sexH && !sexF) {
		alert("Choisie Votre sex !");
		return false;
	}

	tel = document.getElementById("tel").value;
	if (tel.length !== 8 || tel[0] === "0" || isNaN(tel)) {
		alert("Ti wallah !!! Iktib nombrouk w yzi mn blada mte3ik");
		return false;
	}

	email = document.getElementById("email").value;
	if (
		email.length > 50 ||
		(email.indexOf(".com") === -1 && email.indexOf(".tn") === -1)
	) {
		alert("Ti wallah !!! Iktib email w yzi mn blada");
		return false;
	}

	sanguineChoix = document.getElementById("ts").selectedIndex;
	if (sanguineChoix <= 0) {
		alert("Ti wallah !!! A5tar Damik w yzi mn blada");
		return false;
	}

	antecedent = document.getElementById("am").value;
	if (
		!(
			"A" <= antecedent[0].toUpperCase() && antecedent[0].toUpperCase() <= "Z"
		) ||
		antecedent[antecedent.length - 1] !== "."
	) {
		alert("Ti wallah !!! Iktib Antécédent Médical w yzi mn blada");
		return false;
	}
}

function activerMedecin() {
	if (RVD("medecin")) {
		document.getElementById("codeMedecin").disabled = false;
		document.getElementById("codeMedecin").focus();
	}
}

function verifier(ch) {
	let i = 0;
	let test = true;
	while (i < ch.length - 1 && test) {
		if (parseInt(ch[i]) % 2 == 0) {
			i = i + 1;
		} else {
			test = false;
		}
	}
	test = true;
	while (i < ch.length && test) {
		if (parseInt(ch[i]) % 2 == 1) {
			i = i + 1;
		} else {
			test = false;
		}
	}
	return test;
}

function RVD(option) {
	let IdPatient = document.getElementById("idPatient");
	if (option == "medecin") {
		if (
			IdPatient.value.length !== 10 ||
			isNaN(IdPatient.value) ||
			!verifier(IdPatient.value)
		) {
			return false;
		} else {
			return true;
		}
	} else {
		let codeMedecin = document.getElementById("codeMedecin").value;
		if (
			!(
				codeMedecin.length === 5 &&
				codeMedecin[0] == "M" &&
				0 <= parseInt(codeMedecin[1]) &&
				parseInt(codeMedecin[1]) <= 9 &&
				0 <= parseInt(codeMedecin[2]) &&
				parseInt(codeMedecin[2]) <= 9 &&
				0 <= parseInt(codeMedecin[3]) &&
				parseInt(codeMedecin[3]) <= 9 &&
				0 <= parseInt(codeMedecin[4]) &&
				parseInt(codeMedecin[4]) <= 9
			)
		) {
			return false;
		}

		let dateRvd = document.getElementById("dateRvd").value;
		let j = new Date(dateRvd).toString().substring(0, 3);
		if (
			dateRvd == "" ||
			new Date(dateRvd) < new Date() ||
			j.toLowerCase() == "sun"
		) {
			alert("Erreur !");
			return false;
		}

		let heureRvd = document.getElementById("heureRvd").value;
		if (heureRvd == "") {
			return false;
		} else {
			if (j.toLowerCase() == "sat") {
				if (heureRvd >= "14:00") {
					alert("If samedi ija bokri");
					return false;
				}
			}
		}
	}
}

function Contact() {
	let contactNom = document.getElementById("contactNom").value;
	if (
		!(
			7 <= contactNom.length &&
			contactNom.length <= 40 &&
			"A" <= contactNom[0].toUpperCase() &&
			contactNom[0].toUpperCase() <= "Z" &&
			"A" <= contactNom[contactNom.length - 1].toUpperCase() &&
			contactNom[contactNom.length - 1].toUpperCase() <= "Z" &&
			est_alpha(contactNom)
		)
	) {
		alert("Saisir Votre Nom !");
		return false;
	}

	let contactEmail = document.getElementById("contactEmail").value;
	if (!(contactEmail.length <= 50 && (contactEmail.indexOf(".com") != -1 || contactEmail.indexOf(".tn") != -1))){
		alert("Saisir Votre Email !");
		return false;
	}

	let contactMessage = document.getElementById("contactMessage").value;
	if (contactMessage == "" || contactMessage.length > 150){
		alert("Remplir un message !");
		return false;
	}
}
