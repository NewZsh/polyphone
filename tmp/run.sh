if [ "$1" = "test" ]; then
    python scripts/test_g2p_bert.py \
        --config "$2/config.py" \
	--checkpoint "$2/best_accuracy.pth" \
    	--sent_path ../data/cpp/test.sent \
    	--lb_path ../data/cpp/test.lb \
    	--pos_path ../data/cpp/test.pos
elif [ "$1" == "train" ]; then
    CUDA_VISIBLE_DEVICES=1 python scripts/train_g2p_bert.py \
	--config configs/config_cpp.py 
elif [ "$1" == "predict" ]; then 
    echo "$1"
    break
fi
