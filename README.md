# NOTED

This is a wrapper of CPC2 algorithm. Download from original source, [http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz](http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz), 
 would be perfect. 
 
This wrapper is just for myself easy use.

Almost whole codes were from [http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz](http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz). 
I just modified the structure and install setup.py for myself easier use.

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
