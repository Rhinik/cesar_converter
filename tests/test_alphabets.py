import string
import typing as ty

import cesar_converter.alphabets
import pytest


@pytest.mark.parametrize(
    "first_letter,last_letter,extra_letters, output",
    [
        ("a", "z", [], string.ascii_lowercase),
        ("а", "я", [("ё", 7)], "абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    ]
)
def test_generate_alphabet(
    first_letter: str,
    last_letter: str,
    extra_letters: ty.List[ty.Tuple[str, int]],
    output: str
):
    assert cesar_converter.alphabets.generate_alphabet(
        first_letter, last_letter, extra_letters=extra_letters
    ) == output


def test_add_alphabet():
    cesar_converter.alphabets.add_alphabet(string.ascii_lowercase)
    assert len({
        *cesar_converter.alphabets.ALPHABETS[-2:]
    } - {
        string.ascii_lowercase, string.ascii_uppercase
    }) == 0
