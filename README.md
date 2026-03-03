# CPC2-wrapper

> Coding Potential Calculator 2 - Python wrapper for easy installation and use

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

## Overview

CPC2-wrapper is a Python package that wraps the [CPC2 (Coding Potential Calculator 2)](http://cpc2.cbi.pku.edu.cn) algorithm for predicting the coding potential of RNA sequences. This wrapper makes installation and usage easier while maintaining all the original functionality.

**Note**: Most code is from the [original CPC2 source](http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz). This wrapper restructures the code for pip installation and easier integration.

## Features

- ✅ Predict coding potential of RNA sequences
- ✅ Calculate Fickett TESTCODE scores
- ✅ Support for gzipped input files
- ✅ Easy pip installation
- ✅ Python 3.8+ support

## Installation

### From GitHub (Recommended)

```bash
pip install git+https://github.com/loganylchen/CPC2-wrapper.git
```

### From Source

```bash
git clone https://github.com/loganylchen/CPC2-wrapper.git
cd CPC2-wrapper
pip install -e .
```

### Prerequisites

- Python 3.8 or higher
- libsvm binaries (`svm-scale` and `svm-predict`)

Install libsvm:
```bash
# Ubuntu/Debian
sudo apt-get install libsvm-tools

# macOS
brew install libsvm

# From source
wget http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz
tar -xzf CPC2-beta.tar.gz
cd CPC2-beta/libs/libsvm
make
```

## Quick Start

```bash
# Basic usage
CPC2.py -i input.fa -o output.txt

# With reverse strand analysis
CPC2.py -i input.fa -o output.txt -r

# Include ORF start position in output
CPC2.py -i input.fa -o output.txt --ORF

# Specify custom libsvm path
CPC2.py -i input.fa -o output.txt --libsvm-bin /path/to/libsvm/bin
```

## Input Format

FASTA format:
```
>sequence_1
ATGAAATAAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC
>sequence_2
ATGGGGTAA...
```

## Output Format

Tab-separated table with the following columns:

| Column | Description |
|--------|-------------|
| #ID | Sequence identifier |
| transcript_length | Length of input sequence |
| peptide_length | Length of predicted peptide |
| Fickett_score | Fickett TESTCODE score |
| pI | Isoelectric point |
| ORF_integrity | ORF completeness (1=complete, -1=incomplete) |
| coding_probability | Probability of being coding |
| label | Classification (coding/noncoding) |

Example output:
```
#ID	transcript_length	peptide_length	Fickett_score	pI	ORF_integrity	coding_probability	label
seq1	1000	333	2.45	6.5	1	0.95	coding
seq2	500	166	0.12	4.2	1	0.23	noncoding
```

## Algorithm

CPC2 uses Support Vector Machine (SVM) classification with the following features:

1. **Peptide length** - Length of the longest ORF
2. **Fickett TESTCODE score** - Position-dependent nucleotide composition
3. **Isoelectric point (pI)** - Biochemical property of the peptide
4. **ORF integrity** - Whether the ORF has proper start/stop codons

For algorithm details, see the [original CPC2 paper](https://pubmed.ncbi.nlm.nih.gov/28525517/).

## Examples

### Example 1: Analyze a single sequence

```bash
# Create test file
echo ">test
ATGAAATAA" > test.fa

# Run CPC2
CPC2.py -i test.fa -o test_output.txt

# View results
cat test_output.txt
```

### Example 2: Batch processing

```bash
# Process multiple FASTA files
for file in *.fa; do
    echo "Processing $file..."
    CPC2.py -i "$file" -o "${file%.fa}_cpc2.txt"
done
```

### Example 3: Python API

```python
from CPC2 import calculate_potential

# Analyze sequences
result = calculate_potential(
    fasta='input.fa',
    strand='+',
    output_orf=0,
    outfile='output.txt',
    libsvm_bin='/usr/local/bin/'
)
```

## Development

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/loganylchen/CPC2-wrapper.git
cd CPC2-wrapper

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install in development mode
pip install -e .[dev]
```

### Run Tests

```bash
pytest tests/ --cov=cpc2
```

### Code Quality

```bash
# Format code
black cpc2/

# Check style
flake8 cpc2/

# Type checking
mypy cpc2/
```

## Troubleshooting

### "libsvm binaries not found"

**Problem**: CPC2 can't find svm-scale or svm-predict

**Solution**:
1. Install libsvm (see Installation section)
2. Specify path explicitly: `--libsvm-bin /path/to/libsvm/bin`

### "Command injection detected"

**Problem**: File paths with special characters cause errors

**Solution**: Avoid special characters in file paths (spaces, quotes, etc.)

### Slow performance on large files

**Problem**: Processing takes too long

**Solution**:
1. Use gzipped input files (automatic detection)
2. Split large FASTA files into smaller batches
3. Consider parallel processing

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Citation

If you use CPC2 in your research, please cite:

> Kang YJ, Yang DC, Kong L, Hou M, Meng YQ, Wei L, Gao G. CPC2: a fast and accurate coding potential calculator. *Bioinformatics*. 2017;33(16):2522-2523. doi:10.1093/bioinformatics/btx244

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Original CPC2 algorithm by [CBI PKU](http://cpc2.cbi.pku.edu.cn)
- Based on work by Kang Yujian and team

## Contact

- Maintainer: CHEN Yuelong <yuelong.chen.btr@gmail.com>
- Issues: [GitHub Issues](https://github.com/loganylchen/CPC2-wrapper/issues)

---

**Original README below:**

# Raw readme


CPC2 standalone
====

* 2019-11-19 16:50, Yu-jian Kang

1 Pre-requisite:
----
a. Biopython package: a local version could be downloaded from
http://biopython.org/wiki/Download

2 Install
----
a. Unpack the tarball:

	tom@linux$ gzip -dc CPC2-beta.tar.gz | tar xf -

b. Build third-part packages: 

	tom@linux$ cd CPC2-beta
	tom@linux$ export CPC_HOME="$PWD"
	tom@linux$ cd libs/libsvm
	tom@linux$ gzip -dc libsvm-3.18.tar.gz | tar xf -
	tom@linux$ cd libsvm-3.18
	tom@linux$ make clean && make

3 Run the predict
----
	tom@linux$ cd $CPC_HOME
	tom@linux$ bin/CPC2.py -i (input_seq) -o (result_in_table)
example: tom@linux$ bin/CPC2.py -i data/example.fa -o example_output

4 Output result
----
The result is in table format (plain text delimited by tab).

Default output:<br>
#ID	transcript_length	peptide_length	Fickett_score	pI	ORF_integrity	coding_probability	label

Set '--ORF' to output the start position of longest ORF:<br>
#ID	transcript_length	peptide_length	Fickett_score	pI	ORF_integrity	ORF_Start	coding_probability	label

Contact
----
>See the website for tutorial and more details. (http://cpc2.cbi.pku.edu.cn)<br>

>This is a beta version of CPC2, if have any questions please report to us.<br>

>Contact: cpc@mail.cbi.pku.edu.cn
