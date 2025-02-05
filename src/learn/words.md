<script setup>
import Chaifen from '@/chaifen/Chaifen.vue'
</script>

# 词语编码

除了设置简码，宇码还将常用的词语，也编成 4 个字母的编码。这样可以降低每一个字的平均码长，提高打字速度。

「宇浩」的词语编码规则，分为三种情况。

## 两字词

两字词，取每个字**全码**的前两码即可：

::: tip 例

`人生`：`人`的编码为 `Ree`，`生`的编码为 `Pss`。因此，`人生`的编码为 `RePs`。  

`事情`：`事`的编码为 `KLBj`，`情`的编码为 `RHWy`。因此，「事情」的编码为 `KLWy`。
<div class="flex justify-left flex-wrap">
<Chaifen char='事' :parts='[1,3,3,1]' :colors='[1,2,0,1]' />
<Chaifen char='情' :parts='[3,4,4]' :colors='[3,4,0]' />
</div>
:::

## 三字词

三字词，取前两字的第一码，和第三个字的前两码即可：

::: tip 例
`泡泡糖`：`泡`的编码为`〔氵月巳・ NWOs〕`，`糖`的编码为`〔米广又古・ QMBL〕`。因此，`泡泡糖`的编码为`〔氵氵米广・ NNQM〕`。
<div class="flex justify-left flex-wrap">
<Chaifen char='泡' :parts='[3,2,3]' :colors='[1,0,0,0]' />
<Chaifen char='泡' :parts='[3,2,3]' :colors='[1,0,0,0]' />
<Chaifen char='糖' :parts='[6,3,4,3]' :colors='[3,4,0,0]' />  
</div>

`星期三`：`星`的编码为`〔日生・ JPsr〕`，`期`的编码为`〔其月・ UWyq〕`，`三`的编码为`〔三・ Laa〕`。因此，`星期三`的编码为`〔日其三・ JULa〕`。
<div class="flex justify-left flex-wrap">
<Chaifen char='星' :parts='[4,5]' :colors='[1,0,0,0]' />
<Chaifen char='期' :parts='[8,4]' :colors='[2,0,0,0]' />
<Chaifen char='三' :parts='[3]' :colors='[3,0,0,0]' />
</div>
:::

## 四字词及以上

四字词及以上，取前三字的第一码，和最后一个字的第一码即可：

::: tip 例
`狐假虎威`：`狐`的编码为`〔犭瓜・ HUgq〕`，「假」的编码为`〔亻尸二又・ EBIB〕`，「虎」的编码为`〔虎・ Uhh〕`，「威」的编码为`〔戊一女・ KFCn〕`。因此，「狐假虎威」的编码为`〔犭亻虎戊・ HEUK〕`。  
<div class="flex justify-left flex-wrap">
<Chaifen char='狐' :parts='[3,5]' :colors='[1,0]' />
<Chaifen char='假' :parts='[2,3,2,2,2]' :colors='[2,0,0,0,0]' />
<Chaifen char='虎' :parts='[8]' :colors='[3]' />
<Chaifen char='威' :parts='[2,1,3,3]' :colors='[4,0,0,4]' />
</div>

`中华人民共和国`：这是一个七字词，所以我们只看前三字和最后一字`中`、`华`、`人`、`国`。`中`的编码为`〔口丨・ LUsv〕`，`华`的编码为`〔亻匕十・ ENGi〕`，`人`的编码为`〔人・ Ree〕`，`国`的编码为`〔囗王丶・ WJKd〕`。因此，`中华人民共和国`的编码为`〔口亻禾囗・ LERW〕`。
<div class="flex justify-left flex-wrap">
<Chaifen char='中' :parts='[3,1]' :colors='[1,0]' :size=50 />
<Chaifen char='华' :parts='[2,2,2]' :colors='[1,0,0]' :size=50 />
<Chaifen char='人' :parts='[2]' :colors='[1]' :size=50 />
<Chaifen char='民' :parts='[3,2]' :colors='[0,0]' :size=50 />
<Chaifen char='共' :parts='[4,2]' :colors='[0,0]' :size=50 />
<Chaifen char='和' :parts='[5,3]' :colors='[0,0]' :size=50 />
<Chaifen char='国' :parts='[2,4,1,1]' :colors='[1,0,0,1]' :size=50 />
</div>
:::

## 词语输入的优缺点

用词语的方式进行输入，优点在于降低了每个字的平均码长。

::: tip

试想`我们今天一起吃饭`这个句子。

<div class="flex justify-left flex-wrap">
<Chaifen char='今' :parts='[2,1,2]' :size=50 />
<Chaifen char='天' :parts='[1,3]' :size=50 />
<Chaifen char='我' :parts='[1,1,2,3]' :colors='[1,0,2,3,5,1]' :size=50 />
<Chaifen char='们' :parts='[2,3]' :size=50 />
<Chaifen char='一' :parts='[1]' :size=50 />
<Chaifen char='起' :parts='[7,3]' :size=50 />
<Chaifen char='吃' :parts='[3,2,1]' :size=50 />
<Chaifen char='饭' :parts='[3,2,2]' :size=50 />
</div>

- 如果打单字全码的话，需要按`GFKgETmrRKYiFOdiFii_HOjzLGYiXDBo`。
- 如果打单字简码的话，需要按`G_ET_RK_FOd_F_HO_LG_XD`。
- 如果打词语全码的话，需要按`GFETRKFOFIHOLGXD`。

可以看到，词语全码有效降低了按键的次数。
:::
但是，词语输入也有其缺点，最主要的缺点包括：

- 如果词库太小，不是每个词语都在词库中。很多时候还是需要打单字。
- 如果词库太大，则会出现大量的重码，需要进行选择，破坏了形码输入的流畅性。
- 你输入一个词语，却发现它并不在词库中，就需要删除后重新输入单字。让人感觉不悦。
- 人工分词需要消耗额外的注意力。

**因此，精简词库，熟悉词库，打单字和打词语相结合，是形码高手们的修炼之路。**
