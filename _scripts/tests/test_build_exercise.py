# Test for build_exercise utilities

import os.path as op
import sys
import shutil
from zipfile import ZipFile

import jupytext

HERE = op.realpath(op.dirname(__file__))
sys.path.append(op.join(HERE, '..'))
DATA_DIR = op.join(HERE, 'data')
THREE_GIRLS = op.join(DATA_DIR, 'three_girls')


from tempfile import TemporaryDirectory

from cutils import (process_write_nb, HTML_COMMENT_RE, clear_md_comments)


def test_smoke():
    base_nb_root = 'three_girls_template'
    with TemporaryDirectory() as tmpdir:
        tmp_3g = op.join(tmpdir, 'three_girls')
        shutil.copytree(THREE_GIRLS, tmp_3g)
        tmp_nb_in = op.join(tmp_3g, base_nb_root + '.Rmd')
        tmp_nb_out = op.join(tmp_3g, base_nb_root + '.ipynb')
        assert op.isfile(tmp_nb_in)
        assert not op.isfile(tmp_nb_out)
        process_write_nb(tmp_nb_in)
        assert op.isfile(tmp_nb_out)


def test_comment_strip():
    base_nb_root = 'three_girls_template'
    nb_in_fname = op.join(THREE_GIRLS, base_nb_root + '.Rmd')
    nb = jupytext.read(nb_in_fname)
    json = jupytext.writes(nb, fmt='ipynb')
    assert len(HTML_COMMENT_RE.findall(json)) == 4
    clear_nb = clear_md_comments(nb)
    json = jupytext.writes(clear_nb, fmt='ipynb')
    assert len(HTML_COMMENT_RE.findall(json)) == 0
