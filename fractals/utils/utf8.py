from typing import Literal
from unicodedata import normalize
from emoji import demojize, emojize, is_emoji

utf8_forms = (NFC, NFD, NFKC, NFKD) = ("NFC", "NFD", "NFKC", "NFKD")
UTF8Form = tuple[Literal["NFC"], Literal["NFD"], Literal["NFKC"], Literal["NFKD"]]
emoji_forms = EMOJI, CODE = ("emoji", "code")
EmojiForm = tuple[Literal["emoji"], Literal["code"]]


def emoji_fn(text: str, emoji_form: EmojiForm = None) -> str | None:
    if emoji_form == EMOJI:
        text = emojize(text)
    if emoji_form == CODE:
        text = demojize(text)
    return text


def utf8_norm_fn(text: str, utf8_form: UTF8Form = None) -> str:
    if utf8_form in utf8_forms:
        text = normalize(utf8_form, text)
    return text
