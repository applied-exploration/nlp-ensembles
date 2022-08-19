from pprint import pformat
import textwrap
import re


def pprint_indent(text, indent=" " * 4 + "┃ ") -> None:
    text = pformat(text)
    print("".join([indent + l for l in text.splitlines(True)]))


class PrintFormats:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class DocumentWrapper(textwrap.TextWrapper):
    def wrap(self, text):
        split_text = text.split("\n")
        lines = [
            line
            for para in split_text
            for line in textwrap.TextWrapper.wrap(self, para)
        ]
        return lines


def remove_ansi_escape(s: str) -> str:
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub("", s)


def multi_line_print(text: str, level: int = 0) -> None:

    base_indent = " " * 4

    if level == 0:
        initial_indent = base_indent + "┣━━━ "
        subsequent_indent = base_indent + "┃ "
    if level == 1:
        initial_indent = base_indent + "┃  ├── "
        subsequent_indent = base_indent + "┃  │   "
    if level == 2:
        initial_indent = base_indent + "┃    "
        subsequent_indent = base_indent + "┃    "

    d = DocumentWrapper(
        width=100,
        initial_indent=initial_indent,
        subsequent_indent=subsequent_indent,
    )
    print(d.fill(text))


def print_box(
    text: str, width: int = 100, height: int = 1, thickness_level: int = 0
) -> None:
    if thickness_level == 0:
        top_left = "┏"
        top_right = "┓"
        vertical = "┃"
        bottom_left = "┗"
        bottom_right = "┛"
        horizontal = "━"
        t_down = "┳"

    print(top_left + horizontal * width + top_right)
    for _ in range(height):
        print(vertical + " " * width + vertical)

    for sub_string in text.split("\n"):
        text_length = len(remove_ansi_escape(sub_string))
        whitespace_around_text = int(max(0, (width - text_length) / 2))

        print(
            vertical
            + " " * whitespace_around_text
            + sub_string
            + " " * max(0, (width - whitespace_around_text - text_length))
            + vertical
        )

    for _ in range(height):
        print(vertical + " " * width + vertical)
    print(
        bottom_left + horizontal * 3 + t_down + horizontal * (width - 4) + bottom_right
    )
