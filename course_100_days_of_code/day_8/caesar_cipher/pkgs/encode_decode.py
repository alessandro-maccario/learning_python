"""_summary_"""

# create the English alphabet
alphabet = list(map(chr, range(97, 123)))


def caesar(direction: str, text: str, shift: int) -> str:
    """Caesar Cipher (Encodying/Decoding functionalities)

    Parameters
    ----------
    direction : str
        Either 'encode' or 'decode' or 'stop'
    text : str
        Text to encrypt
    shift : int
        Integer that represents the shift in the Caesar Cypher


    Returns
    -------
    str
        Encoded/decoded string
    """
    # empty list to store the caesar/original result
    word_list = []
    # to cover those cases in which the shift is too big, we can use the modulo operator
    # Why? If the shift entered by the user is equal to 150, with the modulo, we are
    # asking for the amount of time 26 is fitting, without remainders into the shift.
    # This value will be used to shift the letters.
    shift = shift % 26

    for char in text:
        # if char is an empty space or a number, break and keep it as it is
        if char not in alphabet:
            char = char
            word_list.append(char)
            continue
        else:
            # get the chr corresponding character underneath the entered one
            char = ord(char)  # e.g.: t -> 116

        # ENCODING
        if direction == "encode":
            char_shift = char + shift  # e.g.: 116 + shift(2) = 118
            # if > 122, we have to go forward in the lower alphabetic chr system
            if char_shift > 122:
                char_shift -= len(alphabet)

        # DECODING
        elif direction == "decode":
            char_shift = char - shift  # e.g.: 116 + shift(2) = 118
            # if < 97, we have to go back in the higher alphabetic chr system
            if char_shift < 97:
                char_shift += len(alphabet)

        unicode_char = chr(char_shift)  # e.g.: 118 -> v
        word_list.append(unicode_char)

    return f"The {direction} word is: {"".join(word_list)}."
