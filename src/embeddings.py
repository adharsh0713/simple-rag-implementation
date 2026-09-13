from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def create_embeddings(items):

    texts = []

    for item in items:

        if isinstance(item, dict):
            texts.append(item["text"])
        else:
            texts.append(item)

    return model.encode(texts)