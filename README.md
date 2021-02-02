## VisionTutorial-python
  
新人研修で用いたpythonを使ってOpenCVでの画像処理の基本を学ぶ勉強会  
  
このリポジトリは[こちらのリポジトリ](https://github.com/yotaseki/VisionTutorial-Summer2019)のC++で書かれたソースコードをpythonで書き直し、内容を加えたものになります。
  
## 動作環境  
  
このリポジトリは以下の環境で動作を確認しています。  

- python 3.6.9  
- OpenCV 3.4.3  
- numpy 1.19.5  
  
基本的に **Linuxのネイティブ環境** を前提としています。  
自分のWSL環境でも動作は確認していますが、WSL側の問題で一部の動作を行うことできません。  
  
### はじめに
  
1. 環境構築をします。  
```sh
$ sudo apt update
$ sudo apt install python3
$ sudo apt-get install libopencv-dev python3-opencv
```
  
2. 00から順に各フォルダのREADMEに沿って進めてください。  
