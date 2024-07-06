# 常見輸入法測評數據

夢澤閒客 更新於二零二四年五月七日

::: warning 提醒

本文只是呈現輸入法的客觀測評數據，不能用來作爲此輸入方案是否優秀的唯一評價標準。評判一個輸入方案，應該綜合考量以下因素：

- 在不同字集/使用環境下的重碼率。
- 規則複雜度。
- 字根記憶難度。
- 拆字直觀性/唯一性/容錯性。
- 和漢字體系和漢字理論的相容性。
- 編碼或規則的特例數量。
- 人體工學性。
- 平臺通用性。
:::

## 單字重碼數據

### 單字重碼定義

表格中的各項名稱定義如下：

- 「通規一二級」是指大陸《通用規範漢字表》中的 6500 個簡化漢字。測試輸入法**簡化字確定性**。
- 「國字」是指臺灣《常用國字標準字體表》中的 4808 個繁體漢字。測試輸入法**繁體字確定性**。
- 「常用繁簡」是指大陸《通用規範漢字表》一二級的 6500 個漢字、臺灣《常用國字標準字體表》中的 4888 個漢字、以及《古籍印刷通用規範》中的 125 個大陸繁體字形 [^mainland_shape]。總共爲 8390 個常用繁簡漢字。測試輸入法**繁簡混合文本下的確定性**。
- GB2312 是大陸信息技術簡化字集，共有簡化漢字 6764 個。
- GBK 是大陸的信息技術大字集，共有繁簡漢字 21003 個。
- **靜態重碼數**指的是一個字集範圍內，編碼相同的漢字的絕對數量，反映出了輸入法在檢字方面的確定性。
- **動態選重率**指的是用字頻數據對重碼漢字進行加權。因爲存在五碼自動頂一選，只有在二選或三選時才需要選重。這個指標更能反映實際的輸入體驗。
- 注意，動態重碼率基於字頻數據，不同的字頻統計會產生不同結果。我採用的字頻數據，簡體來自北京師範大學邢紅兵的 [《25 億字語料漢字字頻表》](https://faculty.blcu.edu.cn/xinghb/zh_CN/article/167473/content/1437.htm)，繁體來自 [繁體字頻表](https://language.moe.gov.tw/001/Upload/files/SITE_CONTENT/M0001/PIN/biau1.htm?open)。

### 單字重碼計算公式

假設 $Z$ 爲一個漢字的集合，$M$ 爲一個編碼的集合，$p:Z\rightarrow [0,1]$ 爲漢字到某文本狀態下單字頻率的映射。
用編碼和字頻對漢字排序，使漢字 $z_{ij}$ 是編碼爲 $m_i$ 的第 $j$ 個漢字，$i \in I$, $j \in J_i$, 且滿足 $a\geq b$ 時，$f(z_{ia})\geq f(z_{ib})$.

那麽，靜態重碼數可以表達爲：

$$N_{s} = \mid \{z_{ia}, z_{ib}  \text{ if } M(z_{ia}) = M(z_{ib}) \text{ for all } a,b \in J_i \text{ and } i \in I \}.$$

動態重碼率可以表達爲：
$$N_{d} = \sum\limits_{i \in I, j \in J_i/\{1\}} p(z_{ij}).$$

### 單字全碼數據

以下爲單字全碼的結果。表格按輸入法的性質排列。

| 形碼方案     | 簡體<br>選重率 | 繁體<br>選重率 | 繁簡混合<br>選重率 | GB2312 | 國字<br>常用 |   GBK | CJK-B | CJK-D | CJK-F | CJK-H | CJK-I |
| :----------- | -------------: | -------------: | -----------------: | -----: | -----------: | ----: | ----: | ----: | ----: | ----: | ----: |
| **四碼**     |                |                |                    |        |              |       |       |       |       |       |       |
| 五筆86       |          34.2‱ |          77.7‱ |             238.3‱ |    521 |          333 |  6453 | 36494 |     - |     - |     - |     - |
| 五筆98       |          31.8‱ |          79.5‱ |             240.0‱ |    515 |          330 |  6378 |     - |     - |     - |     - |     - |
| 五筆06       |          31.8‱ |          83.8‱ |             236.3‱ |    532 |          387 |  6610 |     - |     - |     - |     - |     - |
| 五笔986      |          34.2‱ |          61.7‱ |             231.2‱ |    441 |          294 |  6120 |     - |     - |     - |     - |     - |
| 米十五笔     |          26.8‱ |          28.4‱ |             205.9‱ |    285 |          144 |     - |     - |     - |     - |     - |     - |
| 藍寶石2      |          21.6‱ |          57.3‱ |              58.4‱ |    388 |          284 |  5082 |     - |     - |     - |     - |     - |
| 藍寶石3      |           9.7‱ |              - |                  - |    392 |            - |     - |     - |     - |     - |     - |     - |
| 鄭碼         |          59.0‱ |          83.6‱ |             262.8‱ |    559 |          316 |  6631 | 36159 | 39353 |     - |     - |     - |
| 真碼         |           6.4‱ |          45.9‱ |             151.2‱ |    406 |          184 |  4328 | 35120 | 38397 | 48575 | 56168 | 56706 |
| 徐碼         |          10.7‱ |          22.8‱ |              24.9‱ |    318 |          127 |  2902 | 25605 | 27956 | 35746 |     - |     - |
| 嘸蝦米       |              - |          72.5‱ |             814.6‱ |      - |           98 |     - |     - |     - |     - |     - |     - |
| 宇浩光華     |           4.1‱ |          15.1‱ |              15.6‱ |    316 |          198 |  5168 | 33199 | 35874 | 44495 | 50667 | 51126 |
| 宇浩星陳     |           7.8‱ |          10.9‱ |              14.9‱ |    412 |          149 |  4918 | 33183 | 36032 | 45016 | 51706 | 52200 |
| 卿雲         |           7.6‱ |           7.6‱ |              13.0‱ |    532 |          192 |  6145 | 37132 | 40186 | 49809 | 56865 | 57387 |
| 雲碼         |           4.8‱ |           6.5‱ |              10.5‱ |    287 |           97 |  3877 | 29902 | 32503 | 40870 | 46990 | 47429 |
| 天碼         |           9.2‱ |          26.4‱ |              57.4‱ |    471 |          299 |  5547 | 33457 | 36251 | 45116 | 51685 | 52157 |
| **五碼**     |                |                |                    |        |              |       |       |       |       |       |       |
| 倉頡五代     |          25.9‱ |          57.0‱ |              51.0‱ |    422 |          164 |     - |     - |     - |     - |     - |     - |
| 蒼頡六代     |          25.3‱ |          39.6‱ |              40.0‱ |    384 |          113 |     - | 17949 | 19590 | 25415 | 29603 |     - |
| **三碼出簡** |                |                |                    |        |              |       |       |       |       |       |       |
| 三鄭250簡    |          51.4‱ |         281.2‱ |             386.5‱ |   2677 |         1568 | 16472 |     - |     - |     - |     - |     - |
| 吉旦餅30簡   |          37.8‱ |          62.6‱ |              85.7‱ |   2244 |          987 | 15949 | 68356 | 72903 | 86503 | 95844 | 96472 |
| 易碼676簡    |           5.8‱ |              - |                  - |   1324 |            - |     - |     - |     - |     - |     - |     - |
| **不定長**   |                |                |                    |        |              |       |       |       |       |       |       |
| 山人全息     |           6.4‱ |          39.0‱ |             246.1‱ |    192 |           84 |  3948 |     - |     - |     - |     - |     - |
| **音形**     |                |                |                    |        |              |       |       |       |       |       |       |
| 小鶴音形     |          85.5‱ |              - |                  - |      - |            - |     - |     - |     - |     - |     - |     - |
| **形音**     |                |                |                    |        |              |       |       |       |       |       |       |
| 字源         |          46.8‱ |              - |                  - |    294 |            - |     - |     - |     - |     - |     - |     - |

### 二級簡碼出簡不出全數據

以下爲二級簡碼出簡不出全的結果，換句話説，如果一個字存在一級和二級簡碼，則默認只打簡碼，並將其全碼後置。部分方案設置了兩重二級簡碼字，數據無法準確計算，故而略去。注意，真碼只設置一級簡碼，不設置二級簡碼。表格按輸入法的性質排列：

| 形碼方案   | 簡體<br>選重率 | 繁體<br>選重率 | 繁簡混合<br>選重率 | GB2312 | 國字<br>常用 |   GBK | CJK-B | CJK-D | CJK-F | CJK-H | CJK-I |
| :--------- | -------------: | -------------: | -----------------: | -----: | -----------: | ----: | ----: | ----: | ----: | ----: | ----: |
| **四碼**   |                |                |                    |        |              |       |
| 五筆86     |          21.8‱ |          69.0‱ |             168.5‱ |    451 |          293 |  6111 | 35953 |     - |     - |     - |     - |
| 藍寶石2    |           5.2‱ |          36.9‱ |              30.7‱ |    301 |          245 |  4815 |     - |     - |     - |     - |     - |
| 藍寶石3    |           2.3‱ |              - |                  - |    299 |            - |     - |     - |     - |     - |     - |     - |
| 鄭碼       |          24.5‱ |          47.7‱ |             152.2‱ |    460 |          283 |  6405 | 35853 | 39035 |     - |     - |     - |
| 真碼       |           4.4‱ |          44.9‱ |             148.9‱ |    380 |          172 |  4316 | 35126 | 38404 | 48585 | 56174 | 56712 |
| 徐碼       |           9.1‱ |          19.0‱ |              19.1‱ |    353 |          119 |  2871 | 25378 | 27721 | 35456 |     - |     - |
| 宇浩光华   |           3.2‱ |          14.0‱ |              13.8‱ |   2118 |         1517 | 15171 | 64467 | 68843 | 82077 | 91208 | 91830 |
| 宇浩星陈   |           6.0‱ |           9.5‱ |              12.7‱ |    357 |          127 |  4720 | 32791 | 35618 | 44549 | 51221 | 51716 |
| 卿雲       |           3.7‱ |           6.1‱ |               9.7‱ |    454 |          169 |  5915 | 36746 | 39806 | 49415 | 56441 | 56966 |
| 雲碼       |           3.5‱ |           5.5‱ |               7.8‱ |    259 |           85 |  3735 | 29522 | 32105 | 40433 | 46539 | 46976 |
| 天碼       |           8.0‱ |          22.0‱ |              37.1‱ |    429 |          284 |  5399 | 33146 | 35937 | 44781 | 51328 | 51798 |
| **三碼**   |                |                |                    |        |              |       |
| 三碼鄭碼   |          51.4‱ |         281.1‱ |             379.4‱ |   2700 |         1578 |     - |     - |     - |     - |     - |     - |
| 吉旦餅     |          37.8‱ |          62.6‱ |              85.7‱ |   2244 |          987 | 15949 | 68356 | 72903 | 86503 | 95844 | 96472 |
| **不定長** |
| 山人全息   |           5.0‱ |          38.1‱ |             141.1‱ |    499 |          266 |  4430 |     - |     - |     - |     - |     - |
| **形音**   |                |                |                    |        |              |       |       |       |       |       |       |
| 字源       |           9.5‱ |              - |                  - |    209 |            - |     - |     - |     - |     - |     - |     - |

## 詞語重碼數據

### 詞語重碼定義

表格中的各項名稱定義如下：

- **詞語完美動態選重率**指的是用詞頻數據對重碼詞語（包括單字詞和多字詞）進行加權後得到的選重的頻率。
- **單字動態選重率**指的是使用極端保守的分詞法，即所有多字詞全部視作單字詞輸入時選重的頻率。
- **實際動態選重率**指的是在實際輸入過程中，因爲用戶分詞和字頻表分詞的差異造成的偏差所造成的選重率。介於「單字動態選重率」（極端保守分詞）和「詞語完美動態選重率」（完美分詞）之間。因爲用戶輸入了詞庫中不存在的詞而導致的回刪，不算入此內。
- 因爲存在五碼自動頂一選，只有在二選或三選時才需要選重。
- 動態重碼率對詞頻數據的依賴度極高，不同的詞頻統計會產生不同結果。本文采用的詞頻數據，來自《現代漢語語料庫分詞類詞頻表》。

::: info 詞語完美動態選重率
這裡給出對於「詞語完美動態選重率」的一個直觀解釋。假設存在這樣一個句子：

「請用大約十句話來描述你所居住城市的歷史的來龍去脈。」

情況一：如果詞庫爲**中等大小**，換言之，分詞比較適中，我們對這句話進行如下分割：

「請·用·大約·十句·話·來·描述·你·所·居住·城市·歷史·的·來龍去脈。」

我們得到了 14 個詞語，也就是説，用戶要輸入 14 次全碼。假設「請」和「描述」發生了重碼，那麽我們輸入這 14 個詞，就要選重一次。這句話的詞語動態選重率就是 1 / 13 = 7.1%。

情況二：如果詞庫爲**超大詞庫**，換言之，分詞比較激進，我們對這句話進行如下分割：

「請用·大約·十句話·來·描述·你所·居住·城市·歷史的·來龍去脈。」

我們得到了 10 個詞語，也就是説，用戶要輸入 10 次全碼。假設「請用」和「描述」發生了重碼，那麽我們輸入這 10 個詞，就要選重一次。這句話的詞語動態選重率就是 1 / 10 = 10.0%。

情況三：如果詞庫爲**精簡詞庫**，換言之，分詞比較保守，我們對這句話進行如下分割：

「請·用·大約·十·句·話·來·描述·你·所·居住·城市·歷史·的·來·龍·去·脈。」

我們得到了 18 個詞語，也就是説，用戶要輸入 18 次全碼。假設「請」和「描述」發生了重碼，那麽我們輸入這 18 個詞，就要選重一次。這句話的詞語動態選重率就是 1 / 18 = 5.56%。

一個基本的經驗 (rule of thumb) 是：分詞越激進、詞庫越大，那麽「詞語完美動態選重率」就越高，同時平均碼長也越短。
:::

::: tip 結論
從上例可以看出，詞語的重碼數據，極度依賴於用戶的「人工分詞」和統計數據中的詞語的一致性。只有在以下條件**全部**滿足時，數據才會比較準確：

- 用戶只打詞頻表中出現的詞。如：詞頻表中若無「我們」，那麽用戶只打「我·們」。
- 用戶必定打長度較長的詞。如：出現「電視機」時，必定打「電視機」，而不是「電視·機」或「電·視·機」。這一條也意味着，一個多字詞若在字頻表中，那麽用戶絕對不會打成單字。

因爲這兩個條件過於完美，實際使用時對用戶的分詞壓力高，所以一般不會實現。很多時候，用戶會將某些詞頻表中的多字詞分爲單字詞輸入，這意味着：

實際輸入時的動態選重率，應介於「單字動態選重率」和「詞語完美動態選重率」之間。依照用戶習慣：

- 如果一個人偏好打單字，那麽動態選重率更偏向「單字動態選重率」（更低）。
- 如果一個人偏好打詞語，那麽動態選重率更偏向「詞語動態選重率」（更高）。

因此，**精簡詞庫配合單字輸入**，是平衡碼長（效率）和選重（確定性）的一個解決方案，適合新手。而**背誦字詞簡碼和選重位置**也是提高確定性的一種方式，適合老手。
:::

### 詞語重碼計算公式

假設$W$爲一個詞語的集合，詞長大於等於 1。 $M$ 爲一個編碼的集合。一段文本$T$可以被貪婪地分割爲$W$的組合。統計每一個詞語的概率，定義$p:W\rightarrow [0,1]$ 爲詞語到其出現頻率的映射。
用編碼和頻率對詞語排序，使詞語 $w_{ij}$ 是編碼爲 $m_i$ 的第 $j$ 個項目，$i \in I$, $j \in J_i$, 且滿足 $a\geq b$ 時，$f(w_{ia})\geq f(w_{ib})$.

那麽，詞語完美動態選重率可以表達爲：
$$N_{d} = \sum\limits_{i \in I, j \in J_i/\{1\}} p(w_{ij}).$$

::: warning 提醒
在部分指標計算軟件中，詞語選重率只包括了多字詞，不能成詞的單字詞被移除，例如，「我今天去那裡」被分割成「今天  那裡」，一共有 2 個詞語。倘若「我」和「那裡」生了重碼，則選重率爲 0 / 2 = 0%。這不能完全反應實際打字時的選重頻率。
:::

### 詞語重碼結果

::: warning 注意
下表內容僅適用於**現代漢語典範白話文**的文本空間。  
實際動態選重率，應介於「單字動態選重率」（極端保守分詞）和「詞語完美動態選重率」（完美分詞）之間。
:::

<!-- 
單字全碼數據。也就是説，單字全碼在詞語全碼之前。

| 方案     | 簡體詞語<br>完美動態選重率 | 繁體詞語<br>完美動態選重率 | 繁簡混合詞語<br>完美動態選重率 |
| :------- | -------------------------: | -------------------------: | -----------------------------: |
| 藍寶石 3 |                      45.9‱ |                          - |                              - |
| 藍寶石 2 |                      48.4‱ |                      89.3‱ |                         199.0‱ |
| 雲碼     |                     103.1‱ |                     106.7‱ |                         245.3‱ |
| 卿雲     |                     107.3‱ |                     111.5‱ |                         295.8‱ |
| 宇浩光華 |                     116.0‱ |                     129.3‱ |                         311.7‱ |
| 徐碼 23  |                     116.3‱ |                     131.2‱ |                         316.7‱ |
| 天碼     |                     115.3‱ |                     116.0‱ |                         356.1‱ |
| 宇浩星陳 |                     127.2‱ |                     144.4‱ |                         302.6‱ |
| 字源     |                     129.8‱ |                          - |                              - |
| 五筆 86  |                     204.1‱ |                     235.6‱ |                         750.2‱ |
| 五筆 98  |                     204.2‱ |                     242.7‱ |                         733.5‱ |
| 五筆 06  |                     217.8‱ |                     238.3‱ |                         749.6‱ |
 -->

單字一簡、二簡出簡不出全數據。也就是説，有一簡、二簡的單字，全碼在詞語全碼之後。

| 方案     | 簡體詞語<br>完美動態選重率 | 繁體詞語<br>完美動態選重率 | 繁簡混合詞語<br>完美動態選重率 |
| :------- | -------------------------: | -------------------------: | -----------------------------: |
| 藍寶石 3 |                      45.9‱ |                          - |                              - |
| 藍寶石 2 |                      48.4‱ |                      89.3‱ |                         199.0‱ |
| 雲碼     |                     103.1‱ |                     106.7‱ |                         245.3‱ |
| 卿雲     |                     107.3‱ |                     111.5‱ |                         295.8‱ |
| 宇浩光華 |                     116.0‱ |                     129.3‱ |                         311.7‱ |
| 徐碼 23  |                     116.3‱ |                     131.2‱ |                         316.7‱ |
| 天碼     |                     115.3‱ |                     116.0‱ |                         356.1‱ |
| 宇浩星陳 |                     127.2‱ |                     144.4‱ |                         302.6‱ |
| 字源     |                     129.8‱ |                          - |                              - |
| 五筆 86  |                     204.1‱ |                     235.6‱ |                         750.2‱ |
| 五筆 98  |                     204.2‱ |                     242.7‱ |                         733.5‱ |
| 五筆 06  |                     217.8‱ |                     238.3‱ |                         749.6‱ |

## 候選項個數·檢字效率

本節給出各個字集中、重碼最多的碼位上候選項的個數。本指標可以有效反映輸入方案在大字集上的**檢字**效率。

該數字不大於 9，則可以不用翻頁；該數字不大於 18，則只需要翻頁一次。

| 形碼方案 | GB2312 | 國字<br>常用 |  GBK | CJK-B | CJK-D | CJK-F | CJK-H | CJK-I |
| :------- | -----: | -----------: | ---: | ----: | ----: | ----: | ----: | ----: |
| 五筆 86  |     21 |            4 |   21 |    44 |     - |     - |     - |     - |
| 五筆 98  |      4 |            4 |   13 |     - |     - |     - |     - |     - |
| 五筆 06  |      4 |            4 |   13 |     - |     - |     - |     - |     - |
| 藍寶石 2 |      3 |            4 |   10 |     - |     - |     - |     - |     - |
| 藍寶石 3 |      4 |            - |    - |     - |     - |     - |     - |     - |
| 鄭碼     |      3 |            4 |    7 |    18 |    19 |     - |     - |     - |
| 真碼     |      4 |            4 |   13 |    43 |    44 |    46 |    46 |    46 |
| 徐碼     |      3 |            3 |    7 |    17 |    17 |    17 |     - |     - |
| 嘸蝦米   |      3 |            2 |    - |     - |     - |     - |     - |     - |
| 宇浩光華 |      3 |            3 |    7 |    14 |    14 |    15 |    16 |    16 |
| 宇浩星陳 |      4 |            3 |    6 |    15 |    15 |    17 |    18 |    18 |
| 卿雲     |      3 |            3 |    6 |    16 |    17 |    17 |    18 |    18 |
| 雲碼     |      3 |            3 |    5 |    13 |    13 |    14 |    14 |    14 |
| 天碼     |      3 |            4 |    6 |    13 |    13 |    14 |    15 |    15 |
| 倉頡五代 |      3 |            2 |    6 |    32 |    34 |     - |     - |     - |
| 蒼頡六代 |      3 |            3 |    5 |    11 |    11 |    11 |    12 |     - |
| 小鶴音形 |      4 |            - |    - |     - |     - |     - |     - |     - |
| 山人全息 |      2 |            2 |    5 |     9 |     9 |     - |     - |     - |
| 字源     |      4 |            - |    - |     - |     - |     - |     - |     - |

## 古今名著選重頻率統計

這裡給出部分名著的選重頻率統計。四本簡體、三本繁體、三本繁簡混排。

::: info 現象
文本越趨近於**現代漢語典範白話文**，其重碼數據越符合前面幾章所展示的「動態選重率」。文本越趨近於**古漢語**、**詩詞歌賦**，其重碼數據越符合前面幾章所展示的「靜態重碼數」。
:::

### 單字全碼數據

以下爲單字全碼的結果（三碼方案默認出簡）。

| 方案     | 毛澤東選集（簡） | 天龍八部（簡） | 三體三部曲（簡） | 戰爭與和平（簡） |
| :------- | ---------------: | -------------: | ---------------: | ---------------: |
| 五筆86   |            25.8‱ |          30.6‱ |            25.7‱ |            20.9‱ |
| 五筆98   |            31.3‱ |          28.4‱ |            26.5‱ |            33.2‱ |
| 五筆06   |            22.2‱ |          25.5‱ |            24.3‱ |            37.1‱ |
| 藍寶石2  |            18.4‱ |          20.5‱ |            24.9‱ |            18.1‱ |
| 藍寶石3  |             8.1‱ |          10.2‱ |             3.7‱ |             4.7‱ |
| 鄭碼     |            44.2‱ |          51.6‱ |            49.2‱ |            48.1‱ |
| 真碼     |             5.1‱ |          13.9‱ |             5.1‱ |             6.5‱ |
| 徐碼     |             3.3‱ |           9.8‱ |             7.0‱ |             7.8‱ |
| 宇浩光華 |             1.2‱ |           2.9‱ |             2.7‱ |             2.4‱ |
| 宇浩星陳 |             3.5‱ |           6.4‱ |             2.3‱ |             6.2‱ |
| 卿雲     |             3.3‱ |          10.9‱ |             4.8‱ |             5.6‱ |
| 雲碼     |             1.1‱ |           3.1‱ |             4.1‱ |             6.6‱ |
| 天碼     |             3.5‱ |           7.2‱ |             4.5‱ |             6.0‱ |
| 倉頡五代 |            74.0‱ |          71.1‱ |            80.2‱ |            60.0‱ |
| 蒼頡六代 |            62.5‱ |          65.0‱ |            61.0‱ |            43.1‱ |
| 三碼鄭碼 |             9.7‱ |          47.3‱ |            26.4‱ |            29.5‱ |
| 吉旦餅   |            13.8‱ |          41.6‱ |            16.2‱ |            23.6‱ |
| 山人全息 |             2.4‱ |           6.8‱ |             5.6‱ |             6.1‱ |
| 小鹤音形 |            81.7‱ |          84.2‱ |            74.2‱ |            69.6‱ |
| 字源     |            39.1‱ |          50.9‱ |            39.7‱ |            34.0‱ |

| 方案     | 史記（繁） | 紅樓夢（繁） | 笑傲江湖（繁） |
| :------- | ---------: | -----------: | -------------: |
| 五筆86   |      88.4‱ |        28.9‱ |          46.7‱ |
| 五筆98   |      69.3‱ |        32.5‱ |          48.8‱ |
| 五筆06   |      79.7‱ |        35.3‱ |          49.2‱ |
| 藍寶石2  |      43.8‱ |        25.3‱ |          29.9‱ |
| 鄭碼     |      89.9‱ |        39.2‱ |          32.2‱ |
| 真碼     |      30.1‱ |        12.9‱ |          14.0‱ |
| 徐碼     |      22.1‱ |        10.9‱ |           9.1‱ |
| 宇浩光華 |      25.9‱ |         9.2‱ |           6.5‱ |
| 宇浩星陳 |      32.7‱ |         9.4‱ |           7.3‱ |
| 卿雲     |      24.2‱ |         7.0‱ |           5.9‱ |
| 雲碼     |      15.5‱ |         3.9‱ |           2.8‱ |
| 天碼     |      39.6‱ |        18.8‱ |          12.6‱ |
| 倉頡五代 |      74.6‱ |        33.0‱ |          30.9‱ |
| 蒼頡六代 |      69.3‱ |        16.4‱ |          14.2‱ |
| 三碼鄭碼 |     296.1‱ |       143.8‱ |         132.3‱ |
| 吉旦餅   |     115.5‱ |        54.4‱ |          34.3‱ |
| 山人全息 |      20.8‱ |         6.3‱ |           3.2‱ |

| 方案     | 論語集解（繁簡混） | 三國演義（繁簡混） | 海上花列傳（繁簡混） |
| :------- | -----------------: | -----------------: | -------------------: |
| 五筆86   |             260.8‱ |             360.8‱ |               244.6‱ |
| 五筆98   |             265.7‱ |             374.8‱ |               242.5‱ |
| 五筆06   |             252.5‱ |             345.7‱ |               232.7‱ |
| 藍寶石2  |              20.5‱ |              52.7‱ |                35.6‱ |
| 鄭碼     |             266.7‱ |             385.9‱ |               311.2‱ |
| 真碼     |             147.5‱ |             165.2‱ |               174.9‱ |
| 徐碼     |              10.3‱ |              39.2‱ |                22.7‱ |
| 宇浩光華 |               4.4‱ |              24.5‱ |                 9.6‱ |
| 宇浩星陳 |               3.9‱ |              32.2‱ |                18.1‱ |
| 卿雲     |               4.4‱ |              24.6‱ |                10.6‱ |
| 雲碼     |               7.8‱ |              21.8‱ |                13.1‱ |
| 天碼     |              45.9‱ |              71.9‱ |                47.3‱ |
| 倉頡五代 |              67.4‱ |             144.6‱ |                88.3‱ |
| 蒼頡六代 |              38.6‱ |             129.6‱ |                83.4‱ |
| 三碼鄭碼 |             330.2‱ |             562.3‱ |               395.4‱ |
| 吉旦餅   |              70.3‱ |             119.4‱ |                96.4‱ |
| 山人全息 |             281.3‱ |             352.3‱ |               314.7‱ |

### 二級簡碼出簡不出全數據

以下爲二級簡碼出簡不出全的結果，換句話説，如果一個字存在一級和二級簡碼，則默認只打簡碼，並將其全碼後置。部分方案設置了兩重二級簡碼字，數據無法準確計算，故而略去。注意，真碼只設置一級簡碼，不設置二級簡碼。

| 輸入方案 | 毛澤東選集（簡） | 天龍八部（簡） | 三體三部曲（簡） | 戰爭與和平（簡） |
| :------- | ---------------: | -------------: | ---------------: | ---------------: |
| 五筆86   |             5.7‱ |          15.6‱ |            12.1‱ |             9.0‱ |
| 藍寶石2  |             3.8‱ |           5.6‱ |             1.7‱ |             2.2‱ |
| 真碼     |            36.4‱ |          21.8‱ |            35.1‱ |            24.1‱ |
| 徐碼     |             3.2‱ |           7.9‱ |             5.8‱ |             7.3‱ |
| 宇浩光華 |             1.0‱ |           2.4‱ |             2.4‱ |             2.0‱ |
| 宇浩星陳 |             3.3‱ |           5.2‱ |             1.7‱ |             4.5‱ |
| 卿雲     |             1.4‱ |           3.3‱ |             1.6‱ |             4.0‱ |
| 雲碼     |             0.9‱ |           2.2‱ |             1.7‱ |             6.1‱ |
| 天碼     |             3.0‱ |           5.7‱ |             3.6‱ |             4.8‱ |
| 三碼鄭碼 |             9.5‱ |          46.8‱ |            26.2‱ |            29.4‱ |
| 吉旦餅   |            15.4‱ |          44.7‱ |            26.1‱ |            35.6‱ |
| 易碼     |             1.5‱ |           4.8‱ |             1.7‱ |             2.8‱ |
| 山人全息 |           129.9‱ |         173.6‱ |           152.3‱ |           152.5‱ |
| 小鹤音形 |            81.7‱ |          84.2‱ |            74.2‱ |            69.6‱ |
| 字源     |             5.3‱ |          12.0‱ |             6.8‱ |             9.7‱ |

| 輸入方案 | 史記（繁） | 紅樓夢（繁） | 笑傲江湖（繁） |
| :------- | :--------- | :----------- | :------------- |
| 五筆86   | 75.0‱      | 24.1‱        | 35.0‱          |
| 藍寶石2  | 35.3‱      | 20.4‱        | 19.5‱          |
| 真碼     | 50.0‱      | 20.2‱        | 29.4‱          |
| 徐碼     | 23.6‱      | 10.2‱        | 8.0‱           |
| 宇浩光華 | 22.9‱      | 8.3‱         | 5.6‱           |
| 宇浩星陳 | 29.8‱      | 8.6‱         | 6.6‱           |
| 卿雲     | 36.7‱      | 18.6‱        | 21.6‱          |
| 雲碼     | 14.0‱      | 3.3‱         | 2.4‱           |
| 天碼     | 33.7‱      | 17.0‱        | 11.0‱          |
| 三碼鄭碼 | 294.8‱     | 142.6‱       | 131.0‱         |
| 吉旦餅   | 114.0‱     | 63.3‱        | 57.3‱          |
| 山人全息 | 117.7‱     | 99.9‱        | 109.6‱         |

| 輸入方案 | 論語集解（繁簡混） | 三國演義（繁簡混） | 海上花列傳（繁簡混） |
| :------- | -----------------: | -----------------: | -------------------: |
| 五筆86   |             192.0‱ |             242.8‱ |               187.5‱ |
| 藍寶石2  |               9.8‱ |              43.9‱ |                17.0‱ |
| 真碼     |             193.4‱ |             174.2‱ |               175.7‱ |
| 徐碼     |              12.7‱ |              35.5‱ |                27.7‱ |
| 宇浩光華 |               3.9‱ |              21.5‱ |                 8.4‱ |
| 宇浩星陳 |               2.9‱ |              29.5‱ |                16.6‱ |
| 卿雲     |              20.0‱ |              47.8‱ |                32.2‱ |
| 雲碼     |               7.8‱ |              18.8‱ |                10.4‱ |
| 天碼     |              38.1‱ |              56.0‱ |                30.9‱ |
| 三碼鄭碼 |             337.5‱ |             555.2‱ |               398.3‱ |
| 吉旦餅   |              41.5‱ |             154.7‱ |               104.1‱ |
| 山人全息 |             415.6‱ |             686.1‱ |               597.8‱ |

上表反映的是確定性，而平均碼長則反映輸入效率。現統計如下。注意，真碼只設置一級簡碼，不設置二級簡碼。

| 輸入方案 | 簡體<br>均值 | 毛澤東<br>選集·簡 | 天龍<br>八部·簡 | 三體<br>·簡 | 戰爭與<br>和平·簡 | 史記<br>·繁 | 紅樓<br>夢·繁 | 笑傲<br>江湖·繁 | 論語集解<br>·繁簡混 |
| :------- | -----------: | ----------------: | --------------: | ----------: | ----------------: | ----------: | ------------: | --------------: | ------------------: |
| 藍寶石2  |         3.05 |              3.04 |             3.1 |        3.03 |              3.05 |        3.48 |          3.29 |            3.29 |                3.36 |
| 雲碼     |         3.06 |              3.02 |            3.11 |        3.04 |              3.08 |        3.46 |          3.29 |            3.29 |                 3.3 |
| 藍寶石3  |         3.07 |              3.03 |            3.12 |        3.05 |              3.07 |        2.51 |           2.2 |            2.26 |                2.92 |
| 宇浩光華 |          3.1 |              3.13 |            3.13 |        3.07 |              3.09 |        3.52 |          3.29 |             3.3 |                 3.4 |
| 宇浩星陳 |         3.12 |              3.12 |            3.14 |         3.1 |              3.12 |        3.51 |          3.29 |             3.3 |                3.35 |
| 五筆06   |         3.14 |              3.06 |            3.19 |        3.13 |              3.18 |        3.47 |          3.33 |            3.34 |                3.37 |
| 五筆98   |         3.16 |              3.06 |            3.22 |        3.16 |               3.2 |        3.46 |          3.36 |            3.36 |                3.34 |
| 徐碼     |         3.18 |              3.15 |            3.21 |        3.18 |              3.17 |        3.49 |          3.32 |            3.33 |                3.33 |
| 天碼     |         3.18 |              3.19 |            3.21 |        3.15 |              3.16 |         3.5 |          3.34 |            3.37 |                3.33 |
| 五筆86   |         3.22 |              3.12 |            3.31 |        3.21 |              3.24 |        3.59 |          3.44 |            3.45 |                3.49 |
| 鄭碼     |         3.23 |              3.18 |            3.31 |        3.19 |              3.23 |        3.54 |           3.4 |            3.41 |                3.49 |
| 卿雲     |         3.24 |              3.26 |            3.27 |        3.22 |              3.21 |        3.51 |          3.39 |            3.38 |                3.38 |
| 真碼     |         3.49 |              3.45 |            3.53 |        3.46 |              3.52 |        3.69 |          3.62 |             3.6 |                3.62 |

## 手感·人體工學

### 速度當量

全碼速度當量如下。

| 輸入方案·用鍵數量 | 簡體速度當量 | 繁體速度當量 | 繁簡速度當量 |
| :---------------- | -----------: | -----------: | -----------: |
| 卿雲·26鍵         |       1.2652 |       1.2579 |       1.2616 |
| 易碼·26鍵         |       1.2865 |            - |            - |
| 吉旦餅·26鍵       |        1.295 |         1.31 |       1.3025 |
| 雲碼·26鍵         |       1.3008 |       1.3058 |       1.3033 |
| 宇浩星陳·26鍵     |       1.3017 |       1.3058 |       1.3038 |
| 蒼頡六代·25鍵     |       1.3063 |       1.3302 |       1.3183 |
| 藍寶石2·25鍵      |       1.3079 |       1.3302 |       1.3191 |
| 宇浩光華·25键     |       1.3201 |       1.3307 |       1.3254 |
| 山人全息·26鍵     |       1.3249 |       1.3349 |       1.3299 |
| 藍寶石3·25鍵      |       1.3294 |            - |            - |
| 倉頡五代·25鍵     |       1.3343 |       1.3368 |       1.3356 |
| 真碼·25鍵         |        1.337 |       1.3588 |       1.3479 |
| 鄭碼·26鍵         |       1.3451 |       1.3473 |       1.3462 |
| 五筆86·25鍵       |        1.354 |       1.3592 |       1.3566 |
| 字源·26键         |       1.3558 |            - |            - |
| 五筆98·25鍵       |       1.3587 |       1.3643 |       1.3615 |
| 五筆06·25鍵       |       1.3636 |       1.3655 |       1.3646 |
| 徐碼·26鍵         |       1.3865 |       1.3679 |       1.3772 |
| 天碼·26鍵         |       1.3942 |       1.3865 |       1.3904 |

出一簡、二簡、三簡後速度當量如下。

| 輸入方案·用鍵數量 | 簡體速度當量 | 繁體速度當量 | 繁簡速度當量 |
| :---------------- | -----------: | -----------: | -----------: |
| 卿雲·26鍵         |       1.2795 |       1.2645 |        1.272 |
| 易碼·26鍵         |       1.2865 |            - |            - |
| 吉旦餅·26鍵       |       1.2924 |       1.3032 |       1.2978 |
| 宇浩星陳·26鍵     |       1.2939 |       1.3024 |       1.2982 |
| 雲碼·26鍵         |       1.2976 |       1.3051 |       1.3014 |
| 藍寶石3·25鍵      |       1.3003 |            - |            - |
| 藍寶石2·25鍵      |       1.3069 |       1.3222 |       1.3146 |
| 字源·26键         |         1.31 |            - |            - |
| 宇浩光華·25键     |       1.3187 |       1.3273 |        1.323 |
| 山人全息·26鍵     |       1.3196 |       1.3201 |       1.3198 |
| 鄭碼·26鍵         |       1.3239 |       1.3261 |        1.325 |
| 天碼·26鍵         |       1.3283 |        1.338 |       1.3331 |
| 真碼·25鍵         |       1.3327 |       1.3542 |       1.3435 |
| 五筆98·25鍵       |       1.3382 |       1.3537 |       1.3459 |
| 五筆86·25鍵       |       1.3397 |       1.3547 |       1.3472 |
| 倉頡五代·25鍵     |       1.3402 |       1.3445 |       1.3423 |
| 徐碼23·26鍵       |       1.3414 |        1.341 |       1.3412 |
| 五筆06·25鍵       |       1.3454 |       1.3565 |        1.351 |

### 古今名著雙手互擊頻率

因爲宇浩輸入法是將字根按照鍵盤分區進行排布的，相對於全亂序字根排布的方案，雙手互擊方面有天生的劣勢。如果不進行優化，那麽會影響手感。這也是爲什麽宇浩輸入法的算法中，將雙手互擊率專門設置爲一個約束條件。

對於雙手互擊率，作者進行了以下的定義：給定一段**連續文本**，將其中的漢字以及逗號和句號轉換爲輸入方案的編碼，分別計算其單手連按的頻數和雙手互擊的頻數，則：「雙手互擊的頻數 / （雙手互擊的頻數 + 單手連按的頻數）」即爲雙手互擊率。

連續文本的雙手互擊率，可以用以下案例展示。「我今天去那裡」，編碼爲 qaggtobufgdihvvtvacjksij。出現了 14 次同手擊鍵，9 次雙手互擊，故而互擊率爲 39.13%。在連續文本情況下，單字全碼派和詞語派的雙手互擊率比較相近。

對於連續文本的雙手互擊率的優化，需要用到隱馬爾科夫鏈或者大樣本統計。算法中，需要計算每個漢字後下一個漢字的頻率，從而得到連續文本的雙手互擊率。

::: warning 注意
在部分指標計算軟件中，雙手互擊只包括了單字，例如，「我今天去那裡」被分割成 qagg tobu fgdi hvvt vacj ksij，出現了 9 次同手擊鍵，9 次雙手互擊，故而互擊率爲 50%。這種算法無法完全反應實際打字時的雙手互擊情況。
:::

下表列出了常見輸入方案對於古今名著時的雙手互擊率。表格按行均值降序排列，越靠前的方案，雙手互擊頻率越高。

| 輸入方案·用鍵數量 | 簡體<br>均值 | 毛澤東<br>選集·簡 | 天龍<br>八部·簡 | 三體<br>·簡 | 戰爭與<br>和平·簡 | 史記<br>·繁 | 紅樓<br>夢·繁 | 笑傲<br>江湖·繁 | 論語集解<br>·繁簡混 |
| :---------------- | -----------: | ----------------: | --------------: | ----------: | ----------------: | ----------: | ------------: | --------------: | ------------------: |
| 卿雲·26键         |       46.26% |            47.35% |          47.81% |      47.07% |            47.70% |      44.36% |        45.32% |          46.52% |              46.97% | 44.16% | 45.30% |
| 三碼杏碼·27鍵     |       45.88% |            46.06% |          46.45% |      46.77% |            46.31% |      43.80% |        45.77% |          47.06% |              46.59% | 45.96% | 44.03% |
| 易碼·26鍵         |       45.70% |            45.91% |          46.68% |      46.75% |            46.78% |      44.08% |        45.96% |          46.91% |              44.94% | 45.02% | 43.98% |
| C42·30 鍵         |       44.83% |            44.66% |          46.28% |      45.50% |            45.22% |      42.69% |        45.44% |          46.00% |              47.29% | 43.09% | 42.12% |
| 三碼吉旦餅·26 鍵  |       43.64% |            43.70% |          44.37% |      44.77% |            44.89% |      42.44% |        43.13% |          44.66% |              44.68% | 42.25% | 41.48% |
| 三碼貓碼·26 鍵    |       43.05% |            44.93% |          43.73% |      44.31% |            44.86% |      42.86% |        42.11% |          41.54% |              45.50% | 40.50% | 40.15% |
| 藍寶石 2·25 鍵    |       42.85% |            44.54% |          44.17% |      44.30% |            43.97% |      40.77% |        42.02% |          43.08% |              44.94% | 40.51% | 40.17% |
| 雲碼·26 鍵        |       41.97% |            43.52% |          42.45% |      42.84% |            43.29% |      42.45% |        41.27% |          42.01% |              39.71% | 41.26% | 40.91% |
| 蒼頡六代·25 鍵    |       40.65% |            40.49% |          40.09% |      40.52% |            41.12% |      39.66% |        40.86% |          41.64% |              39.85% | 40.52% | 41.71% |
| 宇浩星陳·26 鍵    |       40.26% |            40.59% |          40.49% |      40.89% |            41.62% |      38.22% |        40.25% |          40.49% |              40.40% | 38.69% | 40.93% |
| 倉頡五代·25 鍵    |       40.10% |            40.22% |          40.24% |      39.96% |            41.12% |      39.13% |        39.82% |          41.12% |              39.41% | 39.24% | 40.71% |
| 三碼鄭碼·26 鍵    |       38.89% |            38.80% |          39.31% |      39.96% |            40.66% |      38.17% |        37.97% |          38.03% |              40.85% | 37.91% | 37.24% |
| 藍寶石 3·25 鍵    |       38.75% |            38.00% |          39.91% |      38.12% |            38.14% |      37.54% |        39.57% |          41.33% |              37.71% | 38.76% | 38.41% |
| 真碼·25 鍵        |       38.61% |            40.38% |          39.67% |      40.56% |            39.15% |      37.69% |        38.62% |          38.32% |              36.51% | 37.76% | 37.43% |
| 鄭碼·26 鍵        |       38.54% |            36.70% |          38.86% |      38.56% |            39.12% |      38.90% |        37.98% |          37.92% |              39.50% | 38.53% | 39.29% |
| 宇浩光華·25 鍵    |       38.46% |            39.41% |          38.67% |      39.11% |            38.14% |      37.11% |        38.90% |          38.07% |              39.65% | 38.20% | 37.34% |
| 徐碼·26 鍵        |       37.97% |            37.92% |          37.61% |      37.35% |            37.17% |      38.56% |        37.99% |          37.00% |              39.06% | 38.51% | 38.57% |
| 山人全息·26 鍵    |       36.16% |            36.39% |          36.53% |      36.24% |            36.68% |      36.09% |        35.58% |          35.79% |              37.18% | 35.46% | 35.68% |
| 天碼·26 鍵        |       35.59% |            35.28% |          35.75% |      34.80% |            35.93% |      34.72% |        35.87% |          36.41% |              36.25% | 35.48% | 35.43% |
| 五筆 98·25 鍵     |       35.41% |            36.96% |          35.90% |      37.58% |            37.05% |      34.31% |        34.98% |          34.35% |              33.56% | 35.48% | 33.99% |
| 五筆 06·25 鍵     |       35.32% |            36.96% |          35.54% |      37.24% |            37.11% |      34.24% |        35.04% |          34.25% |              33.70% | 35.08% | 34.01% |
| 五筆 86·25 鍵     |       34.30% |            36.46% |          35.01% |      36.62% |            35.88% |      33.24% |        34.60% |          33.44% |              30.95% | 33.63% | 33.12% |

## 碼表來源

碼表數據基於：

- [宇浩]<https://zhuanlan.zhihu.com/p/614054514> 官方 QQ 群：735728797
- [卿雲] 官方 QQ 群：374630778
- [徐碼 13] 官方 QQ 群：218210590
- [徐碼 23] 官方 QQ 群：761401688
- [倉頡五代]<https://github.com/rime/rime-cangjie>
- [山人全息]<https://github.com/ywxt/rime-sunman>
- [五筆 06·新世紀]<https://github.com/byujiang/wubi06_rime>
- [張碼] 官方 QQ 群：77313896
- [藍寶石] 2023 年版 官方 QQ 群：111088239
- [092 五筆]<https://github.com/lvxingjia/092r>
- [小鶴]<https://github.com/cubercsl/rime-flypy>
- [雲碼]<https://github.com/orbitoo/kumo>
- [天碼] 官方 QQ 群：631302614

[^mainland_shape]: 蟶眾螄斕綉核飆淩轆痴刴戩粽㨃抬佈圇箇絝啟廡儕槪顴躋鉅鋭鎚床廏衹朶讞噁瑋旣蓽嬡偽蹟癟艶淼㑚紈餚攢樑噠韁曬崗壎濕灶殞揹瓚鵰痠鈺巘裡曁皂奬諏孃贇閆跥歎産顔頽摻爲絶昇繳躱薦閲謔卽才剮闕暘屌勳覷伲崟蹌饋駡曇躥翀熒鹵説唄龕裋衊㞞〇誒侷玅薈顎燼嬈缽檯吃摳鶩縐滷襬麵