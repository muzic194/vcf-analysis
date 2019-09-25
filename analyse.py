import vcf

def lines_in_vcf(filepath):   
    bashCommand = "wc -l " + filepath
    import subprocess
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    return int((output.decode("utf-8")).split()[0])
    
def headers(filepath):
    headers = 0 
    with open(filepath) as fp:
        for cnt, line in enumerate(fp):
            if line[0] == "#":
                headers += 1
            else:
                break
    return headers

def samples(filepath):
    vcf_reader = vcf.Reader(open(filepath, 'r'))
    return len(vcf_reader.samples)

def variants(filepath):
    return lines_in_vcf(filepath)-headers(filepath)


def analyse(filepath):
    print( {
        "number_of_samples": samples(filepath),
        "number_of_variants": variants(filepath)
    } )

import sys
analyse(sys.argv[1])