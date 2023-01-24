"""Provide arg parsing functionality for ascnii package."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

import os
from argparse import ArgumentParser
from pathlib import Path


def parse_args():
    """Parse ascnii arguments."""
    columns, _ = os.get_terminal_size()
    background_colors = [
        "black",
        "red",
        "red",
        "green",
        "yellow",
        "blue",
        "magenta",
        "cyan",
        "white",
    ]
    parser = ArgumentParser(
        description=("View NIfTI images in terminal using ASCII characters.")
    )

    parser.add_argument("nifti", type=Path, help="Path to the NIfTI file.")

    parser.add_argument(
        "-o",
        "--output",
        default="terminal",
        type=str,
        help=(
            "How to output the brain image. By default, prints to"
            " {'terminal'}. Otherwise, accepts a path to a html file"
            " or a txt file."
        ),
    )

    parser.add_argument(
        "-H",
        "--header",
        action="store_true",
        help="If activated, print out the image header as well.",
    )

    parser.add_argument(
        "-C",
        "--columns",
        default=columns,
        type=int,
        help="Number of character columns (in terminal) to use for plotting.",
    )

    parser.add_argument(
        "-c",
        "--colorbar",
        action="store_true",
        help="If activated, a colorbar is plotted with the brain images.",
    )

    parser.add_argument(
        "-m",
        "--colormap",
        default="viridis",
        type=str,
        help="Choose a colormap for the image.",
    )

    parser.add_argument(
        "-b",
        "--background",
        default="black",
        choices=background_colors,
        type=str,
        help="Choose a terminal color for the background.",
    )

    parser.add_argument(
        "-t",
        "--threshold",
        default=0.1,
        type=float,
        help="Threshold the given image below this value.",
    )

    parser.add_argument(
        "-cc",
        "--cut_coords",
        default=[-10, 0, 0],
        type=int,
        nargs=3,
        help="MNI coordinates at which to plot the image.",
    )

    parser.add_argument(
        "-a",
        "--annotate",
        action="store_true",
        help="If activated, positions and left/right annotation are added.",
    )

    parser.add_argument(
        "-d",
        "--draw_cross",
        action="store_true",
        help=(
            "If activated, a cross is drawn on the"
            " plot to indicate the cut position."
        ),
    )

    return parser.parse_args()
