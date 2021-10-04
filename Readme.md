# 给羽觞觞的百度人脸融合调用程序

## Quick Start
1. 用你熟悉的方式创建一个conda 环境
2. `conda activate 你的环境`
3. `git clone` 这个仓库
4. `cd`到下载好的这个仓库的目录
5. `pip install -r requirements.txt`
6. 可以愉快地使用了. 使用方式
```bash
python main.py --client_id <从官网拿到的access_key> \
               --client_secret <从官网拿到的access_secret> \
               <你想把哪张图的脸融合>
               <融合到哪张图的脸上>
```
