## seleniumのdocker起動
### 結論
```
selenium/standalone-chrome
```
を使えば可能


### このリポジトリは？
上記`selenium/standalone-chrome`のコンテナとそれを使ってpythonを実行するコンテナを立てている


#### 必要なもの
```
docker
```

#### 起動手順
```
docker-compose build
docker-compose up

（別のターミナルで）
docker exec -it scraper /bin/bash
python ./src/test.py
```