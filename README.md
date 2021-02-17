# Genbank Converter

A way to convert your genbank file to a *.fna, *.rnt, or *.ptt file formats.

  - Scrapes your genbank file of protein / RNA records. 
  - Creates a 9 column tab delimited file ready for Rockhopper.
  - Convert your genbank to a FASTA-like file format (*.fna).
  - Perfect for Rockhopper inputs


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
#### Genbank(*.gb) to FASTA Format DNA (*.fna)
```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED)
$ python genbank_converter.py -i Mycoplasma_genitalium.gb -o Mycoplasma_SEQ -t fna
```
#### Genbank(*.gb) to NCBI Protein Table (*.ptt)
```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED)
$ python genbank_converter.py -i Mycoplasma_genitalium.gb -o Mycoplasma_Proteins -t ptt
```
#### Genbank(*.gb) to NCBI RNA Table (*.rnt)
```sh
$ cd ($PATH TO FOLDER WHERE YOU DOWNLOADED)
$ python genbank_converter.py -i Mycoplasma_genitalium.gb -o Mycoplasma_RNAS -t rtt
```

