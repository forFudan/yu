<script setup>
import Chaifen from '@/chaifen/Chaifen.vue'
</script>

# 進階討論

## 字形差異

漢字具有多態性。同一個漢字，在不同的標準、不同的字體下，存在一定的差別。有些字形上的差別，通過 Unicode 的離散來實現。比如`户` `戶` `戸`三字，在 Unicode 裡被安排在了不同的碼位上，故而實現了分離。但是很多漢字的不同字形，卻共用 Unicode 碼位（這其實是 CJK 的初衷），那麼這個字到底應該依照哪個標準來拆分，便成了問題。

宇浩輸入法的規定是：

- 每個字都有一種**標準拆法**，字形標準取自：The Unicode Standard, Version 15.0。各地區優先級降序為：GTHJKV，即陸、臺、港、日、韓、越。也就是說，如果存在大陸提交的標準，就依照大陸標準。如果大陸沒有提交標準，就按照臺灣標準。依此類推。
- 每個字都可能有若干**兼容拆法**，目的是兼容臺灣、香港、大陸古籍的字形標準。比如`起` = `走己`（大陸標準）和 `起` = `走巳`（臺灣標準）兼收。

宇浩輸入法的筆順選取，依照大陸標準《GF 3003-1999 GB13000.1 字符集漢字字序（筆畫序）規範》。同時，也兼容臺灣標準的筆順。

::: tip 例
比如`攀 = 木乂乂木手`（大陸標準）和`攀 = 乂乂木木手`（臺灣標準）兼收。

<div class="flex justify-left flex-wrap">
<Chaifen char='攀' :parts='[4,2,2,4,3,4]' :colors='[1,2,3,0,0,4]' />
陸
<Chaifen char='攀' :parts='[4,2,2,4,3,4]' :colors='[3,1,2,0,0,4]' />
臺
</div>

比如`與 = ⺽丂丄八`（大陸標準）和`與 = 丂丿⺽一八`（臺灣標準）兼收。
<div class="flex justify-left flex-wrap">
<Chaifen char='與' :parts='[4,2,1,3,1,2]' :colors='[1,2,3,1,3,4]' />
陸
<Chaifen char='與' :parts='[4,2,1,3,1,2]' :colors='[3,1,2,3,0,4]' />
臺
</div>
:::

## 書體差異

某些字根，即使在相同的規範下，也會楷體和宋體的不同而產生微小差異。這些差異往往會影響對於「散」「連」的判斷。我們主要以宋體為準（也是 CJK 的書體）進行拆分，同時有以下考量。

::: info 散連認定

1. `⼇`作頭時的`丶一`，無論書體，一概視為「散」。
<div class="flex justify-left flex-wrap">
<Chaifen char='主' :parts='[1,4]' />
✅
<Chaifen char='主' :parts='[2,3]' />
❌
</div>

2. `䒑`作頭時的`丷一`是`艹`的草化，無論書體，一概視為「連」。
<div class="flex justify-left flex-wrap">
<Chaifen char='兰' :parts='[3,2]' />
✅
<Chaifen char='兰' :parts='[2,3]' />
❌
</div>

3. `龷`在字中時的`艹一`，無論書體，一概視為「連」。
<div class="flex justify-left flex-wrap">
<Chaifen char='垂' :parts='[3,4,1]' />
✅
<Chaifen char='垂' :parts='[3,3,2]' />
❌
</div>
:::

## 字根的內在屬性

上面我們提到了宇浩輸入法拆字規則的優先級。其實，在「字根最少」之上，還有一個隱藏的原則，也就是：**字根的內在屬性**。

何為字根的內在屬性？其實就是指某一個字根區別於另一個字根的內在特點。

::: tip 例
`吉`拆成`士口`而不是`土口`，`周`拆成`⺆土口`而不是`⺆士口`，這是因為`土`的下面一筆更長，而`士`的下面一筆更短。這是區別兩個字根的本質原因和內在屬性。

<div class="flex justify-left flex-wrap">
<Chaifen char='吉' :parts='[3,3]' />
<Chaifen char='周' :parts='[2,3,3]' />
</div>
:::

