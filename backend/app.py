from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from word_model import get_similarity_score, get_rank
from words import get_today_answer

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/guess")
async def guess(word: str):
    answer = get_today_answer()
    sim = get_similarity_score(word, answer)
    rank = get_rank(word, answer)
    return {
        "guess": word,
        "similarity": round(sim * 100, 2),
        "rank": rank,
        "correct": word == answer
    }

@app.get("/answer")
def answer():
    return {"answer": get_today_answer()}
