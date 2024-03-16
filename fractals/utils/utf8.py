from typing import Literal
from unicodedata import normalize
from emoji import demojize, emojize, is_emoji

emoji_forms = EMOJI, CODE = ("emoji", "code")
EmojiForm = tuple[Literal["emoji"], Literal["code"]]
utf8_forms = (NFC, NFD, NFKC, NFKD) = ("NFC", "NFD", "NFKC", "NFKD")
UTF8Form = tuple[Literal["NFC"], Literal["NFD"], Literal["NFKC"], Literal["NFKD"]]


def emoji_fn(text: str, emoji_form: EmojiForm = None) -> str | None:
    """
    Convert from emoji to emoji codes or vice versa.

    @param text - text to be emojized / demojized
    @param emoji_form - whether to convert to emoji (`EMOJI`), emoji codes (`CODE`).
        Skips conversion if None.

    @return text with emoji or emoji codes, or unchanged if emoji_form is None.
    """
    if emoji_form == EMOJI:
        text = emojize(text)
    if emoji_form == CODE:
        text = demojize(text)
    return text


def utf8_norm_fn(text: str, utf8_form: UTF8Form = None) -> str:
    """
    Normalize UTF-8 text.

    @param text - The text to normalize. It must be a string.
    @param utf8_form - The form (NFC | NFD | NFKC | NFKD) according to which the text is normalized.
        If None the normalization is not performed.

    @return The normalized text (or unchanged if utf8_form is None).
    """
    if utf8_form in utf8_forms:
        text = normalize(utf8_form, text)
    return text
