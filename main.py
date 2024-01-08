from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel

from helper import extract_ebook_blurb
app = FastAPI() # create instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class params(BaseModel):
    paid_product_blurb: str

@app.get("/ebook_blurb")
async def read_users(params):
    # paid_product_blurb = "if you want our expert support to apply automation principles outlined in the ebook give us a shout! We have 4 slots left for 1to1 coaching sessions left. Use the code 'FITMATE25' for 25% off the standard price. 7 day money back guarantee!"
    paid_product_blurb = params.paid_product_blurb
    return { "ebook_blurb": extract_ebook_blurb(paid_product_blurb) }