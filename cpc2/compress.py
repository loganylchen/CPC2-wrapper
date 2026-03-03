'''
This module deals with compressed file (.gz or .bz2)
'''

import gzip
import bz2
import sys


def gz_file(fq_file, mode, level=6):
    try:
        if fq_file.endswith("gz"):
            fq_fp = gzip.open(fq_file, mode + "b", level)
        else:
            sys.stderr.write(f"[INFO] read file '{fq_file}'\n")
            fq_fp = open(fq_file, mode)
    except (IOError, OSError) as e:
        sys.stderr.write(f"Error: Fail to IO file: {fq_file}: {e}\n")
        sys.exit(1)
    return fq_fp


def bz2file(f):
    if f.endswith("bz2"):
        fz = bz2.BZ2File(f)
        return fz
    else:
        sys.stderr.write(f"Error: File is not bz2 compressed: {f}\n")
        sys.exit(1)
