import pickle
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--filepath', type=str)
args = parser.parse_args()

with open(args.filepath, 'rb') as f:
    data = pickle.load(f)

data = sorted(data.items(), key = lambda x: len(x[1]), reverse = True)
with open('./phones.csv', 'w') as f:
    for char, phones in data:
        f.write('%s' % char)
        for phone in phones:
            f.write(',%s' % phone)
        f.write('\n')

# for g2pw
with open('../data/cpp/POLYPHONIC_CHARS.txt', 'w') as f:
    for char, phones in data:
        for phone in phones:
            f.write('%s\t%s\n' % (char, phone))

