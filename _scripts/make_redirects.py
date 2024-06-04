#!/usr/bin/env python
""" Write redirects
"""

import os
from pathlib import Path
import sys
from argparse import ArgumentParser

import yaml

from oktools.cutils import find_site_config


HERE = Path(__file__).parent.resolve()
SITE_ROOT = (HERE / '..').resolve()
sys.path.append(str(HERE))



def write_redirect(source, target, out_dir):
    redirect_fname = out_dir / f'{source}.html'
    fname_dir = redirect_fname.parent
    if not fname_dir.is_dir():
        fname_dir.mkdir()
    redirect_fname.write_text(
            """<meta http-equiv="Refresh" content="0; """
            f"""url='{target}.html'" />""")


def main():
    parser = ArgumentParser()
    parser.add_argument('--site-config',
                        help='Path to configuration file for course '
                        '(default finds _config.yml, in dir, parents)'
                       )
    args = parser.parse_args()
    site_config = args.site_config
    if site_config is None:
       site_config = find_site_config(os.getcwd(), filenames=('_config.yml',))
    with open(site_config, 'r') as ff:
        site_dict = yaml.load(ff.read(), Loader=yaml.SafeLoader)
    redirection = site_dict.get('redirection', {})
    out_dir = redirection['builddir']
    redirects = redirection['redirects']
    if redirects is not None:
        for source, target in redirects.items():
            write_redirect(source, target, out_dir)


if __name__ == '__main__':
    main()
