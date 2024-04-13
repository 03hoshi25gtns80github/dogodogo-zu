### docker

コマンド ➀：docker ディレクトリに移動後に実行、docker イメージ作成  
docker build -t dogodogo-zu .  
コマンド ➁：docker コンテナ起動、自身のローカルリポジトリと docker コンテナ内のリポジトリをマウント
（C:\Users\03hos\Documents\benkyo\dogodogo-zu の部分は自身の PC のパス）
docker run -it --name dogodogo-zu -v C:\Users\03hos\Documents\benkyo\dogodogo-zu:/dogodogo-zu dogodogo-zu /bin/bash  
コマンド ➂：二回目以降のコンテナの起動
docker start -ai dogodogo-zu



### soratest

otameshi

### matsumototest

otamesi