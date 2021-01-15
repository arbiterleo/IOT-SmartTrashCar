# IOT-Project 智慧垃圾車

### Introduction

這是一台能夠幫助你丟垃圾的智慧垃圾車。
當你舒服地坐在座位上不想站起來時，只要在手機上按個按鈕，它就會自動前來收走你的垃圾並幫你拿去垃圾桶。

在此專案中，你必須具備基礎的電路學知識，並且會使用樹莓派以及python來驅動硬體設備。

### Things you will need

+ 一個RasPberry Pi 3
+ 行動電源，用於給樹梅派供電
+ 一個L298N馬達驅動模組
+ 一個電池盒
+ 四顆1.5v電池
+ 彩虹排線
+ Micro USB傳輸線
+ 四個直流減速電機
+ 一套雙層四驅自走車底盤(包含四顆輪胎)

### Before Getting Start

在開始之前，你必須先架設好樹梅派的環境。
請根據本專案中的rasberryPi_instruction文件來架設環境。

當你按照文件中的步驟一步一步進行，最後你應該會擁有一個已安裝好conda與python的作業系統。

接著打開terminal，輸入下列指令來透過conda安裝flask。

```
conda install flask
```

flask是一個使用Python編寫的輕量級Web應用框架，透過它我們可以在短短幾行程式碼內便建出一個可用的網站。

接著，創建用來存放專案的資料夾。

```
mkdir carapp

cd carapp

mkdir statics
mkdir templates
```

這些資料夾用於存放控制車子行動的網頁。

當我們需要呼叫車子時，我們會透過手機進入我們寫好的網頁，然後網頁會根據使用者的行動再呼叫rasPberryPi上已寫好的python程式來控制車子。

### Build up your Car

在進行其他步驟之前，我們必須先組裝好車子。

照著此影片組裝你的車體。
https://www.youtube.com/watch?v=uW8YVcBjPGU

我使用的車體是在下列連結購買的，如果你使用的是其他型號的車體，可能必須自行尋找組裝的方法。

[連結](https://www.taiwaniot.com.tw/product/%e5%9b%9b%e9%a9%85-4wd-%e6%99%ba%e6%85%a7%e5%b0%8f%e8%bb%8a-%e8%87%aa%e8%b5%b0%e8%bb%8a-%e6%a9%9f%e5%99%a8%e4%ba%ba-%e5%ba%95%e7%9b%a4%e9%96%8b%e7%99%bc%e5%a5%97%e4%bb%b6%e7%b5%84/)

### L298N motor driver

我們使用L298N motor driver來驅動車體附贈的四台直流馬達。

這部影片中有較為詳細的講解。
https://www.youtube.com/watch?v=bNOlimnWZJE&list=PLc6fhBPeC6SBbZFcrHLlPXyR2svfxf1RZ&index=19&t=507s

##### 開始之前該注意的地方
+ L298N motor driver一開始被包裝在一個防靜電的袋內，確保你在接觸它之前已消過靜電，並且在用完時應將它放回袋內
+ 直流馬達與L298N motor driver的正負極要分清楚，千萬不要接反，不然就會跟我一樣報銷設備還浪費一堆時間debug
+ 線要接穩不然會一直掉，建議使用杜邦線而不要用車體附贈的紅黑線，並且L298N motor driver上面的螺絲是可以調整鬆緊的，善用這些點來提高工作效率

##### 線路圖
![線路圖](/suppotpics/l298n.jpg)

可以直接照著線路圖接，不過要記得線接在樹梅派的哪個腳位，因為程式要用到。

### How to implement

使用者一開始應該要進入index.html，然後得先設定航線。

點擊設定航線後會進入controll.html，讓使用者能夠自己操控車子前進，並且車子會自動記錄航線。

記錄好後，使用者返回index.html並且將車子放置垃圾桶旁。

之後使用者只需在index.html按呼叫車子的按鈕車子就會沿著航線從垃圾桶旁來到使用者設定好的位置，然後當使用者放好垃圾按下返回按鈕，車子就會帶著垃圾原路返回垃圾桶。

### Programming

### Control wheels

### PWM

### Final Product

成品示意圖

![成品圖](/suppotpics/final.jpg)

### Functions can be improved or have not been made

1. 無法讓車子自動偵測到使用者位置
2. 沒有自動避障功能
3. 網頁只能透過本機存取
4. 未來應該加裝垃圾籃來丟垃圾

### Reference

參考資料連結

+ https://github.com/Penny0514/IoT_car#features
+ https://github.com/ponponmusic/IOT-Project-_-FourWheelCar-ImageRecognize

### Demo video

https://www.youtube.com/watch?v=ibp4K1n_lDc&ab_channel=leoarbiter
