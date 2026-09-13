from src.utils import split_text


def create_chunks(pages, source):

    chunks = []

    for page in pages:

        page_chunks = split_text(
            page["text"]
        )

        for chunk in page_chunks:

            chunks.append(
                {
                    "text": chunk,
                    "source": source,
                    "page": page["page"]
                }
            )

    return chunks