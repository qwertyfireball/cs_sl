from typing import List, Tuple


def string_frequencies(value: str) -> List[Tuple[str, int]]:
    """Creates a list of tuples containing the frequency of each unique character in a string
        e.g.
        string_frequencies('www.google.com') =>
            [('w', 3), ('.', 2), ('g', 2), ('o', 3), ('l', 1), ('e', 1), ('c', 1), ('m', 1)]


    Returns:
        List: List of tuples in the form of (character, frequency)
    """
    result = []
    seen = ""
    for c in value:
        if c not in seen:
            freq = value.count(c)
            result.append((c, freq))
            seen = seen + c
    return result


def string_wrapper(value: str, wrapper: str) -> str:
    half = len(wrapper) // 2
    first_half = wrapper[:half]
    second_half = wrapper[half:]
    return first_half + value + second_half


def locale_number(number: int, interval: int = 3, sep: str = ",") -> str:
    """Returns a number string with separators at a localized interval

    e.g.
        locale_number(123456789, 3, ",") => "123,456,789"
        locale_number(123456789, 4, ",") => "1,2345,6789"
        locale_number(12345, 3, ".") => "123.456.789"

    Args:
        number (int): an integer
        spacing (int, optional): spacing between separators. Defaults to 3.
        sep (str, optional): type of separator. Defaults to ",".

    Returns:
        str: a localized number string
    """
    snum = str(number)
    last = len(snum) - interval
    while last > 0:
        snum = snum[:last] + "," + snum[last:]
        last -= interval
    return snum


def move_spaces(value: str) -> str:
    space_count = value.count(" ")
    text_without_space = value.replace(" ", "")
    return " " * space_count + text_without_space


def str_sum(value: str) -> int:
    digits = [int(char) for char in value if char.isdigit()]
    result = sum(digits)

    return result


def balanced(value: str, open: str = "(", close: str = ")") -> bool:
    """Determines if a string has a balanced set of brackets

    e.g. balanced("(())") => True
         balanced(")(())(") => False
         balanced("((())") => False
         balanced("(()))(()") => False


    Args:
        value (str): A string containing opening and closing elements as well as other characters
        open (str, optional): an opening symbol. Defaults to "(".
        close (str, optional): a closing symbol. Defaults to ")".

    Returns:
        bool: True if balanced, False otherwise
    """
    seen_open = False
    seen_close = False
    for char in value:
        if char == open:
            if seen_close == True:
                return False
        elif char == close:
            seen_close = True
    else:
        return True


import unittest


def _message(result: any, expected: any, *args) -> str:  # type: ignore
    s = f"\nExpected {expected}\nReceived {result}"
    if args:
        s += f"\nInputs: {args}"
    return s


class Tests(unittest.TestCase):
    def test_string_frequencies(self):
        value = "www.google.com"
        result = string_frequencies(value)
        expected = [
            ("w", 3),
            (".", 2),
            ("g", 2),
            ("o", 3),
            ("l", 1),
            ("e", 1),
            ("c", 1),
            ("m", 1),
        ]

        result.sort(key=lambda t: t[0])
        expected.sort(key=lambda t: t[0])
        self.assertListEqual(result, expected, _message(result, expected))

        value = "tttttteeeeessssttt"
        result = string_frequencies(value)
        expected = [("t", 9), ("e", 5), ("s", 4)]
        result.sort(key=lambda t: t[0])
        expected.sort(key=lambda t: t[0])
        self.assertListEqual(result, expected, _message(result, expected))

    def test_string_wrapper(self):
        value = "wrapme"
        wrapper = "(())"
        expected = "((wrapme))"
        result = string_wrapper(value, wrapper)
        self.assertEqual(result, expected, _message(result, expected))
        wrapper = "|||"
        expected = "|wrapme||"
        result = string_wrapper(value, wrapper)
        self.assertEqual(result, expected, _message(result, expected))
        wrapper = "abcdef"
        expected = "abcwrapmedef"
        result = string_wrapper(value, wrapper)
        self.assertEqual(result, expected, _message(result, expected))

    def test_locale_number(self):
        value = 123456789
        interval = 3
        sep = ","
        expected = "123,456,789"
        result = locale_number(value, interval, sep)
        self.assertEqual(result, expected, _message(result, expected))
        interval = 4
        expected = "1,2345,6789"
        result = locale_number(value, interval, sep)
        self.assertEqual(result, expected, _message(result, expected))
        value = 123
        expected = "123"
        interval = 3
        result = locale_number(value, interval, sep)
        self.assertEqual(result, expected, _message(result, expected))

    def test_move_spaces(self):
        value = "I'm a sentence"
        expected = "  I'masentence"
        result = move_spaces(value)
        self.assertEqual(result, expected, _message(result, expected))
        value = "I   have   a   lot   of   spaces"
        expected = "               Ihavealotofspaces"
        result = move_spaces(value)
        self.assertEqual(result, expected, _message(result, expected))

    def test_str_sum(self):
        value = "12a45b89"
        expected = 29
        result = str_sum(value)
        self.assertEqual(result, expected, _message(result, expected))

        value = "abcdefg"
        expected = 0
        result = str_sum(value)
        self.assertEqual(result, expected, _message(result, expected))

        value = "1abcdefg1hijklmn1opqrstuv1wxyz"
        expected = 4
        result = str_sum(value)
        self.assertEqual(result, expected, _message(result, expected))

    def test_balanced(self):
        value = "(())"
        expected = True
        result = balanced(value)
        self.assertTrue(result, _message(result, expected, value))

        value = ")((((((("
        expected = False
        result = balanced(value)
        self.assertFalse(result, _message(result, expected, value))

        value = "(()()((())()()))"
        expected = True
        result = balanced(value)
        self.assertTrue(result, _message(result, expected, value))

        value = "())(()"
        expected = False
        result = balanced(value)
        self.assertFalse(result, _message(result, expected, value))


if __name__ == "__main__":
    # unittest.main()
    # result = locale_number(12345678)
    # print(result)

    result = string_wrapper("eiwof", "xxxx")
    print(result)
