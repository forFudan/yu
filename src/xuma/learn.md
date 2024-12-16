# 徐码简明教程

朱宇浩　2022年5月31日初稿

::: tip 说明

本文字形依据中华人民共和国《古籍印刷通用字规范字形表》《通用规范汉字表》中制定的繁体字标准。

:::

## 初识徐码

### 汉字输入法

输入法，顾名思义，就是汉字（或其他字符）录入进电脑中的方法。大多数时候，输入的过程，有两个阶段：

1. 用户将汉字，用一定规则，编成一串字母、数字、符号的组合，输入电脑中。
2. 输入法会串字符，根据一定的规则，转化为对应的汉字，显示到屏幕上。

当我们用「输入法」指代第二个阶段时，一般我们指的是软件。徐码可依托 Rime（小狼毫、鼠须管等）、小小输入法、大大输入法等平台实现输入。

本教程中的「输入法」，特别指代上文中提到的第一阶段，亦即：用户将汉字，用一定规则，编成一串字母、数字、符号的组合，输入电脑中。

### 输入法种类

输入法，根据其特点，一般分为三类

- 音码
- 形码
- 音形（形音）混合码。

**音码输入法**，最常见的例子就是拼音了。我们将汉字对应的拼音，直接输入到软件中，软件会显示对应的汉字供你选择。

**形码输入法**，最常见的例子是五笔字型。我们将汉字拆成若干部件，输入每一个部件对应的代码，软件会显示出汉字。常见的形码，还包括五笔字型，郑码，仓颉等等。

徐国银先生发明的徐码繁简通打输入法（尔雅输入法），便是一种形码输入法。

### 形码和音码的对比

形码输入法和拼音最大的区别，在于拼音输入法，知道读音，便能输入汉字。而形码输入法，知道写法，便能输入汉字。

音码的优点，不言而喻，只要知道标准的发音，便可以打出字来。同时，汉语拼音也是当代人的必修课，不需要特别地学习，因此，它的学习成本近乎为零。

音码缺点，那便是同音字很多，经常需要选字。虽然当代的不少输入软片在「智能化」上下足了工夫，但在输入一些书面语、古文、或者生僻字词时，还是需要选字。大量翻页会打输入的节奏。

形码的优点，便是像写字一样去打字。你不需要知道每个字的具体读音。同时，因为编码比较离散，你甚至不怎么需要去选字。这在写作时，保证你的思路不被打断。在看打、或者打古文的时候，形码的速度很快。

音码缺点是，如果你一下字忘了这个字的写法，那就会卡住，必须临时改用拼音输入法（反查）。

至于音码和形码哪个更好？这就是仁者见仁、智者见智的问题了。当然，也依赖于你的需求和使用场合。笔者在日常对话时使用拼音，在写作时使用徐码，做到扬长避短。

### 徐码的特点

徐码作为一种**形码输入法**，除了继承了刚刚所说的形码的全部重点外，还有一些自身的特点，让它在众多输入法中脱颖而出。这里仅举例一二：

- 大字集。也就是说，用徐码可以打出几乎所有的 CJK 的汉字（官方码表更新至扩G区，我拆到了扩H区），单字拆分提示我已经完成了93000个汉字，并且一一直保持保持更新维护。
- 繁简通。也就是说，你可以直接打出传统汉字和简化汉字，且大多数情况下，繁简字根不占用同一个码位，因此繁简混输的时候也很少选字。
- 低重码。也就是说，每个编码一般只对应唯一的候选项，你不需要进行选字，可以不用打断思路地进行输入。

这个对比一下五笔、郑码、徐码、仓颉在不同汉字字符集下的单字全码的重码数量。[更多比较见此页面](../docs/statistics.md)。

其中：

- 「通规」是指大陆《通用规范汉字表》中的 8105 个简化汉字。测试输入法**简化字确定性**。
- 「国字」是指台湾《常用国字标准字体表》中的 4808 个繁体汉字。测试输入法**繁体字确定性**。
- 「常用繁简」是指大陆《通用规范汉字表》和台湾《常用国字标准字体表》中的 9853 个繁简汉字。测试输入法**繁简混输确定性**。
- GB2312 是大陆的简化字集，共有简化汉字 6764 个。
- BIG5 是台湾的繁体字集，共有繁体汉字 13069 个。
- GBK 是大陆的繁简字集，共有繁简汉字 21003 个。
- **动态重码率**指的是用字频对重码字进行加权，只使用大陆《通用规范汉字表》中的**简化汉字**。
- **动态选重率**指的是用字频对重码字中除却煅选的汉字进行加权，只使用大陆《通用规范汉字表》中的**简化汉字**。这里的假设明文打开记住首选字，并默认将之上屏。因此只有在二选或三选时才需要选重。更能反映实际**简化汉字**输入体验。

