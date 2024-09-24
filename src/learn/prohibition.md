
<script setup>
import Chaifen from '@/chaifen/Chaifen.vue'
import MultiChaifen from '@/chaifen/MultiChaifen.vue'
</script>

# 宇浩拆分禁手

拆分之「禁手」，指的是无论任何时候都不应当出现一些拆分情形。它高于一切拆分规则。一旦某一个拆分候选中出现了「禁手」，则直接淘汰。禁手包括：散件不分割、竖向不包夹、横间不穿心。

## 散件不分割

有一部分字根，本身存在离散的部件，比如`戈`字右上的点、`犬`字的右上的点、`三`字的三个横等等。为了保证拆字的直观，保证检字（尤其是大字集下）的便捷性，我们需要对字根的连续性做出要求，并将它认定为字根的内在属性。

字根的连续性定义如下：

非连续写成、且被全包围结构或半包围结构分割的部件，不视为一个字根。

::: tip 例

`为`字的两点不可以被视为字根`两点`，因为它们非连续写成、且被半包围结构分割。  
<div class="flex justify-left flex-wrap">
<Chaifen char='为' :parts='[1,2,1]' />
✅
<Chaifen char='为' :parts='[1,2,1]' :colors='[1,2,1]' />
❌
</div>

`卵`字不拆`卯⺀`而拆成`卯丶丶`，因为`卯`字的两点非连续写成、且被半包围结构分割。
<div class="flex justify-left flex-wrap">
<Chaifen char='卵' :parts='[2,1,1,2,1]' :colors='[1,2,1,1,3]' />
✅
<Chaifen char='卵' :parts='[2,1,1,2,1]' :colors='[1,2,1,1,2]' />
❌
</div>
:::

## 竖向不包夹

不少字根中存在若干分散的部件。

::: tip 例

`二`和`三`中的横画是分离的。

`合`分为了`人` `一` `口`三个部分。

`儿`分为了`丿` `乚`两个部分。
:::

这给了它们包夹其他字根的可能。如`亘`可看成`二`包夹`日`。

为了防止拆分不直观，我们做出规定，一个字根**可以横向包夹，但不能纵向包夹**。

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

这是因为，汉字的左右对称多于上下对称。左右包夹是可预测的，但上下包夹往往不可预测，必须要观察到最下方。

::: tip 如果设置了衣字根

某些输入法设置了`衣下`字根，但`亠`和`𧘇`的出现并不总是成对的，必须看到最下方才能正确判断。

<div class="flex justify-left flex-wrap">
<Chaifen char='襄' :parts='[2,11,4]' :colors='[1,0,1]' />
<Chaifen char='衮' :parts='[2,4,4]' :colors='[1,0,1]' />
<Chaifen char='兖' :parts='[2,4,2]' :colors='[1,0,2]' />
</div>

:::

## 横间不穿心

为了使拆分更加直观，符合笔顺，防止字根交叉粘连，我们规定：

`工土士干千禾キ王壬龶丰末未生古矢缶早羊虫`等字根不允许在`一一`间穿插其他字根。

这个规定在常用字中比较少用。

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
<Chaifen char='禹' :parts='[1,3,2,3]' :colors='[0,1,0,1]' />
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
