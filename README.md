# LanzaTech Genbank Converter

[![N|Solid](http://www.lanzatech.com/wp-content/uploads/2014/05/LanzaTech-Logo-Final-a.png)](http://www.lanzatech.com/)

A way to convert your genbank file to an *.rnt or *.ptt file format.

  - Scrapes your genbank file of protein / RNA records. 
  - Creates a 9 column tab delimited file ready for Rockhopper.
  - Easy to use command line tool.


### Installation

This program requires [Python3](https://www.python.org/downloads/) to run.

Open the folder and install the dependencies.

```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED) 
$ pip install -r requirements.txt
```
### Running The Program
There are a few flags to keep in mind before running the program from console .
  - -i or --input (Specify the name of your genbank file that you would like to convert. Remember to include file extension.) 
  - -o or --output (Specify the name of the file that you would like to be created. Omit the file extension.)
  - -t or --type (Specify "rnt" or "ptt" for the type of genbank conversion that you would like to happen.)
```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED)
$ python genbank_converter.py -i Mycoplasma_genitalium.gb -o Mycoplasma_Proteins -t ptt
```
```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED)
$ python genbank_converter.py -i Mycoplasma_genitalium.gb -o Mycoplasma_RNAS -t rtt
```

