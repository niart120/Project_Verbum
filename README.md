# Project_Verbum
 
Pokemon Wordleを破壊するために色々作ってみました.
細かいドキュメントは時間があるときに作りたいですが, 作れるか怪しいです.

## Environment
Python3.6 or higher

## アルゴリズムについての概説
このプログラムは, 各ポケモンの名前によって得られる(条件付)平均エントロピーを評価値とする貪欲法によって実装されています.

より詳しい説明は時間が出来次第別サイトに掲載予定です.

## How to run

コマンドを実行すると, ランダムなお題(第八世代までのポケモン)についての解法が出力されます
```
git clone https://github.com/niart120/Project_Xs.git
cd ./Project_Verbum
python3 ./src/main.py
```

## Credits
ポケモン名の抽出, jsonファイル生成(names.json)の際に夜綱氏のPokemonPRNG(https://github.com/yatsuna827/PokemonPRNG) を利用させていただきました. この場をお借りして御礼申し上げます.
