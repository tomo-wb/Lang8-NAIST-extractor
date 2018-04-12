import codecs
import platform
import sys

assert platform.python_version_tuple()[0] == '3', 'This program supports only python3'
filename = sys.argv[1]
with codecs.open(filename, 'r', encoding='utf8') as f:
    for line in f:
        line = line.rstrip()
        cols = line.split('\t')
        if len(cols) > 4:
            orig = cols[4]
            corr = cols[4]
        if len(cols) > 5:
            corr = cols[5]
        output = orig + "\t" + corr
        print(output)