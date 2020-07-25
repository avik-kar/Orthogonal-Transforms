#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python version: 3.6

import argparse


def args_parser():
    parser = argparse.ArgumentParser()

    # federated arguments (Notation for the arguments followed from paper)
    parser.add_argument('--transform', type=str,
                        choices = ['dft', 'ditfft', 'diffft', 'dct', 'dst', 'wht',
                                   'slant', 'haar', 'klt'],
                        default='DFT', help="Name of the transform.")
    parser.add_argument('--sequence', type=str, default='random', choices = ['random', 'takeinput'],
                        help="Whether the sequence will be generated or provided.")
    parser.add_argument('--roundDigit', type=int, default=4, choices = [0, 2, 4, 6, 8],
                        help="Number of digits after decimel place in output.")
    args = parser.parse_args()
    return args
