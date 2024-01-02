import cv2
import numpy as np
from matplotlib import pyplot as plt
import subprocess


FILE = r""
CASCADE = r""

img = cv2.imread(FILE)
#画像の高さ
height = img.shape[0]
#画像の幅
width = img.shape[1]
# 画像サイズを取得
print(f"height:{height}, width:{width}")

cv2.putText(img,
            "Hello Python",
            org=(200, 50),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1.5,
            color=(0, 255, 0),
            thickness=2,
            lineType=cv2.LINE_AA)

color = ("b", "g", "r")
for i, col in enumerate(color):
    histr = cv2.calcHist(images=[img], channels=[i],
     mask=None, histSize=[256], ranges=[0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.show()

# 画像をトリミング
#trim = img[200: 500, 300: 600]
#cv2.imwrite(r"C:\Users\coff-\OneDrive\デスクトップ\Hack\trim.jpg", trim)

#resize = cv2.resize(img, dsize=(200, 200))
#resize = cv2.resize(img, dsize=None, fx=1, fy=0.5)

# 画像処理のノイズ除去のため一旦グレースケールに変更
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#グレースケールの表示
#cv2.imshow('img', gray)
#cv2.waitKey(0)

#学習済みモデルの読み込み
cascade = cv2.CascadeClassifier(CASCADE)
# 顔の検出
# minSizeで最小検出サイズを指定（今回は20*20以下は探さない）
face = cascade.detectMultiScale(gray, minSize = (20, 20))

# 白黒に変換
#ret, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY_INV)
#cv2.imwrite(r"C:\Users\coff-\OneDrive\デスクトップ\Hack\change1.png", thresh)

# 輪郭検出
#img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img, contours, -1, (0, 0, 255), 10)
#cv2.imwrite(r"C:\Users\coff-\OneDrive\デスクトップ\Hack\change2.png", img)

# 円を検出
#circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=0.8, minDist=50, param1=100, param2=60, minRadius=0, maxRadius=0)
# numpyを用いて描画できる形に変換
#circles = np.uint16(np.around(circles))

# 円が見つかるかで条件分岐
#if len(circles):
    #for circle in circles[0, :]:
    # 円周を描画
        #cv2.circle(img, (circle[0], circle[1]), circle[2], (0, 0, 255), 10)

    # 中心点を描画
        #cv2.circle(img, (circle[0], circle[1]), 2, (0, 0, 255), 5)
   
    #cv2.imshow('img', img)
    #cv2.waitKey(0)

#else:
    #print('見つかりませんでした')

# 顔が見つかるかで条件分岐
if len(face):
    for (x,y,w,h) in face:
        # 顔が見つかった場合赤い四角で囲う
        print('見つけました')
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), thickness=3)
    cv2.imshow('img', img)
    cv2.waitKey(0)

# 顔が見つからなかった場合
else:
    print('見つかりませんでした')

#cv2.imshow('imshow_test', gray)
#cv2.waitKey(0) #待機時間、ミリ秒指定、0の場合はボタンが押されるまで待機
#cv2.destroyWindows()
#cv2.waitKey(1) #待機時間、ミリ秒指定、0の場合はボタンが押されるまで待機