「內在屬性」可以解釋為什麼有些字這樣拆而不是那樣拆，有些字為什麼看上去違反了「字根最少」的原則。

::: tip 例
`敝`拆為`丷巾八攵`而非`氺巾攵`，這看似違反了「字根最少」原則，但其實沒有。注意到，`敝`字左下的筆畫是撇不是提；在`氺`中，左下角的筆畫是提不是撇。故而，`敝`字裡並不存在`氺`字根。正因為如此，我們取四根`丷巾八攵`而非三根`氺巾攵`。
<div class="flex justify-left flex-wrap">
<Chaifen char='敝' :parts='[2,3,2,4]' />
✅
<Chaifen char='敝' :parts='[2,2,3,4]' :colors='[1,2,1,3]' />
❌
</div>
:::

在這個章節，我們就詳細討論字根的內在屬性，討論某些字根在宇浩拆分中被分離或者被合併的原因，從而讓某些字的拆分原因更加明確。

### 日曰之辨

不少輸入法對與`日` `曰`兩字的區分，比較複雜。大概有兩種情況：

- 有些是基於形狀的，凡是長大於高的都為`曰`，凡是長短於高的都為`日`。但這個方法會跟隨著字體的不同而不同，有時候不合字源，也不統一。例如：`書`字源於`聿者`，`曹`古字為`东东口`。
- 另外一種區分方法是基於字源。也就是說：凡是在古文中作`口`形，之後隸變為`曰`形或`甘`形的字，都作`曰`。但這個方法對方一般的使用者難度太大，且分析字源會有疏漏之處，不應用於輸入法。

我們必須注意到，在漢字中，存在`日曰`對立的字形，只有三組，分別為：`日曰`、`汨汩`、`曶㫚`。在其他的情況下，不存在對立，也就不存在混淆問題。

因此，我基於**實用主義**原則，對這兩個字根不多加以區分，而採取更簡單的方法。即：除了上述三組對立情況外，全部取`日`根。換句話說，`曰`根只需要在對立情況下才會使用，即：`曰` `汩` `㫚`三個字。

這樣一來，可以顯著降低使用者的記憶和學習負擔。

### 勹之辨

`旬`的外框`勹`，同`敖`左下的`勹`都是撇加橫折鉤。宇浩輸入法不做區分。

### 點之辨

這裡對含點字根的識別和歸併作出解釋。

::: info 含點字根

- 單點`丶`和捺`乀`視為同一個字根。
- 相重疊的兩點，即`头` `冬`中的部分，和`二`同碼位。
- 左對點`冫`和右對點`飞右`，和`二`同碼位。
- 下對點`八`為一個字根。
- 上對點`丷` `䒑` `リ`同大碼。
- 左`⺦`為一個字根。
- 左三點`氵`都在一個大碼。
- 上三點`ッ𠁼`都在一個大碼。
- 所有四點`灬`都在一個大碼。
:::

