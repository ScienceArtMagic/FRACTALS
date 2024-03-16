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
    """
    Encode text into 8-bit integers based on UTF-8.

    @param text - The text to encode. Must be a unicode string (including emoji).
    @param utf8_form - The form in which normalize the text (pre-encoding).
    @param emoji_form - Convert all emoji codes to emoji, or vice versa (pre-encoding, no conversion if set to None).

    @return List of nested lists of uint8 split by newlines, then spaces, then individual characters, then individual bytes.
        Multi-byte characters are grouped, single-byte represented as scalars.
    """
    # text = text.strip() ### disable to allow (multiple) preceding spaces (e.g. in code)
    text = utf8_norm_fn(emoji_fn(text, emoji_form), utf8_form)
    return [
        [
            [
                list(bytearray(char, "utf-8"))  # if ord(char) > 255 else [ord(char)]
                for char in word.strip("")
                # list containing an empty list 1 level below for repeated spaces,
                # empty list 2 levels below for repeated newlines
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
    """
    Decode/reassemble text into 8-bit integers based on UTF-8.

    @param encoded - List of nested lists of uint8 to be decoded to text.
    @param utf8_form - The form in which normalize the text (post-encoding).
    @param emoji_form - Convert all emoji codes to emoji, or vice versa (post-encoding, no conversion if set to None).

    @return The decoded (possibly normalized and/or emojized/demojized) text.
    """
    decoded = linesep.join(
        " ".join("".join(bytes(char).decode("utf-8") for char in word) for word in line)
        for line in encoded
    )
    decoded = utf8_norm_fn(decoded, utf8_form)
    decoded = emoji_fn(decoded, emoji_form)
    return decoded
