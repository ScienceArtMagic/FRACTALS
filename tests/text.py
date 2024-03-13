from iteration_utilities import deepflatten
from fractals.text import EMOJI, CODE, NFC, NFD, decode, encode

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

enc_d = encode(emojis, NFD, "code")
enc_e = encode(emojis, "NFKC", "emoji")

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
    decode(enc_e, None, CODE),
    "\nDecoded chars (demojized):",
    len(decode(enc_e, None, "code")),
    "\n\n",
)
print(
    decode(enc_d, NFC, EMOJI),
    "\nDecoded chars (emojized):",
    len(decode(enc_d, NFC, EMOJI)),
    "\n\n",
)
