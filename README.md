### docker  
コマンド➀：dockerディレクトリに移動後に実行、dockerイメージ作成  
docker build -t dogodogo-zu .  
コマンド➁：dockerコンテナ起動、自身のローカルリポジトリとdockerコンテナ内のリポジトリをマウント
（C:\Users\03hos\Documents\benkyo\dogodogo-zuの部分は自身のPCのパス）
docker run -it -v C:\Users\03hos\Documents\benkyo\dogodogo-zu:/dogodogo-zu dogodogo-zu /bin/bash  
### soratest  
otameshi
