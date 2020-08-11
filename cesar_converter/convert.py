"""
Here are main operations with Cesar cipher - decode and encode
"""
import operator
import typing as ty

from . import alphabets


def encode(string: ty.Iterable[str], /, *, offset: int) -> str:
    """
    Encode `string` by Cesar cipher using `offset`
    """
    return "".join(_convert(string, offset=offset))


def decode(string: ty.Iterable[str], /, *, offset: int) -> str:
    """
    Decode `string` encoded by Cesar cipher with encoded `offset`
    """
    return "".join(_convert(string, offset=-offset))


def _convert(string: ty.Iterable[str], /, *, offset: int) -> ty.Generator[str, None, None]:
    """
    Iterate over letters in string and `alphabets.ALPHABETS`
    and than yield new letter or old letter if can't replace
    """
    for index, letter in enumerate(string):
        for alphabet in alphabets.ALPHABETS:
            if letter in alphabet:

                # Find real offset using module divide.
                # Negative offset will be negative anyway
                true_offset = offset % len(alphabet)
                if offset < 0:
                    true_offset = operator.neg(true_offset)

                # Get new letter by finding its position
                position = alphabets.ALPHABETS.index(letter)
                new_letter = alphabets.ALPHABETS[position - true_offset]

                yield new_letter

            else:
                yield letter






