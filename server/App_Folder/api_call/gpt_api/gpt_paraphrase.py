# 環境変数にAPIキーを設定
import os
from dotenv import load_dotenv
import openai
from pathlib import Path
import json
import time

load_dotenv(Path(__file__).parent.parent.joinpath(".env"))
openai.api_key = os.environ["OPENAI_API_KEY"]

# テキストを受け取って平易に言い換えたテキストを返す
# 07/22: ほとんど内容が変わらなかったので、"より短く簡潔に言い換える"方針に変更
def paraphrase(content):
  time_sta = time.time()
  # few-shot exampleを二つ与えて、出力の量・内容を制限(例はもっと増やせる)
  prompt = """
          Task: Please provide a shorter abstract of the following paper in Japnese.
          
          Input Abstract(Example):
          大規模言語モデル(LLM)は、教師あり命令/応答データに対する命令-微調整(IFT)によって命令追従能力を得る。しかし、広く使われているIFTデータセット(例えばAlpacaの52kデータ)には、意外にも、誤った回答や無関係な回答を含む低品質なインスタンスが多く含まれており、IFTにとって誤解を招き有害である。本論文では、強力なLLM(例えばChatGPT)を用いて低品質なデータを自動的に識別し除去する、シンプルで効果的なデータ選択戦略を提案する。この目的のために、我々はAlpaGasusを導入する。AlpaGasusは、52kのAlpacaデータからフィルタリングされた9kの高品質データのみで微調整される。AlpaGasusは、複数のテストセットにおいてGPT-4で評価されたオリジナルのAlpacaを大幅に上回り、その13B変種はテストタスクにおいて教師LLM（すなわちText-Davinci-003）の$>90%$性能と一致する。また、Alpaca(7B)と同じエポック数で、より少ないデータで、4$times$NVIDIA A100(80GB)のGPUを使用し、元のAlpacaの設定とハイパーパラメータに従って、IFTを適用する。全体として、AlpaGasusは、新しいデータ中心IFTパラダイムを実証しており、命令チューニングデータに一般的に適用することができ、より高速な学習とより良い命令追従モデルにつながります。私たちのプロジェクトページは、∕URL{https://lichang-chen.github.io/AlpaGasus/}にあります。'
          Output summary(Example):
          大規模言語モデルは命令とその解答例を学習させることでより正しく命令に応えることができます。しかしよく使われるIFTデータセットも、誤ったデータが多く含まれています。そこで、ChatGPTのような高性能の大規模言語モデルで、誤ったデータを除去します。私たちの提案したAlpaGasusは高品質データだけで学習することで普通のAlpacaの結果を上回りました。


          Input Abstract(Example):
          大規模な事前学習とそれに続く下流での微調整というパラダイムは、様々な物体検出アルゴリズムにおいて広く採用されている。本論文では、既存の手法における事前学習と微調整の手順間のデータ、モデル、タスクの不一致を明らかにし、それが暗黙のうちに検出器の性能、汎化能力、収束速度を制限していることを示す。このため、既存の様々な検出器に適用可能な、統一的な事前学習フレームワークであるAlignDetを提案する。AlignDetは、事前学習プロセスを2つの段階、すなわち、画像領域の事前学習と箱領域の事前学習に分離する。画像領域の事前学習では、全体的な視覚的抽象化を捉えるために検出バックボーンを最適化し、ボックス領域の事前学習では、インスタンスレベルの意味論とタスクを意識した概念を学習し、バックボーンのパーツアウトを初期化する。自己教師付き事前訓練バックボーンを組み込むことで、教師なしパラダイムで様々な検出器の全モジュールを事前訓練することができる。図1に描かれているように、広範な実験により、AlignDetは、検出アルゴリズム、モデルバックボーン、データ設定、および訓練スケジュールなどの多様なプロトコルにわたって大幅な改善を達成できることが実証されている。例えば、AlignDetはFCOSを5.3mAP、RetinaNetを2.1mAP、Faster R-CNNを3.3mAP、DETRを2.3mAP、少ないエポックで改善する。

          Output summary(Example):
          物体検出アルゴリズムにおいて、事前学習と微調整の間で、用いるデータ・モデル・タスクに違いがあります。そのため検出機の性能、汎化能力、収束速度に悪影響が生じます。
          そこで、さまざまな検出機に適用できる、統一的な事前学習フレームワークであるAlignDetを提案します。具体的には、事前学習を画像の分野とボックス領域の分野に分けて行います。画像分野では抽象的な分野を捉えるために検出バックボーンの最適化を行う。ボックス領域ではインスタンスレベルの意味論とタスクタスクを意識した概念を学習する。実験により、物体検出アルゴリズムの多様な分野において大幅な改善が見られました。

          Input Abstract:
           """\
          + content \
          + "\n Output Abstract:"
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-16k",
    messages=[
      {"role": "system", "content": "You are the editor of a scientific journal for the general public."},
      {"role": "user", "content": prompt}
    ],
    temperature=0,
  )

  result = completion["choices"][0]['message']['content']
  
  time_end = time.time()
  # 経過時間（秒）
  tim = time_end- time_sta
  print(f"time to paraphrase: {tim}")
  # print(result)
  return result

# # Example Usage
# Text = 'シーケンスの長さをスケーリングすることは、大規模言語モデルの時代において重要な要求となっている。\nしかし、既存の方法は、計算の複雑さとモデルの表現力のどちらか\n計算の複雑さとモデルの表現力のどちらにも苦戦しており、最大配列長\nを制限している。本研究では、Transformerの変種であるLongNetを紹介する。\nより短いシーケンスの性能を犠牲にすることなく、シーケンスの長さを10億トークン以上に拡張できる\nを導入する。具体的には、拡張注意（dilated attention）を提案する、\nこれは距離が長くなるにつれて、注意フィールドを指数関数的に拡大する。ロングネット\nには大きな利点がある：1)計算の複雑さは線形で、トークン間の依存関係は対数である。\nトークン間の依存性が対数である。\n3）その拡張された注意は、標準的な注意に取って代わることができる。\n標準的なアテンションとシームレスに統合できる。\n既存のTransformerベースの最適化とシームレスに統合できる。実験の結果\nLongNetは、長シーケンスモデリングと一般的な言語タスクの両方において強力な性能を発揮する。\n言語タスクの両方で強力な性能を発揮することが実証された。我々の研究は、非常に長いシーケンスのモデリングに新たな可能性を開く。\n例えば、コーパス全体やインターネット全体をシーケンスのように扱うことができる。'
# print(paraphrase(Text))
