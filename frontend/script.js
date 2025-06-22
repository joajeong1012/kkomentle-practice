async function submitGuess() {
  const word = document.getElementById("guessInput").value.trim();
  if (!word) return;

  const res = await fetch(`https://your-backend-url.onrender.com/guess?word=${word}`);
  const data = await res.json();

  const li = document.createElement("li");
  li.innerText = `${data.guess} → 유사도: ${data.similarity}, 순위: ${data.rank ?? "없음"}`;
  document.getElementById("history").prepend(li);

  if (data.correct) {
    alert(`정답입니다! (${data.guess})`);
  }
}