| 形码方案      | 通规 | 国字 | 常用繁简 | GB2312 | BIG5 | GBK  | 动态重码率 | 动态选重率 | 长度 |
| ------------- | ---- | ---- | -------- | ------ | ---- | ---- | ---------- | ---------- | ---- |
| 五笔86        | 787  | 357  | 1938     | 537    | 2236 | 6582 | 7.77%      | 0.34%      | 四码 |
| 五笔98        | 763  | 329  | 1867     | 515    | 2150 | 6368 | 8.56%      | 0.37%      | 四码 |
| 五笔06·新世纪 | 831  | 387  | 1970     | 532    | 2373 | 6610 | 7.90%      | 0.31%      | 四码 |
| 郑码          | 843  | 311  | 2063     | 563    | 2206 | 6590 | 7.50%      | 0.59%      | 四码 |
| 徐码22        | 495  | 131  | 678      | 320    | 1104 | 2899 | 3.49%      | 0.10%      | 四码 |
| 仓颉五代      | 498  | 164  | 714      | 422    | 978  | 2893 | 12.07%     | 0.89%      | 五码 |

可见，徐码在任何字集下都有着优异的表现。尤其在「繁简通打」模式下，它是绝对的王者。

### 徐码的资源

徐码（2022版「新徐码」）的 QQ 群是: 761401688。

你可以在群里和大家讨论，同时获取学习资料、字根图、最新码表。

### 学习步骤

学习徐码，一般从了解拆字和熟悉字根开始。

拆字，就是把汉字按照一定的规则，拆成唯一的部件组合。拆分出来的部件，便叫做「字根」。

这里所谓的「部件」，不仅包括你我熟知的「偏旁部首」，也包括了一些基本笔划，甚至是一些汉字。因此，笔画输入法（横竖撇捺折），也是一种特殊的形码。那么我们为什么要创造别的形码呢？因为一个字若用十几个、甚至几十个字母代替，太没有效率。故而，我们会截取一些比较大的部件作为字根。

对于汉语使用者，拆字并不是一件陌生的事情。我们自小就学会将一个字拆成分离的部首，进行检索。大多数时候，这是非常直观的。比如

- `部`字，大家会自然地将他拆分为`立口阝`三个部分。
- `程`字，大家会自然地将他拆分为`禾口王`三个部分。

对于徐码而言，大多数的字，也是这么拆分的。并且大多数的偏旁部首，也都是「字根」。

所以恭喜你，对于大多数的汉字，你已经可以凭借直觉进行拆分了。

本教程推荐的学习步骤如下。

1. 看字根图，**大致**了解徐码的字根有哪些，以及它们对应的编码。
2. 了解徐码拆字的规则，学会如何得到唯一的拆分方法。
3. 学习编码规则，学会如何将拆好的字根转化成最终的徐码。
4. 记诵最常用的50个字根的编码。
5. 直接在输入软件中练习前500常用字，边练习边记忆字根。
6. 阅读进阶教程，更加深入地了解一些徐码的特点。

以上内容不论顺序，可以交叉或同步进行。

## 字根编码

### 大码和小码

在徐码中，每一个字根，都对应了两个字母。换句话说，徐码使用的是**双编码字根**。这一点和郑码相同，和五笔不同。特别的：

- 第一个字母叫做**大码**，也就是「户口」，大多数时候，我们只需要用到大码，所以应该重点记忆。
- 第二个字母叫做**小码**，也就是「姓名」，或者说是「识别码」。只有在部份情况下，需要用到，记忆起来也比较简单。

字根的大码和小码的分布，并不是随机的，而是有一定的规律。在接下来的教程中会进行介绍。

### 字根图

我们将字根的分布画出来，这便是字根图。如下。

图中，每一个方框右上角的大写字母，就是大码，也就是一群字根的「户口」。而字根右下角的小写字母，则是小码，也就是单个字根的「姓名」。

将大码和小码组合起来，就是一个字根的编码了。比如：

