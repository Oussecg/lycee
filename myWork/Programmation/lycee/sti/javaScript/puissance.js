document.getElementById("execute").addEventListener("click", () => {
  let A = Number(document.getElementById("inputA").value);
  let B = Number(document.getElementById("inputB").value);
  P = 1;
  for (let i = 0; i < B; i++) {
    P *= A;
  }
  document.getElementById("result").innerHTML("P = " + P);
});
