from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PyXML',
  version='0.0.1',
  description='Python XML Parser',
  long_description=open('README.md').read(),
  long_description_content_type="text/markdown",
  url='',  
  author='Johanna Heidel',
  author_email='hdljohanna@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='xml', 
  packages=find_packages(),
  install_requires=['urllib3'] 
)