- 「言」这个字根，在字母`Y`的方框里，同时，右下角的字母是`v`，因此，它的编码就是`Yv`。
- 「其」这个字根，在字母`H`的方框里，同时，右下角的字母是`q`，因此，它的编码就是`Hq`。

字根图是查询字根的重要工具，初学者应当时常将它放在手边，以利用查询。

<!-- [![徐碼字根圖](/resources/徐碼全字根圖.png)](/resources/徐碼全字根圖.png) -->

### 字根大码的规律

字根大码，是按照字根第一笔的笔画来制定的。

- A-D 包含了首笔为「折」的字根，例如：`A水` `B月`等。
- E-J 包含了首笔为「横」的字根，例如：`E王` `F大`等。
- K-O 包含了首笔为「竖」的字根，例如：`K日` `L上`等。
- P-V 包含了首笔为「撇」的字根，例如：`P牛` `V入`等。
- W-Z 包含了首笔为「捺」和「点」的字根，例如：`W穴` `Y言`等。

一般地，各字母上的字根呈现以下的规律：

- B 上的字根大多呈现`乛`的特点。比如：阝、了、予、矛、乙、也、飞、艮、子。
- D 上的字根大多呈现`コ`的特点。比如：尸、弓、己、已、巳、巴、韦。
- E 上的字根大多呈现`二`的特点。比如：二、干、镸、长、髟、马、甫。
- F 吸收了首笔为横，且不在 E G H I J 上的其他字根。
- G 上的字根**几乎全部**呈现`丆`的特点。比如：石、辰、不、兀、歹、豕、页、而、面、厂。
- H 上的字根**几乎全部**呈现`丌`（一横两竖）的特点。比如：卄、革、其、世、瓦、耳、丌。
- I 上的字根大多呈现`木`和`三`的特点。比如：木、未、末、来、三、丰。
- J 上的字根大多呈现`土`的特点。比如：土、士、车、雨、尔、古、走。
- K 上的字根**全部**呈现`日`的特点。比如：日、曰、田、申、由、电、甲、禺、早。
- L 上的字根**全部**呈现`卜`（竖横）或两竖的特点。比如：虫、龰、卜、虍、上、非、卤、齿、止、刂。
- M 上的字根**几乎全部**呈现`⼌`（不封口三面框）和`罒`（横框）的特点。比如：山、⼌、册、巾、贝、黑、皿。
- N 上的字根**几乎全部**呈现`囗`（封口四面框）和`門`（对称）的特点。比如：目、贝、见、骨、囗、门、斗、且。
- O 上的字根**几乎全部**呈现`口`（小口）的特点。比如：口、㗊、黾、𧾷、〇。
- P 上的字根**几乎全部**呈现`𠂉`（撇横）的特点。比如：𥫗、钅、牛、缶、气、生、矢、长。
- Q 上的字根**全部**呈现`𠂊`（撇折）的特点。比如：鱼、鱼、饣、欠、风、殳、几、凡、夕。
- R 上的字根**几乎全部**呈现撇横和撇撇的特点。比如：禾、千、夭、壬、手、毛、九、瓜、舟、爪。
- S 上的字根**几乎全部**呈现`勹`（撇折钩）和两撇的特点。比如：月、用、乌、鸟、彡、彳、行。
- T 上的字根大多呈现`亻`（撇竖）的特点。比如：身、鼻、隹、川、自。
- U 上的字根**全部**呈现`白`和`人`的特点。比如：人、佥、白、臼、𠂤、鸟、乌、鼠、鬼。
- V 上的字根大多呈现`人`（对称）的特点。比如：金、入、食、儿
- W 上的字根**全部**呈现`广`（点横撇）的特点。比如：宀、广、疒、麻、鹿、穴、衤、礻、衣。
- X 上的字根**全部**呈现`丷`（相对两点）的特点。比如：冫、米、羊、为。
- Y 上的字根**全部**呈现`亠`（点横）的特点。比如：言、方、亦、亥、音、立、文、辛。
- Z 上的字根**全部**呈现`讠`（点折）的特点。比如：讠、之、户、门、辶。

其中，只有 A 和 C 键上的字根需要特别记忆。

### 字根小码的规律

#### 主根

每个大码下，都有若干字根比较重要，使用频率高，叫做「主根」。

第一主根的小码是`v`，第二主根是`u`。例如：

