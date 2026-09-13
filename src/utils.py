import pymupdf


def extract_pages(pdf_path):

    doc = pymupdf.open(pdf_path)

    pages = []

    for page_number, page in enumerate(doc):

        pages.append(
            {
                "text": page.get_text(),
                "page": page_number + 1
            }
        )

    return pages


def split_text(text, chunk_size=500, overlap=50):

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        chunks.append(
            text[start:end]
        )

        start += chunk_size - overlap

    return chunks