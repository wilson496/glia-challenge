# from typing import Union
from random import sample

from fastapi import APIRouter
# from pydantic import BaseModel


router = APIRouter()

api_calls = []


# TODO: Enforce the use of a single word?
@router.post("/jumble/{word}")
def post_word_to_jumble(word: str):

    # TODO: Enforce single word (maybe?)

    # Make sure shuffled word DOES NOT match original
    # Initial testing with word 'foo' would return
    # a "shuffled" result of foo sometimes
    while (True):
        shuffled = ''.join(sample(word, len(word)))
        if shuffled != word:
            break
    api_calls.append({"word": str(word), "shuffled_word": str(shuffled)})
    return shuffled


@router.get("/audit")
def get_last_ten_jumbles():
    list = api_calls[-10:]
    return list
