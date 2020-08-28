from setuptools import setup

scripts=['CPC2.py']

setup(
    name='CPC2-wrapper',
    version='0.1.0',
    packages=['cpc2'],
    url='',

    license='GPL V3',
    author='CHEN Yuelong',
    author_email='yuelong.chen.btr@gmail.com',
    description='''
This is a wrapper of CPC2 algorithm. Download from original source, [http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz](http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz), 
 would be perfect. 
 
This wrapper is just for myself easy use.

Almost whole codes were from [http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz](http://cpc2.cbi.pku.edu.cn/data/CPC2-beta.tar.gz). 
I just modified the structure and install setup.py for myself easier use.
    
    '''
)
