<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <title>꼬맨틀</title>
  <style>
    body { font-family: sans-serif; text-align: center; }
    input { font-size: 20px; padding: 10px; }
  </style>
</head>
<body>
  <h1>꼬맨틀 🔍</h1>
  <p>오늘의 단어를 추측해보세요!</p>
  <input type="text" id="word" placeholder="단어 입력">
  <button onclick="checkWord()">제출</button>
  <div id="result"></div>

  <script>
    async function checkWord() {
      const word = document.getElementById("word").value;
      const res = await fetch("https://your-backend-url.com/similarity", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ input: word })
      });
      const data = await res.json();
      document.getElementById("result").innerHTML = `
        유사도: ${data.similarity}점<br>
        ${data.correct ? "🎉 정답입니다!" : ""}
      `;
    }
  </script>
</body>
</html>
