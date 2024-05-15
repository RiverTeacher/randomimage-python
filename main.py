#別のサイトにリクエストするのに必要
import requests
#コンソールログの制御で必要なやつ
from IPython.display import clear_output
#画像をコンソールに出す
from IPython.display import Image

############設定項目#############

#確率を設定　数が低いほどえちえちしやすい。百分率で書く。　0.01〜0.99
probability = 0.5
###############################

print("""

 ■■■       ■                ■■■         ■■■     ■      ■      ■■■   ■      ■      ■        ■■■     ■■■■
■■■■■■    ■■     ■■     ■  ■■■■■■     ■■■ ■■   ■■■     ■■     ■■   ■■■     ■■    ■■      ■■■ ■■   ■■■■■
■■   ■    ■■■    ■■■    ■  ■■    ■   ■■     ■  ■■■    ■■■      ■   ■■■    ■■■    ■■■    ■■        ■■
■■   ■   ■■ ■    ■ ■■   ■  ■■    ■■  ■      ■  ■ ■    ■ ■      ■   ■ ■    ■ ■   ■■ ■    ■         ■■
■■   ■   ■  ■    ■  ■   ■  ■■     ■  ■      ■■ ■ ■■  ■■ ■      ■   ■ ■■  ■■ ■   ■  ■    ■         ■■■■■
■■■■■    ■  ■■   ■  ■■  ■  ■■     ■  ■      ■■ ■  ■  ■  ■      ■   ■  ■  ■  ■   ■  ■■   ■   ■■■■  ■■■■■
■■  ■   ■■■■■■   ■   ■■ ■  ■■    ■■  ■      ■■ ■  ■  ■  ■      ■   ■  ■  ■  ■  ■■■■■■   ■     ■■  ■■
■■  ■■  ■    ■■  ■    ■■■  ■■    ■■  ■■     ■  ■  ■■■   ■      ■   ■  ■■■   ■  ■    ■■  ■■    ■■  ■■
■■   ■  ■     ■  ■    ■■■  ■■   ■■    ■    ■■  ■   ■■   ■      ■   ■   ■■   ■  ■     ■   ■■   ■■  ■■
■■   ■■■      ■  ■     ■■  ■■■■■■      ■■■■■   ■   ■■   ■     ■■■  ■   ■■   ■ ■      ■    ■■■■■■  ■■■■■■



                                                                                                        """)


#APIサイトに画像をリクエスト
print('connecting to server....\n食べ物優先度',probability,'えちえち優先度',1.0 - probability,'でリクエストをしています....')
response = requests.get(f"https://copper-radial-toucan.glitch.me/imagev2?foodProbability={probability}")

#成功したら
if response.status_code == 200:
    #画像をロードする準備
    print("画像をロードしています....")
    #コンソールを一回クリアする。
    clear_output(wait=True)
  #取得した画像リンクを保存
    image_url = response.text
    #画像リンクから画像に変換してコンソールに出す
    display(Image(url=image_url, embed=True))
#成功以外なら(失敗の場合)
else:
  #エラー文を出す
    print("エラーが発生しました。")
