import requests
import json
from datetime import datetime


with open(
    "evaluation/questions.json"
) as f:
    questions = json.load(f)


results = []


for q in questions:

    print("\nRunning:", q["question"])

    try:

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json={
                "question": q["question"]
            },
            timeout=180
        )

        data = response.json()


        results.append(
            {
                "question": q["question"],
                "answer": data.get("answer"),
                "sources": data.get("sources"),
                "top_score":
                    data["sources"][0]["score"]
                    if data.get("sources")
                    else 0
            }
        )


    except Exception as e:

        results.append(
            {
                "question": q["question"],
                "error": str(e)
            }
        )


with open(
    "evaluation/results.json",
    "w"
) as f:

    json.dump(
        {
            "timestamp": str(datetime.now()),
            "results": results
        },
        f,
        indent=4
    )


print(
    "\nEvaluation complete. Saved evaluation/results.json"
)