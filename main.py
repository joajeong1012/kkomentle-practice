from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from gensim.models import KeyedVectors
import datetime, hashlib, random

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# 모델 로드 (같은 폴더에 reduced_fasttext.kv 있어야 함)
model = KeyedVectors.load("reduced_fasttext.kv")
word_list = [w for w in model.key_to_index if len(w) >= 2 and w.isalpha()]

# 날짜 기반 정답 고정
seed = int(hashlib.md5(datetime.date.today().isoformat().encode()).hexdigest(), 16)
random.seed(seed)
answer = random.choice(word_list)

class Input(BaseModel):
    input: str

@app.post("/similarity")
def similarity(data: Input):
    word = data.input
    try:
        sim = round(model.similarity(word, answer) * 100, 2)
        return {"similarity": sim, "correct": word == answer}
    except:
        return {"similarity": None, "correct": False}
