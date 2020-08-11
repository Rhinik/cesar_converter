"""
Creates any alphabets and add its into available
"""
import string
import typing as ty


ALPHABETS: ty.List[str] = []
"""
Available alphabets for ciphering
"""


def add_alphabet(alphabet_lower: str, /) -> None:
    """
    Get lowercase alphabet and add it into available alphabets
    with uppercase alphabet
    """
    ALPHABETS.extend([
        alphabet_lower, alphabet_lower.upper()
    ])


def generate_alphabet(
    first_letter: str,
    last_letter: str, /, *,
    extra_letters: ty.List[ty.Tuple[str, int]] = None,
) -> str:
    """
    Generate alphabet string using all letters in range
    `first_letter` and `last_letter` unicode value.
    If your alphabet has values that don't located in symbols range,
    you can pass it into `extra_letters`: the first element of tuple
    is the letter and the second is the position (starts at 1)
    """
    # Convert letters to their encoding number
    first_letter: int = ord(first_letter)
    last_letter: int = ord(last_letter)

    # Create alphabet-list with these letters
    alphabet: ty.List[str] = [
        chr(letter) for letter in range(first_letter, last_letter + 1)
    ]

    # Insert extra letters to alphabet
    if extra_letters is not None:
        for letter, position in extra_letters:
            alphabet.insert(position - 1, letter)

    alphabet: str = "".join(alphabet)

    return alphabet


# Push available alphabets list
add_alphabet(string.ascii_lowercase)  # English
add_alphabet(generate_alphabet("а", "я", extra_letters=[("ё", 7)]))  # Russian
