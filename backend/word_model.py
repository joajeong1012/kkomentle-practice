from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('backend/data/cc.ko.300.vec', binary=False)

def get_similarity_score(word1, word2):
    try:
        return model.similarity(word1, word2)
    except KeyError:
        return -1.0

def get_rank(word1, word2):
    try:
        similar = model.most_similar(word2, topn=1000)
        for i, (w, _) in enumerate(similar):
            if w == word1:
                return i + 1
        return None
    except KeyError:
        return None
