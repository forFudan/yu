# %%

import pandas as pd
import numpy as np
import re
from sklearn.metrics.pairwise import cosine_similarity

text = """
| 輸入法特性 · 輸入法名稱 | 四角號碼 | 倉頡   | 王碼五筆 | 表形碼 | 鄭碼 | 山人全息 | 徐碼   | 真碼 | 藍寶石2 | 矧碼 | 虎碼   | 宇浩光華 | 宇浩星陳 | 雲碼 | 藍寶石3 | 天碼 | 卿雲 |
| ----------------------- | -------- | ------ | -------- | ------ | ---- | -------- | ------ | ---- | ------- | ---- | ------ | -------- | -------- | ---- | ------- | ---- | ---- |
| 作者                    | 王雲五   | 朱邦復 | 王永民   | 陳愛文 | 鄭朧 | 謝振斌   | 徐國銀 | 命   | 秋風    |      | PeaceB | 朱宇浩   | 朱宇浩   | 爲雲 | 秋風    | 宋天 |      |
| 年份                    | 1926     | 1976   | 1986     | 1987   | 1989 | 2011     | 2013   | 2018 | 2020    | 2020 | 2021   | 2023     | 2023     | 2023 | 2023    | 2024 | 2024 |
| *編碼用鍵*              |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 數字作編碼              | ✓        |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| A-Y字母作編碼           |          | ✓      | ✓        | ✓      | ✓    | ✓        | ✓      | ✓    | ✓       | ✓    | ✓      | ✓        | ✓        | ✓    | ✓       | ✓    | ✓    |
| Z字母作字根編碼         |          |        |          | ✓      | ✓    | ✓        | ✓      |      |         | ✓    | ✓      |          |          | ✓    |         | ✓    |      |
| Z字母作補碼編碼         | -        | -      |          | ✓      | ✓    | ✓        | ✓      |      |         | ✓    | ✓      |          | ✓        | ✓    |         | ✓    | ✓    |
| 符號作編碼              |          |        |          |        |      |          |        |      |         | ✓    |        |          |          |      |         |      |      |
| *拆字理念*              |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 主取形態·切分筆畫       | ✓        | ✓      |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 主取部首·筆畫完整       |          |        | ✓        | ✓      | ✓    | ✓        | ✓      | ✓    | ✓       | ✓    | ✓      | ✓        | ✓        | ✓    | ✓       | ✓    | ✓    |
| 直觀優先                | ✓        | ✓      | ✓        | ✓      |      | ✓        |        |      | ✓       | ✓    | ✓      |          |          |      | ✓       |      |      |
| 規則優先                |          |        |          |        | ✓    |          | ✓      | ✓    |         |      |        | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| *取碼方法*              |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 取全部字根              |          |        |          |        |      | ✓        |        |      |         |      |        |          |          |      |         |      |      |
| 取次末根而非第三根      |          |        |          |        | ✓    | ✓        | ✓      |      |         |      |        |          |          |      |         |      |      |
| 所有字編碼長度一致      |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 字根單編碼              | ✓        | ✓      | ✓        | ✓      |      |          |        |      | ✓       |      |        |          |          |      | ✓       |      |      |
| 字根雙編碼              |          |        |          |        | ✓    | ✓        | ✓      | ✓    |         |      | ✓      | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| 漢字結構參與補碼        |          |        | ✓        |        |      |          |        |      | ✓       |      |        |          |          |      |         |      |      |
| 末根筆劃參與補碼        |          |        | ✓        |        |      |          |        |      | ✓       |      |        |          |          |      | ✓       |      |      |
| 首根筆畫作補碼          |          |        |          |        |      |          |        |      |         |      |        |          |          |      | ✓       |      |      |
| 最長編碼確定            | ✓        | ✓      | ✓        | ✓      | ✓    |          | ✓      | ✓    | ✓       | ✓    | ✓      | ✓        | ✓        | ✓    | ✓       | ✓    | ✓    |
| 最長編碼不確定          |          |        |          |        |      | ✓        |        |      |         |      |        |          |          |      |         |      |      |
| 最高四碼                | ✓        |        | ✓        | ✓      | ✓    |          | ✓      | ✓    | ✓       |      | ✓      | ✓        | ✓        | ✓    | ✓       | ✓    | ✓    |
| 最高五碼                |          | ✓      |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| *小碼情況*              |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 字根分主根副根          |          |        |          |        | ✓    |          | ✓      | ✓    |         |      |        |          |          |      |         |      |      |
| 首根有小碼則必取        | -        | -      | -        | -      | ✓    | ✓        | ✓      | ✓    | -       |      |        |          |          |      | -       |      |      |
| 首根有小碼則順取        | -        | -      | -        | -      | ✓    |          |        |      | -       |      |        |          |          |      | -       |      |      |
| 首根有小碼則後置        | -        | -      | -        | -      |      | ✓        | ✓      |      | -       |      |        |          |          |      | -       |      |      |
| 首根小碼作補碼          | -        | -      | -        | -      |      |          | ✓      |      | -       |      |        | ✓        | ✓        | ✓    | -       | ✓    | ✓    |
| 小碼主取形態·形托       | -        | -      | -        | -      | ✓    |          |        | ✓    | -       |      |        |          |          |      | -       | ✓    |      |
| 小碼主取聲母·強音托     | -        | -      | -        | -      |      | ✓        | ✓      |      | -       |      | ✓      |          | ✓        |      | -       | ✓    | ✓    |
| 小碼主取聲韻·弱音托     | -        | -      | -        | -      |      |          |        |      | -       |      |        | ✓        |          |      | -       |      |      |
| 小碼完全亂序            | -        | -      | -        | -      |      |          |        |      | -       | ✓    |        |          |          | ✓    | -       |      |      |
| *字根分區和聚類*        |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 字根按首筆分區          |          |        | ✓        |        | ✓    |          | ✓      | ✓    |         |      |        | ✓        |          |      |         |      |      |
| 字根按次筆分區          |          |        |          |        |      |          |        | ✓    |         |      |        |          |          |      |         |      |      |
| 字根按形態特徵聚類      | ✓        |        |          |        | ✓    |          | ✓      | ✓    |         |      |        |          | ✓        |      |         |      |      |
| 字根依字母相似度聚類    |          |        |          | ✓      |      |          |        |      |         |      |        |          |          |      |         | ✓    |      |
| 字根按意義或源流聚類    |          |        |          |        |      | ✓        |        |      |         |      |        |          |          |      |         |      |      |
| 字根完全亂序            |          |        |          |        |      |          |        |      | ✓       |      | ✓      |          |          | ✓    | ✓       |      | ✓    |
| 字根不分區              |          |        |          |        |      | ✓        |        |      | ✓       |      | ✓      |          | ✓        | ✓    | ✓       | ✓    | ✓    |
| 字根分區按鍵盤排佈      |          |        | ✓        |        |      |          |        | ✓    |         |      |        | ✓        |          |      |         |      |      |
| 字根分區按字典順序      |          |        |          |        | ✓    |          | ✓      |      |         |      |        |          |          |      |         |      |      |
| *設計理念*              |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 只打全碼設計            | ✓        | ✓      |          |        |      |          |        | ✓    |         |      |        |          |          |      |         |      |      |
| 全簡取碼不一致          | -        | -      |          |        | ✓    |          |        | -    |         |      |        |          |          |      |         |      |      |
| 只打單字設計            | ✓        | ✓      |          |        |      | ✓        |        | ✓    |         |      |        |          |          |      |         |      |      |
| 主字副詞設計            | -        | -      | ✓        |        |      | -        | ✓      | -    | ✓       |      | ✓      | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| 字詞混合設計            | -        | -      |          |        |      | -        |        | -    | ✓       | ✓    | ✓      |          |          |      | ✓       |      |      |
| 字詞取碼不一致          | -        | -      |          |        | ✓    | -        |        | -    |         |      |        |          |          |      |         |      |      |
| *繁簡字和生僻字處理*    |          |        |          |        |      |          |        |      |         |      |        |          |          |      |         |      |      |
| 繁簡字根刻意同鍵        |          |        |          |        |      | ✓        |        |      |         |      | ✓      |          |          |      |         |      |      |
| 繁簡字根刻意分離        |          |        |          |        |      |          | ✓      |      | ✓       | ✓    |        | ✓        | ✓        | ✓    |         |      | ✓    |
| 繁簡字根自然分離        | ✓        | ✓      |          | ✓      |      |          |        |      |         |      |        |          |          |      |         | ✓    |      |
| 官方提供GB2312碼表      | ✓        | ✓      | ✓        | ✓      | ✓    | ✓        | ✓      | ✓    | ✓       | ✓    | ✓      | ✓        | ✓        | ✓    | ✓       | ✓    | ✓    |
| 官方提供至CJK碼表       | ✓        | ✓      | ✓        | ✓      | ✓    | ✓        | ✓      | ✓    | ✓       | ✓    | ✓      | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| 官方提供至擴B區碼表     |          |        |          |        |      |          | ✓      |      |         |      | ✓      | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| 官方提供至擴I區碼表     |          |        |          |        |      |          |        |      |         |      | ✓      | ✓        | ✓        | ✓    |         | ✓    | ✓    |
| 超集字延用常用字字根    | -        | -      | -        | -      | -    | -        | ✓      | -    | -       | ✓    |        | ✓        | ✓        | ✓    | -       | ✓    | ✓    |
| 爲超集字設置額外字根    |          |        |          |        |      |          |        |      |         |      | ✓      |          |          |      |         |      |      |
"""

