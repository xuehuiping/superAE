全部数据参与训练

xuehp@haomeiya002:~/git/superAE/data4/


---
source ~/anaconda3/bin/activate
conda create --name env_superAE python=3.5
conda activate env_superAE
pip install torch==0.3.1
---

python preprocess.py -train_src data4/train.src -train_tgt data4/train.tgt \
 -valid_src data4/valid.src -valid_tgt data4/valid.tgt -save_data data4/
 
python train.py -config data4/lcsts.yaml 