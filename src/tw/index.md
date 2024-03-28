---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "宇浩輸入法"
  text: "情繫漢字 溝通古今"
  tagline: 全漢字字形输入・繁簡通打・極低選重
  image:
    dark: /logo_purple.png
    light: /logo_blue.png
    alt: yuhao-logo
  actions:
    - theme: brand
      text: 介紹信
      link: /tw/docs/
    - theme: alt
      text: 說明書
      link: /tw/learn/
    - theme: alt
      text: 練習簿
      link: /practice/root
    - theme: alt
      text: 安裝包
      link: /install

<!-- features:
  - title: 繁简通打
    details: 繁简汉字编码分离，故而繁简混合文本也不极少选重。
  - title: 动静低重
    details: 在输入常用繁简汉字时，绝对重码数和选重频率都极低。
  - title: 字根聚类
    details: 对相似字形进行聚类，学习更加便捷，维护成本更低。
  - title: 兼顾手感
    details: 减少别手的按键组合频率，且双手互击表现突出。 -->
---

<script setup>
import Search from '@/search/FetchSearch.vue'
</script>
<Search zigenUrl="/zigen-star.csv" supplement />

---

::: tip 致有緣人

當你點開這個頁面的時候，你就是個有緣人。

從第一次牙牙學語，到知道自己名字的寫法，再到於潔白的信紙上寫下洋洋灑灑的文章。 這每一座人生的里程碑，都是同母語母語的邂逅與牽連。 上下五千年，東西九萬裡，中國歷史上，多少人曾經窮經皓首、青燈紅燭，在不同的載體上，寫下一個又一個的漢字。 只在那方寸之間，將燦爛的中華文明，傳承了一代又一代。

你是否懷念國中時代的書桌前，用幾種顏色的中性筆，寫著自己青春的悸動？ 你是否記得高中時代，你曾以筆為劍，寫著生活、對國家的思考？ 你是否想起，曾經一筆一劃抄錄過下唐詩宋詞。 那些波瀾壯闊，抑或是清新雋永的詩句，至今還讓你不時地想起而心潮澎湃？

如果你懷念這種一筆一劃書寫地感覺，那麼，你來對了地方。

宇浩輸入法，就是這樣的一種輸入法：他為了創作而設計，對漢字懷有一份脈脈的溫情。 有別於拼音輸入法需要先輸入發音，再選擇想要的漢字，宇浩輸入法將漢字的部首和筆畫，安排在鍵盤的 26 個按鍵上。 當你連續按下一個漢字中若干部首，這個漢字就會跳到螢幕上。 在宇浩輸入法中，每一個漢字，都基本上對應著唯一的編碼。 因此在輸入地過程中，你並不需要進行「選擇漢字」這個操作。 就像你在寫字的時候，從來不會停下來選擇漢字。

用了它，你在打字中便不會經歷惱人的停頓，在無盡的菜單欄中搜索想要的那個漢字；你可以如同在紙上書寫一般打字，享受一種“下筆如有神”的自由 感和「我書我所想」的掌控度。 你甚至可以忽略輸入框，享受閉眼創作的樂趣，自由書寫古今漢字，在現代文、文言文之間隨心徜徉。

文字不再是一匹匹無羈的野馬，而是你指間緩緩流動的旋律。

「確定帶來自由」。 如果你心動於這種體驗，表示你是一個既浪漫又有品味的人，不妨加入我們吧！

:::

![yustar](/yustar.png)

::: info 鳴謝

感謝以下字形輸入法的發明者、改編人、維護人、各平台方案製作者、插件作者、網頁作者等：

[王碼五筆字形](http://www.wangma.net.cn/)、[鄭碼](https://www.china-e.com.cn/li/main/zhengma/jj.htm) 、[倉頡](http://www.cbflabs.com/)、[山人全像](https://siuze.github.io/ShanRenMaLTS/)、[爾雅徐碼](http://xumax.cn/)〔[五二頂](https://github.com/Ace-Who/rime-xuma?tab=readme-ov-file)〕、真碼、[C42](https://github.com/tansongchen/c42)〔[漢字自動分割系統](https://chaifen.app/)〕、092、[三碼鄭碼](http://zzzm.ysepan.com/?xzpd=1)、 [小鶴音形](https://flypy.com/)、藍寶石、[虎碼](https://www.tiger-code.com/)〔[虎碼評測網](http://assess.tiger-code.com/)〕、[逸碼](https://yb6b.github.io/yima/graceful-code/)、[易碼](https://yb6b.github.io/yima/ )〔[評測工具](https://yb6b.github.io/#/)〕、[吉蛋餅](https://lost-melody.github.io/wafel/)〔[倉輸入法工具](https://lost-melody.github.io/hamster-tools/)〕、[雲碼](https://github.com/orbitoo/kumo)、天碼、[聲筆系列](https://sbxlm.github.io/)、[星空鍵道](https://xkinput.gitee.io/)〔[星貓鍵道](https://github.com/hugh7007/xmjd6-rere)〕

---

感謝在輸入法的製作過程中，參與初期討論和構思、幫助測試和宣傳、提供技術支援、參與生態建設的朋友：

錢多多、阿吉、王牌餅乾、宋天、yb。

還有不少朋友為輸入法的優化提出了許多寶貴的意見和建議，此處不一一致謝。

---

感謝以下輸入平台：

[Rime中州韻](https://rime.im/)、[倉輸入法](https://ihsiao.com/apps/hamster/)、[小輸入法](https://yong.dgod.net/)、大幅輸入法、百度輸入法、搜狗輸入法

---

感謝以下文化平台：

[漢典網](https://www.zdic.net/)、[葉典網](http://yedict.com/zslf.htm)、[字統網](https://zi.tools/ )、[天珩字庫](http://cheonhyeong.com/Simplified/download.html)、[思源宋體](https://source.typekit.com/source-han-serif/cn/)

---

感謝以下網頁框架與資訊科技軟體：

[Vitepress](https://vitepress.dev/zh/)、[Just the docs](https://just-the-docs.com/)、[Python](https://www.python.org/ )〔[Pandas](https://pandas.pydata.org/)〕、[Visual Studio Code](https://code.visualstudio.com/)、[FontForge](https://fontforge.org/en-US/)

---

感謝所有致力於中華文化傳承發揚的前輩。

**知識的傳承與發展，是人類通天的階梯**

:::