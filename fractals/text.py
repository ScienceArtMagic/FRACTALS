from os import linesep

from .utils.utf8 import (
    CODE,
    EMOJI,
    EmojiForm,
    emoji_fn,
    NFC,
    NFD,
    NFKC,
    NFKD,
    UTF8Form,
    utf8_norm_fn,
)


def encode(text: str, utf8_form: UTF8Form = None, emoji_form: EmojiForm = EMOJI):
    # text = text.strip() ### disable to allow (multiple) preceding spaces (e.g. in code)
    text = utf8_norm_fn(emoji_fn(text, emoji_form), utf8_form)
    return [
        [
            [
                list(bytearray(char, "utf-8"))  # if ord(char) > 255 else [ord(char)]
                for char in word.strip("")
                if len(char)
            ]
            for word in line.split(" ")
        ]
        for line in text.splitlines()
    ]


def decode(
    encoded,
    utf8_form: UTF8Form = None,
    emoji_form: EmojiForm = CODE,
):
    decoded = linesep.join(
        " ".join("".join(bytes(char).decode("utf-8") for char in word) for word in line)
        for line in encoded
    )
    decoded = utf8_norm_fn(decoded, utf8_form)
    decoded = emoji_fn(decoded, emoji_form)
    return decoded
