from ckiptagger import WS, POS
# import opencc
from tqdm import tqdm
import numpy as np

ANCHOR_CHAR = '▁'
# converter = opencc.OpenCC('s2t.json')

root = '../data/CVTE-poly'
phrase = 'train'
path = f'{root}/{phrase}.sent'
out_path = f'{root}/{phrase}.pos'

lines = open(path).read().strip().split('\n')
sentence_list = [line.replace(ANCHOR_CHAR, '') for line in lines]
position_list = []
for line in lines:
    position = []
    while line.count(ANCHOR_CHAR) > 0:
        idx = line.index(ANCHOR_CHAR)
        position.append(idx)
        if idx + 3 < len(line):
            line = line[:idx] + line[idx+1] + line[idx+3:]
        else:
            line = line[:idx] + line[idx+1]
    position_list.append(position)

mapping = {
    'A': 'A',
    'Caa': 'C', 'Cab': 'C', 'Cba': 'C', 'Cbb': 'C',
    'D': 'D', 'Da': 'D', 'Dfa': 'D', 'Dfb': 'D', 'Di': 'D', 'Dk': 'D', 'DM': 'D',
    'I': 'I',
    'Na': 'N', 'Nb': 'N', 'Nc': 'N', 'Ncd': 'N', 'Nd': 'N', 'Nep': 'N', 'Neqa': 'N', 'Neqb': 'N', 'Nes': 'N', 'Neu': 'N', 'Nf': 'N', 'Ng': 'N', 'Nh': 'N', 'Nv': 'N',
    'P': 'P',
    'T': 'T',
    'VA': 'V', 'VAC': 'V', 'VB': 'V', 'VC': 'V', 'VCL': 'V', 'VD': 'V', 'VF': 'V', 'VE': 'V', 'VG': 'V', 'VH': 'V', 'VHC': 'V', 'VI': 'V', 'VJ': 'V', 'VK': 'V', 'VL': 'V', 'V_2': 'V',
    'DE': 'DE',
    'SHI': 'SHI',
}
# map to: ['A', 'C', 'D', 'I', 'N', 'P', 'T', 'V', 'DE', 'SHI']

CKIP_DATA = './data/'
ws = WS(CKIP_DATA)
pos = POS(CKIP_DATA)
batch_size = 2048

fw = open(out_path, 'w', buffering=batch_size)

i = 0

for _ in tqdm(list(range(int(np.ceil(len(lines)/batch_size))))):
    j = min(len(lines), i+batch_size)
    sentences = [sent for sent in sentence_list[i:j]]
    positions = position_list[i:j]

    word_sentence_list = ws(sentences)
    pos_sentence_list = pos(word_sentence_list)

    annotations = []
    for position, sentence, words, tags in zip(positions, sentences, word_sentence_list, pos_sentence_list):
        annotation = []
        start = 0
        k = 0
        for word, tag in zip(words, tags):
            for x in range(len(word)):
                if start + x == position[k]:
                    annotation.append(mapping.get(tag, 'UNK'))
                    k += 1
                    if k == len(position):
                        break
            start += len(word)
            if k == len(position):
                break
        annotations.append('\t'.join(annotation))

    if i > 0:
        fw.write('\n')
    fw.write('\n'.join(annotations))
    i = j

fw.close()
