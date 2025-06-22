from datetime import datetime
import random

with open("backend/data/wiktionary_korean_words.txt", encoding="utf-8") as f:
    word_list = [w.strip() for w in f.readlines() if len(w.strip()) >= 2]

def get_today_answer():
    seed = int(datetime.utcnow().strftime("%Y%m%d"))
    random.seed(seed)
    return random.choice(word_list)
