#!/usr/bin/env python
""" Make link for given notebook
"""

import sys
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from oktools.cutils import proc_config, build_url


HERE = Path(__file__).parent.resolve()
SITE_ROOT = (HERE / '..').resolve()
sys.path.append(str(HERE))


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('nb_fname',
                        help='Notebook filename')
    parser.add_argument('--site-config',
                        help='Path to configuration file for course '
                        '(default finds {course,_config}.yml, in dir, parents)'
                       )
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    nb_dir = Path(args.nb_fname).parent.resolve()
    site_dict, out_path = proc_config(nb_dir, args.site_config, None)
    print(build_url(args.nb_fname, site_dict))


if __name__ == '__main__':
    main()
