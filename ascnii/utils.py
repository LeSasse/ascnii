"""Provide utility functions for ascnii."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

from pathlib import Path

import ascii_magic


def get_background_color(color_string):
    """Get background color object for ascii_magic from string."""
    colors = {
        "black": ascii_magic.Back.BLACK,
        "red": ascii_magic.Back.RED,
        "green": ascii_magic.Back.GREEN,
        "yellow": ascii_magic.Back.YELLOW,
        "blue": ascii_magic.Back.BLUE,
        "magenta": ascii_magic.Back.MAGENTA,
        "cyan": ascii_magic.Back.CYAN,
        "white": ascii_magic.Back.WHITE,
    }

    return colors[color_string]


def to_terminal(placeholder, art):
    """Wrap printing art to terminal."""
    return ascii_magic.to_terminal(art)


def get_output_type(filepath):
    """Infer the output filetype from the path."""
    if filepath == "terminal":
        return filepath

    return Path(filepath).suffix


def get_input_params(output_type):
    """Get the correct params for ascii magic depending on output type."""
    params = {
        "terminal": {
            "mode": ascii_magic.Modes.TERMINAL,
        },
        ".txt": {
            "mode": ascii_magic.Modes.TERMINAL,
        },
        ".html": {
            "mode": ascii_magic.Modes.HTML,
        },
    }
    return params[output_type]


def get_output_function(output_string):
    """Get the correct function for each output type."""
    output_functions = {
        "terminal": to_terminal,
        ".html": ascii_magic.to_html_file,
        ".txt": ascii_magic.to_file,
    }

    if output_string not in output_functions.keys():
        raise ValueError(
            f"{output_string} is not an accepted output file type."
            f"Accepted file types are any of: {output_functions.keys()}!"
        )

    return output_functions[output_string]