lines = text.split("\n")
header = lines[1].strip("|").split("|")

data = []

# Loop through lines starting from 2
for line in lines[6:]:
    # Break once we hit an empty line
    if not line.strip():
        break

    if line.strip().startswith("| *"):
        continue

    cols = line.strip("|").split("|")
    row = dict(zip(header, cols))
    data.append(row)

df = pd.DataFrame(data)
df = df.map(lambda x: x.strip())
df.columns = df.columns.map(lambda x: x.strip())
df = df.set_index("輸入法特性 · 輸入法名稱")

df


# %%
def to_value(x) -> float:
    if x == "✓":
        return 1.0
    elif x == "?":
        return 0.5
    elif x == "-":
        return 0
    else:
        return -1


df = df.map(to_value)

cos_simi_matrix = cosine_similarity(df.values.T)
cos_simi_matrix_lower = np.tril(cos_simi_matrix)

output = pd.DataFrame(cos_simi_matrix_lower)
output.index = df.columns
output.columns = df.columns

output

# %%


def format_output(x) -> str:
    if x == 0.0:
        return ""
    elif np.isclose(x, 1.0, atol=1e-8):
        return "-"
    else:
        return f"{x: .0%}"


output = output.map(format_output)

# %%
print(output.to_markdown())

# %%