`为` `卵`等字的兩點和`冬`下的兩點不同，相隔太遠，且被半包圍或全包圍分割，故而不認定為「兩點」。詳[「散件不分隔」禁手](#散件不分割)。
<div class="flex justify-left flex-wrap">
<Chaifen char='冬' :parts='[3,2]' :colors='[0,1]' />
✅
<Chaifen char='为' :parts='[1,2,1]' :colors='[1,0,1]' />
❌
<Chaifen char='卵' :parts='[2,1,1,2,1]' :colors='[0,1,0,0,1]' />
❌
</div>

### 人八入之辨

`人` `八` `入`三字易混，這裡做出區分。

::: info 左撇右捺

1. 凡左撇不低於右捺，視作`人`根。
<div class="flex justify-left flex-wrap">
<Chaifen char='令' :parts='[2,1,3]' :colors='[1,0,0]' />
<Chaifen char='内' :parts='[2,2]' :colors='[0,1]' />
<Chaifen char='两' :parts='[1,2,2,2]' :colors='[0,0,1,2]' />
</div>

2. 凡左撇低於右捺，視作`入`根。
<div class="flex justify-left flex-wrap">
<Chaifen char='籴' :parts='[2,6]' :colors='[1,0]' />
<Chaifen char='陝' :parts='[2,1,2,2,2]' :colors='[0,0,0,1,2]' />
<Chaifen char='兩' :parts='[1,3,2,2]' :colors='[0,0,1,2]' />
</div>

3. 凡左撇右捺分離，視作`八`根。
<div class="flex justify-left flex-wrap">
<Chaifen char='分' :parts='[2,2]' :colors='[1,0]' />
<Chaifen char='兴' :parts='[4,2]' :colors='[0,1]' />
<Chaifen char='典' :parts='[6,2]' :colors='[0,1]' />
</div>

4. 凡左撇右捺的中間被其他筆畫隔開，視作`<丿乀>`根。宇碼中，它和`八`同大小碼。
<div class="flex justify-left flex-wrap">
<Chaifen char='办' :parts='[2,2]' :colors='[0,1]' />
<Chaifen char='朱' :parts='[4,2]' :colors='[0,1]' />
<Chaifen char='兼' :parts='[8,2]' :colors='[0,1]' />
</div>

:::

### 口中無整畫

口（音`kǒu`），囗（音`wéi`）。這兩個根如何區分？

答案是，如果方框裡有**完整**的筆畫，用`囗` `wéi`。否則一律用`口` `kǒu`。

::: tip 例
`国`字中，有完整的筆畫，故而必須用`囗` `wéi`。
`中`字中，雖然`⼁`穿`口`而過，但並未被完全包含在`口`中。由於`口`中沒有完整的筆畫，故而用`口` `kǒu`。
:::

此規定也適用於另外幾個包含`口`的字根。

::: tip 例

- `古`下的`口`中如果包含完整的筆畫，應該拆如`十囗`。例如：`鄙`左下方的`口`中有`口`，故而應該拆成`口十囗口阝`。
<div class="flex justify-left flex-wrap">
<Chaifen char='鄙' :parts='[3,2,2,3,1,2]' :colors='[1,2,3,4,3,5]' />
✅
<Chaifen char='鄙' :parts='[3,4,3,1,2]' :colors='[1,2,3,2,4]' />
❌
</div>
- `合`下的`口`中如果包含完整的筆畫，應該拆如`人一囗`。例如：`會`中間的`口`中有`小`，故而應該拆成`人一𫩏丷日`。
<div class="flex justify-left flex-wrap">
<Chaifen char='會' :parts='[2,1,3,2,1,4]' :colors='[1,2,3,4,3,5]' />
✅
<Chaifen char='會' :parts='[5,3,1,4]' :colors='[1,2,1,3]' />
❌
</div>
:::

## 漢字的拆分禁手

拆分之「禁手」，指的是無論任何時候都不應當出現一些拆分情形。它高於一切拆分規則。一旦某一個拆分候選中出現了「禁手」，則直接淘汰。禁手包括：散件不分割、豎向不包夾、橫間不穿心。

### 散件不分割

有一部分字根，本身存在離散的部件，比如`戈`字右上的點、`犬`字的右上的點、`三`字的三個橫等等。為了保證拆字的直觀，保證檢字（尤其是大字集下）的便捷性，我們需要對字根的連續性做出要求，並將它認定為字根的內在屬性。

字根的連續性定義如下：

一個字根的離散部件，不可被全包圍結構或半包圍結構分割。被分割的兩個部件不得視為一個字根。

::: tip 例

`为`字的兩點不可以被視為字根`两点`，因為它們被半包圍結構分割。  
<div class="flex justify-left flex-wrap">
<Chaifen char='为' :parts='[1,2,1]' />
✅
<Chaifen char='为' :parts='[1,2,1]' :colors='[1,2,1]' />
❌
</div>

`卵`字不拆`卯⺀`而拆成`卯丶丶`，因為`卯`字的點被全包圍結構分割。
<div class="flex justify-left flex-wrap">
<Chaifen char='卵' :parts='[2,1,1,2,1]' :colors='[1,2,1,1,3]' />
✅
<Chaifen char='卵' :parts='[2,1,1,2,1]' :colors='[1,2,1,1,2]' />
❌
</div>
:::

### 豎向不包夾

不少字根中存在若干分散的部件。

::: tip 例

`二`和`三`中的橫畫是分離的。

`合`分為了`一` `一` `口`三個部分。

`儿`分為了`丿` `乚`兩個部分。
:::

這給了它們包夾其他字根的可能。如`亘`可看成`二`包夾`日`。

為了防止拆分不直觀，我們做出規定，一個字根**可以橫向包夾，但不能縱向包夾**。

::: tip 例

`卿` = `卯彐厶`
<div class="flex justify-left flex-wrap">
<Chaifen char='卿' :parts='[3,3,2,2]' :colors='[1,0,0,1]' />
✅
<Chaifen char='卿' :parts='[3,3,2,2]' :colors='[1,0,0,4]' />
❌
</div>

`胤` = `儿幺月`
<div class="flex justify-left flex-wrap">
<Chaifen char='胤' :parts='[1,3,4,1]' :colors='[1,0,0,1]' />
✅
<Chaifen char='胤' :parts='[1,3,4,1]' :colors='[1,0,0,4]' />
❌
</div>

`亘` = `一日一`
<div class="flex justify-left flex-wrap">
<Chaifen char='亘' :parts='[1,4,1]' :colors='[1,0,3]' />
✅
<Chaifen char='亘' :parts='[1,4,1]' :colors='[1,0,1]' />
❌
</div>

`僵` = `亻一田一田一`

<div class="flex justify-left flex-wrap">
<Chaifen char='僵' :parts='[2,1,5,1,5,1]' :colors='[0,2,0,4,0,6]' />
✅
<Chaifen char='僵' :parts='[2,1,5,1,5,1]' :colors='[0,2,0,2,0,2]' />
❌
</div>
:::

這是因為，漢字的左右對稱多於上下對稱。左右包夾是可預測的，但上下包夾往往不可預測，必須要觀察到最下方。

::: tip 如果設置了衣字根

某些輸入法設置了`衣下`字根，但`亠`和`𧘇`的出現並不總是成對的，必須看到最下方才能正確判斷。

<div class="flex justify-left flex-wrap">
<Chaifen char='襄' :parts='[2,11,4]' :colors='[1,0,1]' />
<Chaifen char='衮' :parts='[2,4,4]' :colors='[1,0,1]' />
<Chaifen char='兖' :parts='[2,4,2]' :colors='[1,0,2]' />
</div>

:::

### 橫間不穿心

為了使拆分更加直觀，符合筆順，防止字根交叉粘連，我們規定：

`工土士干千禾キ王壬龶丰末未生古矢缶早羊虫`等字根不允許在`一一`間穿插其他字根。

這個規定在常用字中比較少用。

::: tip 例

`再`不拆`王冂`，而拆`一冂土`
<div class="flex justify-left flex-wrap">
<Chaifen char='再' :parts='[1,2,3]' />
✅
<Chaifen char='再' :parts='[1,2,3]' :colors='[1,0,1]' />
❌
</div>

`垂`不拆`壬龷`，而拆`千龷一`
<div class="flex justify-left flex-wrap">
<Chaifen char='垂' :parts='[3,4,1]' :colors='[1,2,3]' />
✅
<Chaifen char='垂' :parts='[3,4,1]' :colors='[1,0,1]' />
❌
</div>

`禹`不拆`丿虫冂`，而拆`丿口冂<丄丶>`
<div class="flex justify-left flex-wrap">
<Chaifen char='禹' :parts='[1,3,2,3]' :colors='[1,2,3,4]' />
✅
<Chaifen char='禹' :parts='[1,3,2,3]' :colors='[1,2,0,2]' />
❌
</div>

`妻`不拆 `キコ女`或`龶乛女`，而拆`十彐女`。
<div class="flex justify-left flex-wrap">
<Chaifen char='妻' :parts='[1,3,1,3]' :colors='[1,2,1,3]' />
✅
<Chaifen char='妻' :parts='[1,1,1,1,1,3]' :colors='[1,0,1,0,1,3]' />
❌
<Chaifen char='妻' :parts='[1,1,3,3]' :colors='[1,0,1,3]' />
❌
</div>

:::
