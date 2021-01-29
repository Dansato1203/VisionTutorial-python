## 01_pixel
  
ここではデジタル画像の仕組みについて簡単に説明します。  
  
### デジタル画像の仕組み
  
デジタル画像は小さな点から構成されています。  
その小さい点のことを**画素(ピクセル)**といいます。  
  
### 画素(ピクセル)とは？

[wikipedia(ピクセル)](https://ja.wikipedia.org/wiki/%E3%83%94%E3%82%AF%E3%82%BB%E3%83%AB)では  
>画素（がそ）とは、コンピュータで画像を扱うときの色情報 (色調や階調) を持つ最小単位、最小要素。
と定義されています。  
  
つまり、デジタル画像を構成する色情報を持っためっっちゃ小さい点です。  
画素数が多ければ画像をより細かいところまで写すことができます。  
余談ですが、画素の密度のことを解像度といいます。  
  
デジタル画像は小さな点(ピクセル)が集まって構成されているのでクソ細かいドット絵といえばわかりやすいかもしれません。  
  
### 画素(ピクセル)の色情報  

今回の勉強会で用いているOpenCVでは主に  
- BGR色空間
- HSV色空間
などがよく利用されています。  
  
ここで上記2つの色空間について簡単に説明します。  
  
1. BGR色空間
光の三原色であるB(Blue: 青)、G(Green: 緑)、R(Red: 赤)の3つのチャンネルからなる色空間です。  
それぞれのピクセルに色情報が(B, G, R)の順で格納されています。  
よく耳にする(R, G, B)とは順番が違うので注意が必要です。  
それぞれの色情報が0 - 256の段階で指定されています。  
  
2. HSV色空間
Hue(色相), Saturation(彩度), Value(明度)で表される色空間です。  
- Hue(色相)
色の種類(赤、青、緑とか)を指す。0 - 360の範囲で指定される。  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_hue.png width=500px>  
  
- Saturarion(彩度)
色の鮮やかさの度合いを指す。彩度が高いほど鮮やかな色になる。0 - 100の範囲で指定される。  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_saturation.png width=500px>  
  
- Value(明度)  
色の明るさの度合いを指す。明度が高いほど明るく白っぽく、低いほど暗く黒っぽくなる。  
<img src=https://github.com/Dansato1203/images/blob/master/VisionTutorial-python/HSV_value.png width=500px>  

