from os import linesep
from dataclasses import dataclass
from unicodedata import normalize
from emoji import demojize, emojize, is_emoji


@dataclass
class Form:
    NFC: str = "NFC"
    NFD: str = "NFD"
    NFKC: str = "NFKC"
    NFKD: str = "NFKD"


@dataclass
class Emoji:
    emojize: str = "emojize"
    demojize: str = "demojize"


def encode(text: str, norm_form: Form = None, emoji: Emoji = Emoji.emojize):
    # text = text.strip()
    if emoji == Emoji.emojize:
        text = emojize(text)
    else:
        if emoji == Emoji.demojize:
            text = demojize(text)
    if isinstance(norm_form, Form):
        text = normalize(norm_form, text)
    return [
        [
            [
                list(bytearray(char, "utf-8"))  # if ord(char) > 255 else [ord(char)]
                for char in word.strip("")
                if len(char)
            ]
            for word in line.split(" ")
            # if len(word)
        ]
        # to preserve lines with "/n" only, do not filter at line level
        for line in text.splitlines()
    ]


def decode(encoded, norm_form: Form = None, emoji: Emoji = Emoji.demojize):
    decoded = linesep.join(
        " ".join(
            "".join(
                bytes(char).decode("utf-8") for char in word
            )  # if len(word) else "\n"
            for word in line
        )
        for line in encoded
    )
    # return normalize("NFC", demojize(bytes(list(chain(*encoded))).decode()))
    if isinstance(norm_form, Form):
        decoded = normalize(norm_form, decoded)
    if emoji == Emoji.emojize:
        decoded = emojize(decoded)
    else:
        if emoji == Emoji.demojize:
            decoded = demojize(decoded)
    return decoded
