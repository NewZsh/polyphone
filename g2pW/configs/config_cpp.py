root = '../data/'
CPP = root + 'cpp/'
CVTE = root + 'CVTE-poly/'

manual_seed = 1313
model_source = 'bert-base-chinese'
polyphonic_chars_path = root + 'POLYPHONIC_CHARS.txt'
window_size = 32
num_workers = 1
use_mask = True
use_conditional = True
param_conditional = {
    'bias': True,
    'char-linear': True,
    'pos-linear': False,
    'char+pos-second': True,
}

# for training
exp_name = 'CPP_BERT_M_DescWS-Sec-cLin-B_POSw01'
train_sent_path_cpp = root + CPP + 'train.sent'
train_lb_path_cpp = root + CPP + 'train.lb'
train_pos_path_cpp = root + CPP + 'train.pos'
valid_sent_path = root + CPP + 'dev.sent'
valid_lb_path = root + CPP + 'dev.lb'
valid_pos_path = root + CPP + 'dev.pos'
test_sent_path = root + CPP + 'test.sent'
test_lb_path = root + CPP + 'test.lb'
test_pos_path = root + CPP + 'test.pos'
train_sent_path_cvte = root + CVTE + 'train.sent'
train_lb_path_cvte = root + CVTE + 'train.lb'
train_pos_path_cvte = root + CVTE + 'train.pos'
with_cvte = False
batch_size = 256
lr = 5e-5
val_interval = 200
num_iter = 10000
use_pos = True
param_pos = {
    'weight': 0.1,
    'pos_joint_training': True,
}
