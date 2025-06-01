# server.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from gensim.models import KeyedVectors
import random, hashlib
from datetime import datetime

app = FastAPI()
model = KeyedVectors.load("reduced_fasttext.kv")

# CORS 허용
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 배포 후에는 도메인 제한 추천
    allow_methods=["*"],
    allow_headers=["*"],
)

word_list = [w for w in model.key_to_index if len(w) >= 2 and w.isalpha()]
seed = int(hashlib.md5(datetime.now().date().isoformat().encode()).hexdigest(), 16)
random.seed(seed)
answer = random.choice(word_list)

class InputWord(BaseModel):
    input: str

@app.post("/similarity")
def similarity_score(data: InputWord):
    word = data.input
    try:
        sim = round(model.similarity(word, answer) * 100, 2)
        return {"similarity": sim, "correct": word == answer}
    except:
        return {"similarity": 0, "correct": False}
