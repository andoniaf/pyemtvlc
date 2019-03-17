import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

     name='dokr',  

     version='0.1',

     scripts=['pyemtvlc'] ,

     author="Andoni Alonso F.",

     author_email="andonialonsof@gmail.com",

     description="Python package to query  EMT Valencia (bus).",

     long_description=long_description,

     long_description_content_type="text/markdown",

     url="https://github.com/andoniaf/pyemtvlc",

     packages=setuptools.find_packages(),

     classifiers=[

         "Programming Language :: Python :: 3",

         "License :: OSI Approved :: GPL-3.0",

         "Operating System :: OS Independent",

     ],

 )
