from fastapi import FastAPI, HTTPException
from gbif_client import APIHandler
from embedding_service import AbstractEmbedder
from typing import List

app = FastAPI()
api_handler = APIHandler()
abstract_embedder = AbstractEmbedder()

@app.get("/process-items/")
def process_items(limit: int):
    if not 1 <= limit <= 20:
        raise HTTPException(status_code=400,
                            detail="Limit must be between 1 and 20")

    # Get items from the API
    items = api_handler.run(limit)
    if not items:
        return []

    # Process each item with the transformer model
    processed_results = []
    for item in items:
        if item.get('abstract'):
            embedding = abstract_embedder.embed_abstract(item)
            processed_results.append({'item':item,
                                      'result':embedding.tolist()})

    return processed_results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
