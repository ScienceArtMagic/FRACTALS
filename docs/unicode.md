(Big Endian)
Binary format of bytes in sequence

1st Byte | 2nd Byte | 3rd Byte | 4th Byte | Number of Free Bits | Maximum Expressible Unicode Value
---------|----------|----------|----------|-------------:|:----------------------------------:
0xxxxxxx | | | | 7 | 007F hex (127)
110xxxxx | 10xxxxxx | | | (5+6)=11 | 07FF hex (2047)
1110xxxx | 10xxxxxx | 10xxxxxx | | (4+6+6)=16 | FFFF hex (65535)
11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx | (3+6+6+6)=21 | 10FFFF hex (1,114,111)

The value of each individual byte indicates its UTF-8 function, as follows:

00 to 7F hex (0 to 127): first and only byte of a sequence.
80 to BF hex (128 to 191): continuing byte in a multi-byte sequence.
C2 to DF hex (194 to 223): first byte of a two-byte sequence.
E0 to EF hex (224 to 239): first byte of a three-byte sequence.
F0 to FF hex (240 to 255): first byte of a four-byte sequence.

(source: <https://www.fileformat.info/info/unicode/utf8.htm>)
