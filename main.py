import random
from typing import List

import yaml
from fastapi import FastAPI, HTTPException
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse, Response

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
    return random_str


# endpoint to serve OpenAPI YAML
@app.get("/openapi.yaml", include_in_schema=False)
async def openapi_yaml():
    openapi_json = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    openapi_yaml = yaml.dump(openapi_json, sort_keys=False)
    return Response(content=openapi_yaml, media_type="text/plain")


@app.get("/config.json", summary="Get config file", include_in_schema=False)
async def get_config_file():
    return JSONResponse(
        content={
            "id": "random-name",
            "schema_version": "v1",
            "name_for_human": "random-name",
            "name_for_model": "random-name",
            "description_for_human": "generate random name",
            "description_for_model": "generate random name",
            "api": {
                "type": "openapi",
                "url": "https://mediatek-davinci-poc.onrender.com/openapi.yaml",
            },
        }
    )
