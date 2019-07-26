from distutils.core import setup
setup(
  name = 'pyvector',         
  packages = ['pyvector'],   
  version = '0.1',     
  license='MIT',       
  description = 'Poor c++ vector implementation for python',   
  author = 'cvsae',                  
  author_email = 'cvsc@gmx.com',     
  url = 'https://github.com/cvsar/pyvector',   
  download_url = 'https://github.com/cvsae/pyvector/archive/v_01.tar.gz',
  keywords = ['vector', 'python', 'c++', "implementation"],   
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Topic :: Software Development :: Build Tools',    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 2.7',
  ],
)