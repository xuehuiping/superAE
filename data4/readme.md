全部数据参与训练

xuehp@haomeiya002:~/git/superAE/data4/


---
source ~/anaconda3/bin/activate
conda create --name env_superAE python=3.5
conda activate env_superAE
pip install torch==0.3.1 -i https://pypi.tuna.tsinghua.edu.cn/simple   
---

python preprocess.py -train_src data4/train.src -train_tgt data4/train.tgt \
 -valid_src data4/valid.src -valid_tgt data4/valid.tgt -save_data data4/ 
 
python train.py -config data4/lcsts.yaml -gpus 0

---

2号机器运行太慢,换到7号机器.


xuehp@haomeiya007:~/git/superAE/data4$ scp xuehp@haomeiya002:~/git/superAE/data4/summary.txt .

xuehp@haomeiya007:~/git/superAE/data4$ scp xuehp@haomeiya002:~/git/superAE/data4/article.txt .

python x4.py

没有process, 从2号机器拷贝pt数据

---

升级pytorch


  Could not find a version that satisfies the requirement torch==0.5.1 (from versions: 0.1.2, 0.1.2.post1, 0.1.2.post2, 0.3.1, 0.4.0, 0.4.1, 1.0.0, 1.0.1, 1.0.1.post2, 1.1.0, 1.2.0, 1.3.0, 1.3.1, 1.4.0, 1.5.0, 1.5.1)
No matching distribution found for torch==0.5.1

pip install torch==0.4.1 -i https://pypi.tuna.tsinghua.edu.cn/simple   
