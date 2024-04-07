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
    - theme: brand
      text: 介紹
      link: /tw/docs/
    - theme: alt
      text: 教程
      link: /tw/learn/
    - theme: alt
      text: 練習
      link: /practice/root
    - theme: alt
      text: 安裝
      link: /tw/install

<!-- features:
  - title: 繁簡通打
    details: 繁簡漢字編碼分離，故而繁簡混合文本也能極少選重。
  - title: 動靜低重
    details: 在輸入常用繁簡漢字時，絕對重碼數和選重頻率都極低。
  - title: 字根聚類
    details: 對相似字形進行聚類，學習更加便捷，維護成本更低。
  - title: 兼顧手感
    details: 減少別手的按鍵組合頻率，且雙手互擊表現突出。 -->
---

<script setup>
import Search from '@/search/FetchSearch.vue'
import Chaifen from '@/chaifen/Chaifen.vue'
</script>
<Search zigenUrl="/zigen-star.csv" supplement />

---

<div class="flex justify-center flex-wrap">
<Chaifen char="光" id="宇" :parts='[3,3]' />
<Chaifen char='華' id='華' :parts='[4,5,2]' :colors='[1,2,3]' />
<Chaifen char="星" id="星" :parts='[4,5]' />
<Chaifen char="陳" id="陳" :parts='[2,1,4,3]' :colors='[1,2,3,2]' />
</div>

::: tip 致有緣人

當你點開這個頁面的時候，你就是一名有緣人。

從第一次牙牙學語，到知道自己名字的寫法，再到於潔白的信紙上寫下洋洋灑灑的文章。這每一座人生的里程碑，都是一次同母語母文的邂逅和牽連。上下五千年，東西九萬里，中國歷史上，多少人曾窮經皓首、青燈紅燭，在不同的載體上，寫下一個又一個的漢字。只在那方寸之間，將燦爛的中華文明，傳承了一代又一代。

你是否懷念初中時代的書桌前，用幾種顏色的中性筆，書寫著自己青春的悸動？你是否記得高中時代，你曾以筆為劍，書寫著生活、對國家的思考？你是否想起，曾經一筆一劃抄錄過下唐詩宋詞。那些波瀾壯闊，抑或是清新雋永的詩句，至今還讓你不時地想起而心潮澎湃？

如果你懷念這種一筆一劃書寫地感覺，那麼，你來對了地方。

宇浩輸入法，就是這樣的一款輸入法：他為了創作而設計，對漢字懷有一份脈脈的溫情。不同於拼音輸入法需要先輸入讀音，再選擇想要的漢字，宇浩輸入法將漢字的部首和筆畫，安排在鍵盤的 26 個按鍵上。當你連續按下一個漢字中若干部首，這個漢字便會跳到屏幕上。在宇浩輸入法中，每一個漢字，都基本對應著唯一的編碼。因此在輸入地過程中，你並不需要進行「選擇漢字」這個操作。就像你在寫字的時候，從不會停下來選擇漢字。

用了它，你在打字中便不會經歷惱人的停頓，在無盡的菜單欄中搜索想要的那個漢字；你可以如同在紙上書寫一般打字，享受一種「下筆如有神」的自由感和「我書我所想」的掌控度。你甚至可以忽略輸入框，享受閉眼創作的樂趣，自由書寫古今漢字，在現代文、文言文之間隨心徜徉。

文字不再是一匹匹無羈的野馬，而是你指間緩緩流淌的旋律。

「確定帶來自由」。如果你心動於這種體驗，說明你是一個既浪漫又有品味的人，不妨加入我們吧！

:::