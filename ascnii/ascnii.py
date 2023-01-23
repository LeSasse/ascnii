"""View brain images in terminal using ASCII characters."""

# Authors: Leonard Sasse <l.sasse@fz-juelich.de>
# License: AGPL

from .args import parse_args

def main():
    
    args = parse_args()
    print(args.nifti) 