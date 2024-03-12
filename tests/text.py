from iteration_utilities import deepflatten
from fractals.text import Emoji, Form, decode, encode

emojis = """
    :sparkles: feat: Now emoji-safe! ✅🔥:pile_of_poo:😊😂⭐💀🎉
Spaces

and

Newlines also work!
  :male_sign::female_sign::transgender_symbol:
📦package
┣ 📂dir1
┃ ┗ 📂subdir
┗ 📜file1
🫱🏿‍🫲🏾\n
:smiling_face_with_horns::mushroom::sign_of_the_horns::broccoli:💨
"""

enc_d = encode(emojis, Form.NFD, Emoji.demojize)
enc_e = encode(emojis, Form.NFD, Emoji.emojize)

print(
    enc_d,
    "\nEncoded bytes (demojized, unrolled for count):",
    len(list(deepflatten(enc_d))),
    "\n\n",
)
print(
    enc_e,
    "\nEncoded bytes (emojized, unrolled for count):",
    len(list(deepflatten(enc_e))),
    "\n\n",
)
print(
    decode(enc_e, None, Emoji.demojize),
    "\nDecoded chars (demojized):",
    len(decode(enc_e, None, Emoji.demojize)),
    "\n\n",
)
print(
    decode(enc_d, Form.NFC, Emoji.emojize),
    "\nDecoded chars (emojized):",
    len(decode(enc_d, Form.NFC, Emoji.emojize)),
    "\n\n",
)
