# 机器实现

这里释出宇浩拆分规则的伪代码，用以展示使用计算机程序来实现拆分筛选的算法逻辑。注意，宇浩的拆分规则是**淘汰性**而非**引导性**的，故而算法的前置条件是已经拥有了若干的候选拆分，在此基础上，程序可以筛选出最满足宇浩拆分规则的唯一拆分。

假设某个汉字存在`N`个候选拆分，记为 `divs = {div_i | i in [1, 2, ..., N]}`。每个拆分都是字根的**有序**集合，记为 `div = {root_i | i in [1, 2, ..., M]}`，有以下属性：

- `div.len: int` 字根个数
- `div.bishun: Booleann` 字根是否完全合笔顺
- `div.san: Boolean` 字根是否分散
- `div.lian: Boolean` 字根是否相连
- `div.jiao: Boolean` 字根是否相交
- `div.duan: Boolean` 字根是否断开

注意：`div.san`, `div.lian`, `div.jiao`, `div`,`duan` 中有且只有一个是 `True`。

以下伪代码会从`N`个候选拆分`divs = {div_i | i in [1, 2, ..., N]}` 中选出最优拆分：

```python
# 字根最少
for div_i in divs:
    # 移除字根数量不是最少的候选拆分
    if div_i.len != min([i.len for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 符合笔顺
for div_i in divs:
    # 存在完全符合笔顺的拆分时，移除不完全符合笔顺的候选拆分
    if div_i.bishun != max([i.bishun for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 结构完整
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
}  # 包围结构得分更高
for div_i, div_j in permutation(divs, 2):  # 俩俩取候选拆分比较
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # 非共同字根中有包围结构的保留
    if unique_i.map(root_completeness_score) < unique_j.map(root_completeness_score):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根分散
for div_i in divs:
    # 存在散的拆分时，移除不散的候选拆分
    if div_i.san != max([i.san for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根相连
for div_i in divs:
    # 存在连的拆分时，移除不连的候选拆分
    if div_i.lian != max([i.lian for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根相交
for div_i in divs:
    # 存在交的拆分时，移除不交的候选拆分
    if div_i.jiao != max([i.jiao for i in divs]):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根断开
# 断属性为散连交的补集，故不用再进行判断

# 字根取大之一
# 让完全符合笔顺的部件尽可能地大
for div_i, div_j in permutation(divs, 2):  # 俩俩取候选拆分比较
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # root_bishun_score(div) 是局部拆分中完全符合笔顺的字根数量
    # 非共同字根中，完全符合笔顺的字根数量多的保留
    if root_bishun_score(unique_i) < root_bishun_score(unique_j):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根取大之二
# 让非歪斜根尽可能地大
for div_i, div_j in permutation(divs, 2):  # 俩俩取候选拆分比较
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # leaning_root_strokes(div) 是局部拆分中歪斜根的笔画数
    # 非共同字根中，非歪斜根笔画多的保留
    if leaning_root_strokes(unique_i) > leaning_root_strokes(unique_j):
        divs.remove(div_i)
    if len(divs) == 1:
        break  # 剩下唯一拆分候选，则停止判断

# 字根取大之三
# 让首笔靠前的字根尽可能地大
for div_i, div_j in permutation(divs, 2):  # 俩俩取候选拆分比较
    common = intersect(div_i, div_j)  # 共同的拆分部分
    unique_i = div_i.difference(common)  # 非共同的拆分部分
    unique_j = div_j.difference(common)  # 非共同的拆分部分
    # root_i.strokes.len 是字根的笔画数
    # 非共同字根中，靠前的字根笔画多的保留
    for root_i, root_j in zip(unique_i, unique_j):  # 俩俩取字根比较
        if root_i.strokes.len < root_j.strokes.len:
            divs.remove(div_i)

# 到此，必然只剩下唯一的拆分候选，即为最终拆分
```
