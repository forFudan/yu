# 機器實現

這裡釋出宇浩拆分規則的偽代碼，用以展示使用計算機程序來實現拆分篩選的算法邏輯。注意，宇浩的拆分規則是**淘汰性**而非**引導性**的，故而算法的前置條件是已經擁有了若干的候選拆分，在此基礎上，程序可以篩選出最滿足宇浩拆分規則的唯一拆分。

假設某個漢字存在`N`個候選拆分，記為 `divs = {div_i | i in [1, 2, ..., N]}`。每個拆分都是字根的**有序**集合，記為 `div = {root_i | i in [1, 2, ..., M]}`，有以下屬性：

- `div.len: int` 字根個數
- `div.bishun: Booleann` 字根是否完全合筆順
- `div.san: Boolean` 字根是否分散
- `div.lian: Boolean` 字根是否相連
- `div.jiao: Boolean` 字根是否相交
- `div.duan: Boolean` 字根是否斷開

注意：`div.san`, `div.lian`, `div.jiao`, `div`,`duan` 中有且只有一個是 `True`。

以下偽代碼會從`N`個候選拆分`divs = {div_i | i in [1, 2, ..., N]}` 中選出最優拆分：

```python
# 字根最少
for div_i in divs:
    # 移除字根數量不是最少的候選拆分
    if div_i.len != min([i.len for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 符合筆順
for div_i in divs:
    # 存在完全符合筆順的拆分時，移除不完全符合筆順的候選拆分
    if div_i.bishun != max([i.bishun for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 結構完整
root_completeness_score = {
    囗：2,
    日：2,
    目：2,
    田：2,
    冂：1,
    勹：1,
    匚：1,
    凵：1,
    コ：1,
    其他：0,
}  # 包圍結構得分更高
for div_i, div_j in permutation(divs, 2):  # 倆倆取候選拆分比較
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # 非共同字根中有包圍結構的保留
    if unique_i.map(root_completeness_score)  unique_j.map(root_completeness_score):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根分散
for div_i in divs:
    # 存在散的拆分時，移除不散的候選拆分
    if div_i.san != max([i.san for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根相連
for div_i in divs:
    # 存在連的拆分時，移除不連的候選拆分
    if div_i.lian != max([i.lian for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根相交
for div_i in divs:
    # 存在交的拆分時，移除不交的候選拆分
    if div_i.jiao != max([i.jiao for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根斷開
# 斷屬性為散連交的補集，故不用再進行判斷

# 字根取大之一
# 讓完全符合筆順的部件儘可能地大
for div_i, div_j in permutation(divs, 2):  # 倆倆取候選拆分比較
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # root_bishun_score(div) 是局部拆分中完全符合筆順的字根數量
    # 非共同字根中，完全符合筆順的字根數量多的保留
    if root_bishun_score(unique_i)  root_bishun_score(unique_j):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根取大之二
# 讓非歪斜根儘可能地大
for div_i, div_j in permutation(divs, 2):  # 倆倆取候選拆分比較
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # leaning_root_strokes(div) 是局部拆分中歪斜根的筆畫數
    # 非共同字根中，非歪斜根筆畫多的保留
    if leaning_root_strokes(unique_i)  leaning_root_strokes(unique_j):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候選，則停止判斷

# 字根取大之三
# 讓首筆靠前的字根儘可能地大
for div_i, div_j in permutation(divs, 2):  # 倆倆取候選拆分比較
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # root_i.strokes.len 是字根的筆畫數
    # 非共同字根中，靠前的字根筆畫多的保留
    for root_i, root_j in zip(unique_i, unique_j):  # 倆倆取字根比較
        if root_i.strokes.len  root_j.strokes.len:
            divs.remove(div_i)

# 到此，必然只剩下唯一的拆分候選，即為最終拆分
```