- `女`，第一笔为「折」，故而它的大码在折区的`C`。根据字根图，「女」是第一主根，所以小码是v。因此，「女」这个字根的编码就是`Cv`。当你输入`Cv`并按下空格时，就可以打出「女」字了。
- `士`，第一笔为「横」，故而它的大码在横区的`J`。根据字根图，「士」是第二主根，所以小码是u。因此，「士」这个字根的编码就是`Ju`。当你输入`Ju`并按下空格时，就可以打出「士」字了。

注意：我在这里使用大写和小写的拉丁字母，是为了区分大码和小码的概念。在实际打字的过程中，不需要区分大小写。

#### 副根

另一部份字根，我们叫它「副根」。

副根的小码是除了`u`和`v`的其他的字母。

一般情况下，副根的小码是它的汉语拼音的第一个字母（请注意，这只是一种记忆方式，并不是说明徐码是一种音形码）。例如：

- `米`，第一笔为「点」，故而它的大码在点区的`X`。根据字根图，它是副根，小码是m，正好是米字的声母。因此，「米」这个字根的编码就是Xm。当你输入`Xm`并按下空格时，就可以打出「米」字了。

<!-- omit in toc -->
#### 字根练习

必练：以下字根是最常见的50个字根，首先学习它们，对于打字的进步提升最大。

`口氵艹扌木亻日一人丷亠土冖宀月女丿忄十讠王⼫纟大禾火又⼂厶勹𠂉阝冂山⺕八广钅虫𥫗⺌目𠃌米⻊白夊𠂆立`

请通过查询字根图，写出以下字根的编码，分辨它是主根还是副根，并用输入法软件打出这个字根。

选练：以下字根是最常见的第51到第100字根，继续学习它们，对于打字的进步提升较大。

`贝𠂇石田二穴犭爫龷疒匚七厂车刀工乂冫隹龶几雨力弓士小马囗门文止耳户耂方⺊戈夕罒乚西心丨干衤夫丁巾彳`

选练：阅读字根图上的全部字根，将它们逐一输入到电脑中，从而对字根编码以及它的性质有一个初步的印象。

## 拆字规则

先前说过，拆字，就是把汉字按照一定的规则，拆成唯一的字根组合。

我刚刚用的「部」字为例，说明了拆字的一般形式。这种将字拆成直观的、分离的部件的方法，足以应付大部分汉字的拆分了。但在实际使用中，遇到这个问题：一个独体字，本身不是字根，怎么办？这时候，我们要把它继续拆成更小的字根甚至笔划。比如：

- 「戋」这个字，我们可以继续将它拆成「一」和「戈」。查字根图可知，「一」和「戈」正好是两个字根，拆字成功。
- 「丸」这个字，我们可以继续将它拆成「九」和「丶」。查字根图可知，「九」和「丶」正好是两个字根，拆字成功。
- 「朱」这个字，我们可以继续将它拆成「丿」和「未」。查字根图可知，「丿」和「未」正好是两个字根，拆字成功。

有时候，独体字的拆分不是很直观。比如「再」拆成「王冂」两个字根。遇到此类字时的拆分，往往需要一些经验和练习。所以当你遇到不会拆的字时，应该主动查询它的编码，及时学习。

更麻烦的情况是，**一个字好像有几种拆分方法**，比如：

- 「章」，可以拆「立早」，也可以拆「音十」。
- 「井」，可以拆「二{齐下}」，也可以拆「一廾」。

这种一字多拆的情况，任何形码中，都是积极避免的。因为一字多拆，会造成极大的不确定性，并造成编码的混乱。

徐码，通过一套严密的规则，使每一个汉字，都只有**唯一**的拆分方案，完全消除了不确定性。

徐码拆字规则的按优先级排序如下：

1. 字根最少
2. 符合笔顺
3. 原形字根
4. 字根离散
5. 字根相连
6. 字根相交
7. 笔划断开
8. 字根取大

可归纳为：**少>顺>原>散>连>交>断>大**。

取根时，按优先级从高到低依次，最终得到唯一的拆分方案。

注：「原形字根」是新版徐码引进的新规则，目的是为了让拆字更加直观。老版徐码的拆字规则为，少>散>连>交>断>顺>大

以下为规则详细介绍：

### 字根最少

字根最少，意思是拆分一个字时，应该使得字根的数量最少。比如：

- 「章」拆「立早」而不拆成「立日十」，因为前者只有两个字根，而后者为三个。

### 符合笔顺

符合笔顺，指的是字根的每一笔，完全符合原汉字的笔顺。比如：

