---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "宇浩輸入法"
  text: "情繫漢字 溝通古今"
  tagline: 全漢字字形輸入・繁簡通打・極低選重
  image:
    dark: /logo_purple.png
    light: /logo_blue.png
    alt: yuhao-logo
  actions:
    - theme: alt
      text: 介紹
      link: /zht/docs/
    - theme: brand
      text: 教程
      link: /zht/learn/division
    - theme: alt
      text: 練習
      link: /zht/practice/root
    - theme: alt
      text: 安裝
      link: /zht/install

---

<script setup>
import Search from '@/search/FetchSearch.vue'
import Chaifen from '@/chaifen/Chaifen.vue'
import MultiChaifen from '@/chaifen/MultiChaifen.vue'
import IME from '@/ime/FetchInput.vue'
</script>

<div class="zigen-font">
<Search chaifenUrl="/chaifen.csv" zigenUrl="/zigen-star.csv" supplement />
</div>

---

<!-- <MultiChaifen chars="卿雲爛兮糾縵縵兮" :size="35" />
<MultiChaifen chars="日月光華旦復旦兮" :size="35" />
<MultiChaifen chars="明明上天爛然星陳" :size="35" />
<MultiChaifen chars="日月光華弘於一人" :size="35" /> -->

::: tip 致有緣人

當你點開這個頁面的時候，你就是一名有緣人。

從第一次牙牙學語，到知道自己名字的寫法，再到於潔白的信紙上寫下洋洋灑灑的文章。這每一座人生的里程碑，都是一次同母語母文的邂逅和牽連。上下五千年，東西九萬里，中國歷史上，多少人曾窮經皓首、青燈紅燭，在不同的載體上，寫下一個又一個的漢字。只在那方寸之間，將燦爛的中華文明，傳承了一代又一代。

你是否懷念初中時代的書桌前，用幾種顏色的中性筆，書寫着自己青春的悸動？你是否記得高中時代，你曾以筆爲劍，書寫着生活、對國家的思考？你是否想起，曾經一筆一劃抄錄過下唐詩宋詞。那些波瀾壯闊，抑或是清新雋永的詩句，至今還讓你不時地想起而心潮澎湃？

如果你懷念這種一筆一劃書寫地感覺，那麽，你來對了地方。

宇浩輸入法，就是這樣的一款輸入法：他爲了創作而設計，對漢字懷有一份脉脉的溫情。不同於拼音輸入法需要先輸入讀音，再選擇想要的漢字，宇浩輸入法將漢字的部首和筆畫，安排在鍵盤的 26 個按鍵上。當你連續按下一個漢字中若干部首，這個漢字便會跳到屏幕上。在宇浩輸入法中，每一個漢字，都基本對應着唯一的編碼。因此在輸入地過程中，你並不需要進行「選擇漢字」這個操作。就像你在寫字的時候，從不會停下來選擇漢字。

用了它，你在打字中便不會經歷惱人的停頓，在無盡的菜單欄中搜索想要的那個漢字；你可以如同在紙上書寫一般打字，享受一種「下筆如有神」的自由感和「我書我所想」的掌控度。你甚至可以忽略輸入框，享受閉眼創作的樂趣，自由書寫古今漢字，在現代文、文言文之間隨心徜徉。

文字不再是一匹匹無羈的野馬，而是你指間緩緩流淌的旋律。

「確定帶來自由」。如果你心動於這種體驗，説明你是一個既浪漫又有品味的人，不妨加入我們吧！

:::

::: info 鳴謝

感謝以下字形輸入法的發明人、改編人、維護人、各平臺方案製作者、插件作者、網頁作者等：

- [王碼五筆字形@王永民](http://www.wangma.net.cn/)
- [鄭碼@鄭易理 鄭瓏](https://www.china-e.com.cn/li/main/zhengma/jj.htm)
- [倉頡@朱邦復](http://www.cbflabs.com/)
- [山人全息@謝振斌](https://siuze.github.io/ShanRenMaLTS/)
- [爾雅徐碼@徐國銀](http://xumax.cn/)〔[五二頂@局外人](https://github.com/Ace-Who/rime-xuma?tab=readme-ov-file)〕
- [真碼@命](http://sixchou.ysepan.com/)
- [C42@譚淞宸](https://github.com/tansongchen/c42)〔[漢字自動拆分系統](https://chaifen.app/)〕
- [092](https://092wb.github.io/)
- [三碼鄭碼@史岳](http://zzzm.ysepan.com/?xzpd=1)
- [小鶴音形@何海峰](https://flypy.com/)
- 藍寶石@秋風
- [虎碼@PeaceB](https://www.tiger-code.com/)〔[虎碼測評網](http://assess.tiger-code.com/)〕
- [逸碼@小泥巴](https://yb6b.github.io/yima/graceful-code/)
- [易碼@小泥巴](https://yb6b.github.io/yima/)〔[測評工具](https://yb6b.github.io/#/)〕
- [吉蛋餅](https://lost-melody.github.io/wafel/)〔[倉輸入法工具
](https://lost-melody.github.io/hamster-tools/)〕
[雲碼@爲雲](https://github.com/orbitoo/kumo)
[天碼@宋天](http://soongsky.com/sky/)
[聲筆系列@戴石麟](https://sbxlm.github.io/)
[星空鍵道@吅吅大山](https://xkinput.github.io/)〔[星猫鍵道](https://github.com/hugh7007/xmjd6-rere)〕

---

感謝在輸入法的制作過程中，參與初期討論和構思、幫助測試和宣傳、提供技術支持、參與生態建設的朋友：

錢多多、阿吉、[王牌餅乾](https://github.com/lost-melody)、[宋天](http://soongsky.com/)、[yb](https://github.com/yb6b)。

還有不少朋友爲輸入法的優化提出了寶貴的意見和建議，爲輸入法的推廣助力，此處不一一致谢。

---

感謝以下輸入平臺：

[Rime中州韻](https://rime.im/)、[倉輸入法](https://ihsiao.com/apps/hamster/)、[小小輸入法](https://yong.dgod.net/)、大大輸入法、百度輸入法、搜狗輸入法

---

感謝以下文化平臺和項目：

[漢典網](https://www.zdic.net/)、[葉典網](http://yedict.com/zslf.htm)、[字統網](https://zi.tools/)、[天珩字庫](http://cheonhyeong.com/Simplified/download.html)、[思源宋體](https://source.typekit.com/source-han-serif/cn/)

---

感謝以下網頁框架、信息技術軟件、技術項目：

[Vitepress](https://vitepress.dev/zh/)、[Just the docs](https://just-the-docs.com/)、[Python](https://www.python.org/)〔[Pandas](https://pandas.pydata.org/)〕、[Visual Studio Code](https://code.visualstudio.com/)、[FontForge](https://fontforge.org/en-US/)、[Hanzi Writer](https://hanziwriter.org/cn/)

---

感謝所有致力於中華文化傳承發揚的前輩。

**知識的傳承和發展，是人類通天的階梯**

:::
