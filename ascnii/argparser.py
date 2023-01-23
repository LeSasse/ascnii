"""Provide arg parsing functionality for ascnii package."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

from argparse import ArgumentParser
from pathlib import Path

def parse_args():
    """Parse ascnii arguments."""
    parser = argparse.ArgumentParser(
        description=(
            "View NIfTI images in terminal using ASCII characters."
        )
    )
    parser.add_argument(
        "nifti", Path, help="Path to the NIfTI file."
    )