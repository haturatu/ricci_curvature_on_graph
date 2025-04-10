# wip
@wowowo-wo

# Usage
pyenv setup
```bash
# aptパッケージのアップデート
sudo apt update
# pyenvをインストールするために必要なパッケージをインストール
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
    libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

# curlで取得したコードをそのままパイプでbashに渡してシェルスクリプト実行しインストールスクリプト実行
curl https://pyenv.run | bash

# pyenvに必要な環境変数を初期化する処理をシェルに入った後実行
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc

# 現在のシェルで.bashrcを実行し、適応
source ~/.bashrc
```

```bash
cd ~ ; mkdir git ; cd git ; git clone https://github.com/haturatu/ricci_curvature_on_graph ; cd ricci_curvature_on_graph
# pyenvの仮想環境としてライブラリが対応しているPythonのバージョンをインストール
pyenv install 3.10.13

# すでに.python-versionがあるから不要だと思うが念の為実行
pyenv local 3.10.13

# 依存関係のPythonのライブラリインストール
pip install -r requirements.txt

# 実行
python3 main.py
```