- 「里」可拆成「甲二」，也可拆成「日土」。观察到「甲二」完全符合「里」字的笔顺，故而选择它。
- 「单」可拆成「丷日十」，也可拆成「丷甲二」。观察到「丷日十」完全符合「单」字的笔顺，故而选择它。

### 原形字根

在徐码的字根，分为两类，一部分称为**原形字根**。另有一部分字根，是根据原形字根变形而来的，在字根图中，这部分**变形字根**列在字根原型的右下方，以小字显示。比如：

- 「牛」字根的「丨」变成「丿」。
- 「尸」字根的「丿」变成「丨」。

注意，**原形字根和变形字根都一定存在于字根图中**。字根图没有的字根永远不能叫做变形字根。

在拆字时，不变形字根的优先级高于变形字根。比如：

- 「失」拆「丿夫」而不拆「牛丶」，因为「牛丶」使用了变形根。

### 字根离散

字根离散，指的是两个字根互相分离。比如：

- 「部」中的「立口阝」，便是三个分离的字根。

### 字根相连

字根相连，指的是两个字根互相连接。比如：

- 「章」拆「立早」而不拆成「音十」，因为「立」和「早」分开，但「日」和「十」相连。因为「字根离散」优先于「字根相连」，故而拆成「立早」。

### 字根相交

字根相交，指的是两个字根互相交叉。比如：

- 「唐」拆成「广コ古」三个字根，其中的「コ」和「古」两根便是交的。
- 「再」拆成「王冂」两个字根，便是相交的。

### 笔划断开

笔划断开，指的是将一个笔划断开。比如：

- 「我」拆成「丿扌戈」三个字根，其中的「扌」和「戈」两根的横本是一笔写成。但如果不断开这一横，就要拆成「丿扌乚丿丶」五个字根。为了让字根数量最少，我们将不得不将横断开。

### 字根取大

字根取大，指的是按照笔顺拆字时，让靠前的字根的笔划数尽量地多。比如：

- 「井」拆成「二{齐下}」，而不拆成「一廾」，因为「字根取大」原则。让靠前的字根的笔划数尽量地多，这里，「二」的笔划数大于「一」。

### 字根排序规则

将汉字拆分后，我们需要将它们进行排序。大多数时候，这是非常直观的。但有时并非如此，需要进行定义。

徐码字根排序规则，是**字根首笔符合笔顺**，意思是拆分一个汉字时，所有字根的**首个笔划**，符合这个汉字的笔顺。比如：

- 「安」拆「宀女」而不拆成「女宀」，因为按照汉字的笔顺，「宝盖头」第一的笔「点」，排在「女」字第一笔的「折」之前。故而应该按照「宀女」排序。
- 「丸」拆「九丶」而不拆成「丶九」，因为按照汉字的笔顺，「九」第一的笔「撇」，排在「捺点」之前。故而应该按照「九丶」排序。

请注意，徐码最终的字根排序，只要求字根的**首笔**符合笔顺，而不是要求字根每一笔都符合笔顺，比如：

