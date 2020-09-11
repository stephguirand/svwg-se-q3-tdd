#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""An enhanced version of the 'echo' cmd line utility."""

__author__ = """
stephguirand
Help from demo, lessons and activities, youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about assignment
in study group.
"""


import sys
import argparse


def lower_case(text):
    return text.lower()


def upper_case(text):
    return text.upper()


def title_case(text):
    return text.title()


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    parser.add_argument('text', help='text to be manipulated')
    return parser


def main(args):
    """Implementation of echo"""

    parser = create_parser()
    # Run the parser to collect command line arguments into a
    # NAMESPACE called 'ns'
    ns = parser.parse_args(args)

    if not ns:
        parser.print_usage()
        exit(1)

    text = ns.text

    # option flag

    if ns.lower:
        text = lower_case(text)
    if ns.upper:
        text = upper_case(text)
    if ns.title:
        text = title_case(text)
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
