# -*- encoding: utf-8 -*-
'''
@File    :   POStagging.py
@Time    :   2024/06/09 21:32:03
@Author  :   zhangsiheng 
@Version :   1.0
@Contact :   zhangsiheng@cvte.com
@Desc    :   None
'''

import tqdm
import os
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER

ANCHOR_CHAR = '▁'

# data_utils.download_data_gdown("/dataset/zhangsiheng/ckiptagger/data") # gdrive-ckip

batch_size = 1024

ws_model = WS("/dataset/zhangsiheng/ckiptagger/data")
pos_model = POS("/dataset/zhangsiheng/ckiptagger/data")

sent_file = './CVTE-poly/train.sent'
pos_file = './CVTE-poly/train.pos'

# sent_file = './cpp/test.sent'
# pos_file = './cpp/test.pos'

if os.path.exists(pos_file):
    pos_lines = open(pos_file).readlines()
else:
    pos_lines = []
sent_lines = open(sent_file).readlines()

POS_TAGS = ['A', 'C', 'D', 'I', 'N', 'P', 'T', 'V']

new_pos_lines = []
print(f'start from {len(pos_lines)}')
for i in tqdm.tqdm(range(len(pos_lines), len(sent_lines), batch_size)):
    sents = []
    idxs = []
    for j in range(i, min(i + batch_size, len(sent_lines))):
        sent = sent_lines[j].strip()
        idx = []
        cnt = 0
        sig = 0
        for j, char in enumerate(sent):
            if char == ANCHOR_CHAR and sig == 0:
                idx.append(j - 2 * cnt)
                cnt += 1
                sig = 1
            elif char == ANCHOR_CHAR and sig == 1:
                sig = 0
        idxs.append(idx)
        sents.append(sent.replace(ANCHOR_CHAR, ''))

    word_sent_list = ws_model(sents)
    pos_sent_list = pos_model(word_sent_list)

    for j in range(len(pos_sent_list)):
        pos_labels = []
        for word, pos in zip(word_sent_list[j], pos_sent_list[j]):
            pos_labels.extend([pos] * len(word))
        
        new_pos_line = []
        for k in idxs[j]:
            pos_label = pos_labels[k]
            if pos_label == 'DE' or pos_label == 'SHI':
                new_pos_line.append(pos_label)
            elif pos_label[0] in POS_TAGS:
                new_pos_line.append(pos_label[0])
            else:
                new_pos_line.append('UNK')
        
        new_pos_lines.append(new_pos_line)
    
    if i + batch_size != len(new_pos_lines):
        print(i, len(new_pos_lines))

if os.path.exists(pos_file):
    f = open(pos_file, 'a')
else:
    f = open(pos_file, 'w')

for line in new_pos_lines:
    f.write('\t'.join(line) + '\n')
f.close()