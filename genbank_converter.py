from __future__ import print_function
import argparse
import bio_util
import sys
import os

args = argparse.Namespace


def count(myco, type):
    counter = 0
    if type == 'ptt' or type == "PTT":
        for count in myco.features:
            if count.type == 'CDS':
                counter += 1
            else:
                continue
    else:
        for count in myco.features:
            if count.type == 'rRNA' or count.type == 'tRNA':
                counter += 1
            else:
                continue
    return counter


def write(myco, f, type):
    f.write("Location\tStrand\tLength\tPID\tGene\tSynonym\tCode\tCOG\tProduct\n")
    if type == 'protein':
        for x in myco.features:
            if x.type == 'CDS':
                if x.strand == 1:
                    strand = '+'
                else:
                    strand = '-'
                f.write("{}..{}\t{}\t{}\t{}\t{}\t-\t-\t-\t{}\n".format(x.location._start, x.location._end, strand,x.location._end - x.location._start,x.qualifiers.get('locus_tag')[0],x.qualifiers.get('locus_tag')[0],x.qualifiers.get('product')[0]))
            else:
                continue
    else:
        for x in myco.features:
            if x.type == 'rRNA' or x.type == 'tRNA':
                if x.strand == 1:
                    strand = '+'
                else:
                    strand = '-'
                f.write("{}..{}\t{}\t{}\t{}\t{}\t-\t-\t-\t{}\n".format(x.location._start, x.location._end, strand,x.location._end - x.location._start,x.qualifiers.get('locus_tag')[0],x.qualifiers.get('locus_tag')[0],x.qualifiers.get('product')[0]))
            else:
                continue


def main():
    genbank_file = bio_util.load_references(args.input_filename)
    myco = genbank_file[0]
    protein_or_rna_count = count(myco,args.conversion_type)
    if args.conversion_type == 'ptt' or args.conversion_type == 'PTT':
        f = open('{}.ptt'.format(args.output_filename), 'w')
        f.write("{} - {}..{}\n".format(myco.description, myco.features[0].location._start, myco.features[0].location._end))
        f.write("{} proteins\n".format(protein_or_rna_count))
        write(myco, f, 'protein')
        f.close()
        print("File created at: {}".format(os.path.realpath("{}.ptt".format(args.output_filename))))
    elif args.conversion_type == 'rnt' or args.conversion_type == 'RNT':
        f = open('{}.rnt'.format(args.output_filename), 'w')
        f.write("{} - {}..{}\n".format(myco.description, myco.features[0].location._start, myco.features[0].location._end))
        f.write("{} rnas\n".format(protein_or_rna_count))
        write(myco, f, 'rna')
        f.close()
        print("File created at: {}".format(os.path.realpath("{}.rnt".format(args.output_filename))))
    else:
        print("You have entered an invalid file extension for the output file that you want to convert.")
        sys.exit(0)
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser._action_groups.pop()
    required = parser.add_argument_group('Required Arguments')
    required.add_argument('--input', '-i', dest="input_filename", type=str, required=True, help="Please specify which file you want to convert.")
    required.add_argument('--output', '-o', dest="output_filename", type=str, required=True, help="Please specify desired output file name.")
    required.add_argument('--type', '-t', dest="conversion_type", type=str, required=True, help="Please specify if you want to convert your genbank file to a *.ptt file or a *.rnt file.")
    parser.parse_args(namespace=args)
    sys.exit(main())
