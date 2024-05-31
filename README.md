# polyphone

Our paper: CVTE-Poly A New Benchmark for Chinese Polyphone Disambiguation, Interspeech 2023 (accepted)

[中文版本](https://newzsh.github.io/zsh/blogging/2022/06/06/polyphone_cn.html)

[English version](https://newzsh.github.io/zsh/blogging/2022/06/06/polyphone.html)

# files

    ├── README.md
    ├── data
    │   ├── CVTE-poly            
    │   ├── POLYPHONIC_CHARS.txt  # generate from `digest_cedict.pkl` by script `cedict2csv.py`
    │   ├── cpp                   # combine `g2pm/data` and `g2pW/cpp_dataset`
    │   └── digest_cedict.pkl     # dictionary has been corrected
    ├── g2pW
    ├── g2pm
    └── scripts
        ├── cedict2csv.py
        └── filter_pos.py         # adjust the `pos` files

### notes
  - `.pos` files are prepared for g2pW training
    - in `data/CVTE-poly`, the POS are labeled by `ckiptagger` [https://github.com/p208p2002/ckiptagger?tab=readme-ov-file], same as `g2pW` does
    - in `data/cpp`, the POS are downloaded from `g2pW` repo and processed by `filter_pos.py`. Please refer to the scripts.