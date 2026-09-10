function IdPatient() {
	let ch = "";
	for (let i = 0; i < 10; i++) {
		let x = Math.trunc(Math.random() * 10);
		if (x % 2 === 0) {
			ch = String(x) + ch;
		} else {
			ch = ch + String(x);
		}
	}
	document.getElementById("IdPatient").value = ch;
}

function est_alpha(ch) {
	let test = true;
	let i = 0;
	do {
		if (
			("A" <= ch[i].toUpperCase() && ch[i].toUpperCase() <= "Z") ||
			ch[i] === ""
		) {
			i = i + 1;
		} else {
			test = false;
		}
	} while (i < ch.length && test);
	return test;
}

function Patient() {
	let nom = document.getElementById("Nom").value;
	if (
		!(
			3 <= nom.length &&
			nom.length <= 20 &&
			"A" <= nom[0].toUpperCase() &&
			nom[0].toUpperCase() <= "Z" &&
			"A" <= nom[nom.length - 1].toUpperCase() &&
			nom[nom.length - 1].toUpperCase() <= "Z" &&
			est_alpha(nom)
		)
	) {
		return false;
	}

	let Prenom = document.getElementById("Prenom").value;
	if (
		!(
			3 <= Prenom.length &&
			Prenom.length <= 20 &&
			"A" <= Prenom[0].toUpperCase() &&
			Prenom[0].toUpperCase() <= "Z" &&
			"A" <= Prenom[Prenom.length - 1].toUpperCase() &&
			Prenom[Prenom.length - 1].toUpperCase() <= "Z" &&
			est_alpha(Prenom)
		)
	) {
		return false;
	}

	let dateNaissance = document.getElementById("dateNaissance").value;
	if (!dateNaissance || new Date() < new Date(dateNaissance)) {
		return false;
	}

	let sex = document.getElementsByName("sex");
	if (sex[0].checked === false && sex[1].checked === false) {
		return false;
	}

	let tel = document.getElementById("tel").value;
	if (tel.length !== 8 || parseInt(tel[0]) === 0 || isNaN(tel)) {
		return false;
	}

	let email = document.getElementById("email").value;
	if (
		email.length > 50 ||
		(email.indexOf(".com") === -1 && email.indexOf(".tn") === -1)
	) {
		return false;
	}

	let sanguinGroup = document.getElementById("groupSanguine").selectedIndex;
	if (sanguinGroup <= 0) {
		return false;
	}

	let antecedantMedical = document.getElementById("antecedantMedical").value;
	if (
		!(
			"A" <= antecedantMedical[0].toUpperCase() &&
			antecedantMedical[0].toUpperCase() <= "Z" &&
			antecedantMedical[antecedantMedical.length - 1].toUpperCase() === "."
		)
	) {
		return false;
	}
}
