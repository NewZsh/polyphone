#!/bin/bash

if [ "$1" = "train" ]; then
    python scripts/train_g2p_bert.py \
        --config configs/config_cpp.py
elif [ "$1" = "test" ]; then
    python scripts/test_g2p_bert.py \
        --config configs/config_cpp.py \
        --checkpoint "$2/best_accuracy.pth"\
        --sent_path ../data/cpp/test.sent \
        --lb_path ../data/cpp/test.lb \
        --pos_path ../data/cpp/test.pos
else
    echo "Invalid argument. Please specify either 'train' or 'test'."
fi