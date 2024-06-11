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
    │   └── cedict2csv.py 
    │   └── POStagging.py         # generate the `.pos` files
    ├── g2pW                      # fork from `g2pW` repo and modify
    ├── g2pm 
    └── scripts                   # my self model

# results

| | acc (Avg. by #sample) | acc (Avg. by #polyphone) | acc (Avg. by #phoneme) |
|---|---|---|---|
| g2pM (ori paper BiLSTM) | 97.31 | - | - |
| g2pM (ori paper BERT) | 97.85 | - | - |
| g2pM (pip and test) | - | - | - |
| g2pW (ori paper) | 99.08 | - | - |
| g2pW (trained on CPP) | 99.0711 | 98.608 | 96.4619 |
| g2pW (trained on CPP + CVTE-poly) | 99.0711 | 98.5023 | 96.6914 |
| self (trained on CPP) | 
| self (trained on CPP + CVTE-poly) |


### notes
  - `.pos` files are prepared for g2pW training. 
  
      The POS are labeled by `ckiptagger` [https://github.com/p208p2002/ckiptagger?tab=readme-ov-file], same as `g2pW` does. However, I do not directly download the `.pos` files for CPP dataset from `g2pW` repo, because the version of `ckiptagger` varied.

  - results of original paper are over-estimated.
  
      In the original test set of CPP, there are **1319** sentences which take a non-polyphone as a target character. After removing these sentences, there are only **8925** sentences in the test set. Using the original test set results in over-estimation of the models.