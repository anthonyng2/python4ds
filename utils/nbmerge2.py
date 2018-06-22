"""
usage:

python nbmerge.py A.ipynb B.ipynb C.ipynb > merged.ipynb

Name is hardcoded to test.ipynb
"""

import io
import os
import sys

import nbformat

def merge_notebooks(filenames):
    merged = None
    for fname in filenames:
        with io.open(fname, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        if merged is None:
            merged = nb
        else:
            merged.cells.extend(nb.cells)
    #merged.metadata.name += "_merged"
    print(nbformat.write(merged, 'test.ipynb', version=nbformat.current_nbformat))

if __name__ == '__main__':
    merge_notebooks(sys.argv[1:])
