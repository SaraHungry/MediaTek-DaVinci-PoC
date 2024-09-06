from fastapi import FastAPI, HTTPException
from typing import List
import random

app = FastAPI()


@app.get(
    "/random-name",
    summary="Get a random name",
    response_description="Random string response",
)
def get_random_name(adjective: int = 1):
    """
    Generates a random string by combining adjective(s) and a noun.

    - **adjective**: the number of adjectives to use (default: 1, max: 10).
    """
    adjectives = [
        "悠揚",
        "快樂",
        "愚蠢",
        "矛盾",
        "嗜睡",
        "神隱",
        "傲慢",
        "可愛",
        "貧困",
        "美麗",
        "調皮",
    ]
    nouns = ["水母", "青苔", "眼屎", "蜻蜓", "王八蛋", "鐘樓怪人", "肚臍眼", "選手"]

    if adjective < 1 or adjective > len(adjectives):
        raise HTTPException(
            status_code=400,
            detail=f"Number of adjectives must be between 1 and {len(adjectives)}.",
        )

    random_adjectives = "".join(random.choices(adjectives, k=adjective))
    random_noun = random.choice(nouns)

    random_str = f"{random_adjectives}的{random_noun}"
    return {"random_string": random_str}


# OpenAPI documentation can be viewed at /docs (Swagger UI) or /redoc (ReDoc)
