# 02_Advanced
  
ここでは00_tutrialと01_pixelで学んだ基礎知識を使って、少し発展的な内容に触れます。  
  
---
  
## Color_extraction  

OpenCVを使うことで、デジタル画像から任意の色だけを抽出することができます。  
ここでは、もともとのBGR色空間のまま抽出する方法とBGR色空間をHSV色空間に変換して抽出する方法の2パターンを紹介します。  
   
---
  
### 1. BGR色空間での抽出
  
任意の色を抽出する画像には以下の画像を使います。  
  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/sea.jpg>  
  
この画像から青色の部分と緑色の部分を抽出します。  
  
サンプルコードを用いて抽出した結果は以下のようになります。  
  
1. BGR色空間で青色を抽出した結果  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/BGR_blue.jpg>  
  
2. BGR色空間で緑色を抽出した結果  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/BGR_green.jpg>  
  
  
結果からうまく任意の色のみを抜き取れていることがわかります。  
これは、画像から任意の色をもつピクセルはそのまま、指定した色以外の色情報をもつピクセルは黒く塗るという処理を行った結果です。  
  
---
  
### 2. HSV色空間での抽出  
  
任意の色をBGR色空間と同様に以下のものを使います。  
  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/sea.jpg>  
  
抽出する色も同様に青と緑とします。  
  
まず、BGR色空間をHSV色空間に変換すると以下のようになります。  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_image.jpg>  
(これを表示する意味はあまりないです。BGR色空間とは違う色空間がある、ということを認識してください) 
  
サンプルコードを用いて抽出した結果は以下のようになります。  
  
1. HSV色空間で青色を抽出した結果  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_blue.jpg>  
  
2. HSV色空間で緑色を抽出した結果  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_green.jpg>  
  
BGR色空間と同様に指定した色だけをうまく抽出できていることがわかります。  
処理自体は先ほどと同様です。  
  
---
  
## 実際に確認してみよう
  
### 1. BGR色空間での色抽出の実践
  
1. BGR色空間で任意の色を抽出できるサンプルコードを確認してみましょう。  
```sh
vi BGR_extraction.py
```
  
2. 実行してみましょう  
```sh
./BGR_extraction.py
```
  
上記の画像が表示されていたら成功です。  
  
### 課題 
抽出する色のしきい値を変更して、挙動の変化を確認しましょう。  
  
---
  
### 2. HSV色空間での色抽出の実践  
  
1. HSV色空間で任意の色を抽出できるサンプルコードを確認してみましょう。  
```sh
vi HSV_extraction.py
```
  
2. 実行してみましょう  
```sh
./HSV_extraction.py
```
  
上記の画像が表示されていたら成功です。  
  
### 課題 
抽出する色のしきい値を変更して、挙動の変化を確認しましょう。  
  
---
  
### BGR色空間とHSV色空間
  
今回、このリポジトリのサンプルコードをコーディングしているときに感じたことですが、BGR色空間よりHSV色空間のほうが直感的に抽出した色の調整ができました。  
BGR色空間は原色の組み合わせで色が決定されるため(BGRのほうが慣れてるし)、こっちのほうが簡単に調整できそうに思われますが、それぞれの値が組み合わさった後の色に与える影響が判断しにくく調整はしづらいと感じました。  
一方、HSV色空間は「色相」に「鮮やかさ」と「明るさ」といった直感的な要素が組み合わさるだけなので、細かい色の調整が容易に行えました。  
場合によりけりですが、任意の色を抽出するときはHSV色空間に変換するほうが良いかと思います。  
  
---
  
## Face_Recognition
  
OpenCVの中には顔検出などをしてくれるフィルター的なのものも用意されています。  
ここでは画像の中の顔を検出する方法を紹介します。  
  
OpenCVでは、公式で学習済みの分類器のデータが用意されています。  
分類器のデータ[こちら](https://github.com/opencv/opencv/tree/master/data/haarcascades)にあります。  
  
今回はそれを用いて顔検出を行います。  
  
---
  
## 実際に確認してみよう
  
1. 顔検出するプログラムを確認してみましょう。  
```sh
vi pic_face_recognition.py
```
  
2. 実行してみましょう  
```sh
./pic_face_recognition
```
  
うまく女性の顔が検出できていたでしょうか。  
  
---
  
### 余談
また、WSL以外の環境の方でwebカメラをつかうことができる場合、その映像から顔を検出することもできます。  
試しに実行してみましょう。  
```sh
./vi_face_recognition.py
```
  