- 「为」的笔顺是「点撇折点」。`{兩點}`字根的第一笔「点」为整个「为」字的第一笔，虽然``{兩點}`字根的最后一笔是「为」字的最后一笔，`{兩點}`字根依旧排在最前面。所以「为」拆「{两点}力」。
- 「国」拆「囗王丶」而不拆成「冂王丶一」，因为前者只有三个字根，而后者为四个。「字根最少」优先于「字根首笔符合笔顺」。同时，`囗`字根的第一笔「竖」为整个「国」字的第一笔，虽然`囗`字根的最后一笔是「国」字的最后一笔，但`囗`字根依旧排在最前面。

### 拆字举例

实际拆字时，如果你感觉拆分方法不唯一，那么可以用以下方法找到最优解：

- 列出所有可能的候选拆分方案。
- 依照「少>顺>原>散>连>交>断>大」的规则顺序，依次比较各个候选拆分。
- 如果所有的候选拆分都不满足本条规则，则进入下条规则。
- 如果部分的候选拆分满足本条规则，则该部分的候选拆分方案进入下条规则。
- 直到只有一个候选拆分方案胜出。

注：「取大原则」又称兜底原则，保证最终只有一个候选方案胜出。

以下通过部分例字来说明拆分规则：

#### 「重」字

「重」字，候选拆分「丿车一」和「千日二」。

依照「少>顺>原>散>连>交>断>大」的规则比较。

- 同时满足「字根最少」。
- 「丿车一」满足「符合笔顺」，「千日二」不满足。
- 「丿车一」胜。

#### 「朱」字

「朱」字，候选拆分「丿未」和「牛八」。

依照「少>顺>原>散>连>交>断>大」的规则比较。

- 同时满足「字根最少」。
- 同时满足「符合笔顺」。
- 「丿未」满足「原型字根」，「牛八」不满足，因为「牛」的竖变撇。
- 「丿未」胜。

## 单字编码规则

学习了徐码的拆字规则后，我们可以将任何一个汉字拆成唯一的字根组合。最后一步，便是把字根转为徐码编码。

单字的编码一般是由**4个字母**构成，部分情况下是2个或3个字母。

在徐码中，无论一个字能拆成几个字根，我们只关心其中的四个根，分别是：

- 第一根：首根
- 第二根：次根
- 倒数第二根：次末根
- 倒数第一根：最末根

在编码时，我们首先判断一个字的首根是**主根**还是**副根**。

### 首根为主根

首根为主根时，有两条规则：

1. 依次取首根、次根、次末根、最末根的**大码**。
2. 不足四码时，补上最末根的**小码**。

举例说明：

- 「嫩」字拆成`女Cv 木Iv 口Ov 攵pp`四根。分别对应了首根、次根、次末根、最末根。我们直接取四个字根的大码`CIOP`即可出字。
- 「整」字拆成`木口攵一止`五根。我们只取首根、次根、次末根、最末根，也就是`木Iv 口Ov 一Gu 止Lz`的大码，输入`IOGL`即可出字。
- 「算」字拆成`𥫗目廾`，只有三根，所以我们取全部根，也就是`𥫗Pv 目Nv 廾Hv`的大码，即`PNH`。此时，注意到不足四码，故而补上最末根的小码`v`。输入`PNGv`即可出字。
- 「好」字拆成`女子`，只有两根，所以我们取全部根，也就是`女Cv 子Bz`的大码，即`CB`。此时，注意到不足四码，故而补上最末根的小码`z`。输入`CBz`即可出字。

再次强调，**首根为主根时，需要取4个根**。

### 首根为副根

首根为副根时，有三条规则：

1. 依次取首根、次根、最末根的**大码**。
2. 不足三码时，补上最末根的**小码**。
3. 在末尾添加首根的**小码**作为识别。

举例说明：

- 「织」字拆成`纟Cj 口Ov 八Tu`三根。分别对应了首根、次根、最末根。我们取三个字根的大码`COT`，再添上首根的小码`j`作识别。输入`COTj`即可出字。
- 「微」字拆成`彳Sr 山Iv 一Gu 几Ov 攵Pp`五根。我们只取首根、次根、最末根，也就是`彳Sr 山Iv 攵Pp`的大码，再添上首根的小码`r`作识别。输入`SIPr`即可出字。
- 「认」字拆成`讠人`，只有两根，所以我们取全部根，也就是`讠Zy 人Uu`的大码，即`ZU`。此时，注意到不足三码，故而补上最末根的小码`u`，再添上首根的小码`y`作识别。输入`ZUuy`即可出字。

再次强调，**首根为副根时，只需要取3个根**。

末尾添加首根的小码，有时候新手会需要一段时间来适应。好在由于**简码**的存在，大多数的时候，我们都不需要输入最后的识别码就能出字。

### 字根字

字根字，依次取其大小码即可出字。比如：

- 「木」字是字根字（主根），输入大小码`Iv`即可出字。
- 「骨」字是字根字（副根），输入大小码`Ng`即可出字。

### 空格键的使用

在很多输入法软件中，空格键（以下用`_`表示）用来上屏首选字。

根据以上的学习内容，我们发现：徐码的编码最长不超过4个字母。由于这个特性，我们在输入完编码后，不一定需要按空格键将字打上屏幕。

空格键只在以下情况需要使用：

- 一个字的编码低于4位，需要按空格键上屏首选。比如「人」字，需要按`Uu_`上屏。
- 一个字的编码等于4位，后面没有其他的字需要输入，则需要按空格键上屏首选。

以下情况，不需要使用空格键：

- 一个字的编码等于4位，且有后续字符等待输入。我们不需要按空格键。只要直接输入下一个字的首码，这个字就会自动上屏。我们称之为「五码顶屏」。例如：我们打「霁雨」二字，「霁」字的编码是`JYTy`。输入`y`后，我们直接输入「雨」字的编码`Jy`，则「霁」字会自动上屏。

## 简码设置

学完了徐码的单字编码，我们发现，徐码的单字码长一般是2到4位之间。不少常用的字，码长是4位，比如字频第一的「的」字，编码为`USUb`。

一种科学的输入策略，应该使得常用字的码长更低，从而加快输入的速度。试想，如果输入「的」字，每次都要按`USUb`四下按键，真是太浪费时间了。

形码对此的优化方式，就是设置简码，也就是给部分汉字设置更短的编码：比如，我们在输入「的」时，只要按上一个字母和空格键，就能实现输入。

在徐码中，简码的设置十分科学，使得每一个字简码和全码的编码规则保持一致。以下进行介绍。

### 一级简码字

一级简码字，又称**一简字**，指的是用一个字母为编码实现输入的汉字。徐码中，有26个高频汉字设置为一简字，只要按下一个字母，加上空格，即可上屏。

一简字的编码，就是该字全码的第一个字母。比如：

- 「我」全码为`PFFg`，一级简码为`P`。输入`P_`即可实现上屏。
- 「的」全码为`USWb`，一级简码为`U`。输入`U_`即可实现上屏。

从A到Z排列，一级简码字分别是`以了发那要大一在事地是上同国中我多和得他的儿家道这为`。

在字根图中，一简字就是每个字母方框的左上角的汉字。

在我们的日常交流中，一简字大约占据了25%的使用频率。在徐码中，只需要按两个按键，这有效提升了输入的速度。

### 二级简码字

二级简码字，又称**二简字**，指的是用两个字母为编码实现输入的汉字。徐码中，有676个高频汉字设置为二简字，只要按下两个字母，加上空格，即可上屏。

一简字的编码，就是该字全码的前两个字母。比如：

- 「起」全码为`JDjz`，二级简码为`JD`。输入`JD_`即可实现上屏。
- 「可」全码为`EOvd`，二级简码为`EO`。输入`EO_`即可实现上屏。

### 三级简码字

三级简码字，又称**三简字**，指的是用三个字母为编码实现输入的汉字，只要按下三个字母，加上空格，即可上屏。

三简字的编码，就是该字全码的前三个字母。这里不再举例。

注意到，三简字需要按四个按键才能上屏，同输入单字全码按键数一样，因此，三简字的设置主要为了以下目的：

- 腾出四码码位，实现避重。
- 首根为副根的字，在末尾不用输入首根的小码。只有在部分时候需要输入识别码定字。这样可以减轻记忆负担，不需要返回去思考首根的小码是什么。
- 减少单手连续击键的可能性，减轻手指的负担。

三级简码字，可在打字时进行熟悉，不需要特别去记忆。

## 词语编码规则

除了设置简码，徐码还将常用的词语，也编成4个字母的编码。这样可以降低每一个字的平均码长，提高打字速度。

徐码的词语编码规则，分为三种情况。

### 两字词

两字词，取每个字**全码**的前两码即可。比如：

- 「人生」：「人」的编码为`Uu`，「生」的编码为`Ps`。因此，「人生」的编码为`UuPs`。
- 「事情」：「事」的编码为`IOBu`，「情」的编码为`UESv`。因此，「事情」的编码为`IOUE`。

### 三字词

三字词，取前两字的第一码，和第三个字的前两码即可。比如：

- 「泡泡糖」：「泡」的编码为`ZSDs`，「糖」的编码为`XWjm`。因此，「泡泡糖」的编码为`ZZXW`。
- 「星期三」：「星」的编码为`KPs`，「期」的编码为`HSvq`，「三」的编码为`Is`。因此，「星期三」的编码为`KHIs`。

### 四字词及以上

四字词及以上，取前三字的第一码，和最后一个字的第一码即可。比如：

- 「狐假虎威」：「狐」的编码为`VRgq`，「假」的编码为`TDDD`，「虎」的编码为`LQjh`，「威」的编码为`FGCw`。因此，「狐假虎威」的编码为`VTLF`。
- 「中华人民共和国」：这是一个七字词，所以我们只看前三字和最后一字「中」、「华」、「人」、「国」。「中」的编码为`OKu`，「华」的编码为`TVEu`，「人」的编码为`Uu`，「国」的编码为`NEWw`。因此，「中华人民共和国」的编码为`OTUN`。

### 词语输入的优缺点

用词语的方式进行输入，优点在于降低了每个字的平均码长。试想「我们今天一起吃饭」这个句子。

- 如果打单字全码的话，需要按`PFFgTZm_UW_Bu_GFd_Gu_JDjzOPBi_QRDi_`。
- 如果打单字简码的话，需要按`P_TZm_Uwb_GF_G_JD_Op_QRd_`。
- 如果打词语全码的话，需要按`PFTZUWGFGuJDOPQR_`。

可以看到，词语全码有效降低了按键的次数。

但是，词语输入也有其缺点，最主要的缺点包括：

- 如果词库太小，不是每个词语都在词库中。很多时候还是需要打单字。
- 如果词库太大，则会出现大量的重码，需要进行选择，破坏了形码输入的流畅性。
- 你输入一个词语，却发现它并不在词库中，就需要删除后重新输入单字。让人感觉不悦。
- 人工分词需要消耗额外的注意力。

因此，精简词库，熟悉词库，打单字和打词语相结合，是形码高手们的修炼之路。

## 进阶教程

### 口囗之辨

口（音`kǒu`），编码为`Ov`，是个主根。囗（音`wéi`），编码为`Nw`，是个副根。这两个根如何区分？

答案是，如果方框里有**完整**的笔画，用「囗」`Nw`。否则一律用「口」`Ov`。例如：

- 「国」字中，有完整的笔画，故而必须用「囗」`Nw`。
- 「中」字中，虽然「⼁」穿「口」而过，但并未被完全包含在「口」中。由于「口」中没有完整的字根，故而用「口」`Ov`。

这个规则不影响含「口」形的其他字根。比如「古」字中的「口」。例如：

- 「鄙」字左下方拆成「古口」，不拆成「十囗口」，尽管「古」中的方框包含了完整笔画。

### 「日」「曰」字根的选取原则

当前的徐码对方「日」「曰」的区分，是基于形状的。也就是说：凡是长大于高的都为「曰」，凡是长短于高的都为「日」。但这个方法会跟随着字体的不同而不同，有时候不合字源，也不统一。例如：

- 「书」字源于「聿者」。徐码中「书」下为「曰」，但「者」下为「日」，取码不统一。
- 「曹」古字为「东东口」。在徐码中，「曹」下为「日」，不符合字源。

另外一种区分方法是基于字源。也就是说：凡是在古文中作「口」形，之后隶变为「曰」形或「甘」形的字，在徐码中作「曰」。但这个方法对方一般的使用者难度太大，且分析字源会有疏漏之处，不应用于输入法。

第三种方法是不做区分。在汉字中，存在「日曰」对立的字形，只有三组，分别为：「日曰」、「汨汩」、「曶㫚」。在其他的情况下，不存在对立，也就不存在混淆问题。因此，取「日」还是取「曰」，可以采取更简单的方法。即：除了上述三组对立情况外，全部取「日」`Kv`根。换句话说，「曰」`Ku`根只需要在「曰」「汩」「㫚」三处使用即可。这样一来，可以显著降低使用者的记忆和学习负担。

然而，第三种方法还是会造成大量重码，比如「旭」和「旮」。因为，在徐码中，「日」「曰」的区分，取决于字根的长宽。字形则依据 GB18030 标准。

### 勹𠂊之辨

「旬」的外框「勹」`Su`，同「敖」左下的「𠂊」`Qu`都是撇加横折钩，但是一个在`S`上，一个在`Q`上。如何分辨呢？

答案是，如果它包围了一个**完整**的笔画，用「勹」`Su`。否则一律用「𠂊」`Qu`。例如：

- 「勺」字中，有完整的笔画，故而必须用「勹」`Su`。
- 「㡬」字中，没有完整的笔画，故而必须用「𠂊」`Qu`。

## 徐码存疑和商榷

以下是关于徐码中部分规则的存疑和商榷。

### 「妻」字

此字官方码表拆作「十彐女」。我提议拆作「キコ女」。

依照「少>顺>原>散>连>交>断>大」的规则比较。

- 同时满足「字根最少」。
- 同时不满足「符合笔顺」。
- 同时满足「原形字根」。
- 同时不满足「散连」。
- 同时满足「交」。
- 同时不满足「断」。
- 「キコ女」满足「字根取大」，「十彐女」不满足。
- 「キコ女」胜。