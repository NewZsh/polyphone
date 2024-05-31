# g2pW labels POS for predicting the phones, however, the POS files
# match the SENT and LB files in g2pM, which have been modified. SO,
# if the sent is removed, the corresponding pos should also be removed.

phrases = ['train', 'dev', 'test']

for phrase in phrases:
    sents1 = open('../data/cpp/%s.sent' % phrase).readlines()
    sents2 = open('../g2pm/data/%s.sent' % phrase).readlines()
    pos = open('../g2pW/cpp_dataset/%s.pos' % phrase).readlines()

    filter_pos = []
    i = 0
    for j, item in enumerate(pos):
        if sents1[i] == sents2[j]:
            i += 1
            filter_pos.append(item)
    with open('../data/cpp/%s.pos' % phrase, 'w') as f:
        for line in filter_pos:
            f.write(line)

