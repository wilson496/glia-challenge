# from typing import Union
from random import shuffle

from fastapi import APIRouter
# from pydantic import BaseModel


router = APIRouter()


# TODO: Enforce the use of a single word?
@router.post("/jumble/{word}")
def post_word_to_jumble(word: str):
    word = list(word)
    shuffle(word)
    return ''.join(word)


@router.get("/audit")
def get_last_ten_jumbles():
    pass
