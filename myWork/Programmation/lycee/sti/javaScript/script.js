N = Number(prompt("Input a Number"))
while (N < 0) {
  alert("Type a Number superior to 0 !")
  N = Number(prompt("Input a Number"))
}

if (N == 0) {
  N = N + 100
  alert(N - 100 + " + 100 = " + N)
} else if (N > 0 && N <= 20){
  N = N + 20
  alert(N - 20 + " + 20 = " + N)
} else {
  for (let i = 1; i < N; i += 2) {
    document.write("I =" + i + "<br>")
  }
}

