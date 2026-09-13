from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(pages, source):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        separators=[
            "\n\n",
            "\n",
            ".",
            " ",
            ""
        ]
    )


    chunks = []


    for page in pages:

        page_chunks = splitter.split_text(
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