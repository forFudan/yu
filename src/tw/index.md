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
      text: 介紹信
      link: /docs/
    - theme: alt
      text: 說明書
      link: /learn/
    - theme: alt
      text: 練習簿
      link: /practice/root
    - theme: alt
      text: 安裝包
      link: /install

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
</script>
<Search zigenUrl="/zigen-star.csv" supplement />

---

::: tip 致有緣人

<svg style="width: 75px; height: 75px; margin-right: 5px;"><g transform="translate(0, 65.91796875) scale(0.0732421875, -0.0732421875)"><path d="M 276 522 Q 228 518 190 513 Q 163 510 176 529 Q 236 635 294 713 Q 307 731 305 738 Q 302 753 262 782 Q 246 795 227 791 Q 217 788 223 773 Q 241 734 163 582 Q 147 548 111 515 Q 93 499 96 487 Q 102 468 117 451 Q 127 441 140 449 Q 162 465 238 490 Q 248 493 258 495 C 287 502 306 525 276 522 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 327 404 Q 282 395 229 377 Q 207 367 221 387 Q 255 436 336 535 Q 361 571 385 591 Q 397 601 391 610 Q 381 628 349 645 Q 334 654 325 651 Q 315 648 318 633 Q 321 600 276 522 L 258 495 Q 168 371 149 360 Q 136 351 139 338 Q 140 325 166 308 Q 176 298 190 309 Q 244 351 334 388 L 336 388 C 364 398 356 410 327 404 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 336 388 Q 345 369 361 362 Q 371 358 379 370 Q 383 380 381 397 Q 377 415 358 428 Q 331 453 318 460 Q 311 464 308 455 Q 304 448 327 404 L 336 388 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 100 165 Q 118 119 135 66 Q 139 50 154 42 Q 163 38 173 46 Q 183 56 191 85 Q 197 110 175 144 Q 150 175 119 207 Q 107 217 101 218 Q 95 218 90 206 Q 89 196 100 165 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 203 220 Q 216 198 228 172 Q 235 159 246 155 Q 255 154 261 161 Q 268 171 270 195 Q 270 222 212 256 Q 202 263 196 262 Q 192 261 190 251 Q 189 242 203 220 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 291 300 Q 318 246 340 240 Q 350 237 358 251 Q 362 261 357 280 Q 345 307 299 321 Q 292 324 289 315 Q 286 308 291 300 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 563 734 Q 581 759 600 781 Q 613 797 610 804 Q 609 817 572 846 Q 557 858 540 854 Q 530 851 536 837 Q 549 803 491 695 Q 479 671 454 649 Q 436 636 438 625 Q 442 607 455 591 Q 465 581 476 588 Q 507 603 612 619 Q 619 620 627 620 C 657 622 669 643 639 643 Q 579 643 529 641 Q 496 640 513 661 Q 534 695 555 723 L 563 734 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 600 534 Q 622 559 670 618 Q 715 676 758 708 Q 774 718 764 730 Q 752 742 719 762 Q 710 765 646 747 Q 582 735 563 734 C 543 732 543 732 555 723 Q 564 713 585 709 Q 594 708 658 716 Q 667 717 669 715 Q 673 711 667 698 Q 652 670 639 643 L 627 620 Q 605 580 588 552 Q 579 539 576 529 C 564 501 580 511 600 534 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 551 491 Q 671 521 860 520 Q 879 520 884 529 Q 888 539 873 551 Q 822 587 754 566 Q 697 554 615 537 Q 606 536 600 534 L 576 529 Q 491 517 398 500 Q 379 497 394 483 Q 407 471 423 467 Q 442 463 457 467 Q 484 476 514 483 L 551 491 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 513 403 Q 568 451 569 457 L 569 460 Q 569 469 553 489 L 551 491 C 532 514 523 511 514 483 Q 502 437 393 344 Q 384 340 382 335 Q 378 328 388 327 Q 412 327 491 385 L 513 403 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 642 313 Q 641 314 641 313 L 627 329 Q 579 380 513 403 C 485 414 465 401 491 385 Q 500 379 511 373 L 560 340 Q 573 328 586 314 L 616 258 Q 634 192 607 96 Q 597 56 584 50 Q 577 46 518 54 Q 478 63 476 56 Q 475 49 487 35 Q 544 -14 566 -48 Q 581 -67 597 -64 Q 648 -37 669 84 Q 681 162 668 246 C 664 276 662 292 642 313 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 511 373 Q 493 307 344 190 Q 328 178 349 181 Q 415 187 519 296 Q 538 317 560 340 C 581 362 520 402 511 373 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 586 314 Q 526 182 336 47 Q 323 35 332 33 Q 351 24 427 68 Q 497 107 579 209 Q 615 252 614 255 Q 615 256 616 258 C 631 284 599 341 586 314 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 641 313 Q 732 377 780 402 Q 799 406 795 418 Q 789 434 770 454 Q 751 473 728 476 Q 712 476 713 456 Q 714 441 705 425 Q 677 388 627 329 C 608 306 616 296 641 313 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 668 246 Q 735 167 815 84 Q 834 68 861 70 Q 957 82 986 90 Q 995 93 996 97 Q 996 101 983 108 Q 845 150 758 217 Q 704 259 642 313 C 619 333 649 269 668 246 Z" style="fill: rgb(44, 150, 255);"></path></g></svg>

當你點開這個頁面的時候，你就是一名有緣人。

從第一次牙牙學語，到知道自己名字的寫法，再到於潔白的信紙上寫下洋洋灑灑的文章。這每一座人生的里程碑，都是一次同母語母文的邂逅和牽連。上下五千年，東西九萬里，中國歷史上，多少人曾窮經皓首、青燈紅燭，在不同的載體上，寫下一個又一個的漢字。只在那方寸之間，將燦爛的中華文明，傳承了一代又一代。

你是否懷念初中時代的書桌前，用幾種顏色的中性筆，書寫著自己青春的悸動？你是否記得高中時代，你曾以筆為劍，書寫著生活、對國家的思考？你是否想起，曾經一筆一劃抄錄過下唐詩宋詞。那些波瀾壯闊，抑或是清新雋永的詩句，至今還讓你不時地想起而心潮澎湃？

如果你懷念這種一筆一劃書寫地感覺，那麼，你來對了地方。

宇浩輸入法，就是這樣的一款輸入法：他為了創作而設計，對漢字懷有一份脈脈的溫情。不同於拼音輸入法需要先輸入讀音，再選擇想要的漢字，宇浩輸入法將漢字的部首和筆畫，安排在鍵盤的 26 個按鍵上。當你連續按下一個漢字中若干部首，這個漢字便會跳到屏幕上。在宇浩輸入法中，每一個漢字，都基本對應著唯一的編碼。因此在輸入地過程中，你並不需要進行「選擇漢字」這個操作。就像你在寫字的時候，從不會停下來選擇漢字。

用了它，你在打字中便不會經歷惱人的停頓，在無盡的菜單欄中搜索想要的那個漢字；你可以如同在紙上書寫一般打字，享受一種「下筆如有神」的自由感和「我書我所想」的掌控度。你甚至可以忽略輸入框，享受閉眼創作的樂趣，自由書寫古今漢字，在現代文、文言文之間隨心徜徉。

文字不再是一匹匹無羈的野馬，而是你指間緩緩流淌的旋律。

「確定帶來自由」。如果你心動於這種體驗，說明你是一個既浪漫又有品味的人，不妨加入我們吧！

:::

![yustar](/yustar.png)

![assess](/assess.png)

::: info 鳴謝

感謝以下字形輸入法的發明人、改編人、維護人、各平臺方案製作者、插件作者、網頁作者等：

[王碼五筆字形](http://www.wangma.net.cn/)、[鄭碼](https://www.china-e.com.cn/li/main/zhengma/jj.htm)、[倉頡](http://www.cbflabs.com/)、[山人全息](https://siuze.github.io/ShanRenMaLTS/)、[爾雅徐碼](http://xumax.cn/)〔[五二頂](https://github.com/Ace-Who/rime-xuma?tab=readme-ov-file)〕、真碼、[C42](https://github.com/tansongchen/c42)〔[漢字自動拆分系統](https://chaifen.app/)〕、092、[三碼鄭碼](http://zzzm.ysepan.com/?xzpd=1)、[小鶴音形](https://flypy.com/)、藍寶石、[虎碼](https://www.tiger-code.com/)〔[虎碼測評網](http://assess.tiger-code.com/)〕、[逸碼](https://yb6b.github.io/yima/graceful-code/)、[易碼](https://yb6b.github.io/yima/)〔[測評工具](https://yb6b.github.io/#/)〕、[吉蛋餅](https://lost-melody.github.io/wafel/)〔[倉輸入法工具
](https://lost-melody.github.io/hamster-tools/)〕、[雲碼](https://github.com/orbitoo/kumo)、天碼、[聲筆系列](https://sbxlm.github.io/)、[星空鍵道](https://xkinput.gitee.io/)〔[星貓鍵道](https://github.com/hugh7007/xmjd6-rere)〕

---

感謝在輸入法的製作過程中，參與初期討論和構思、幫助測試和宣傳、提供技術支持、參與生態建設的朋友：

錢多多、阿吉、王牌餅乾、宋天、yb。

還有不少朋友為輸入法的優化提出了眾多寶貴的意見和建議，此處不一一致謝。

---

感謝以下輸入平臺：

[Rime中州韻](https://rime.im/)、[倉輸入法](https://ihsiao.com/apps/hamster/)、[小小輸入法](https://yong.dgod.net/)、大大輸入法、百度輸入法、搜狗輸入法

---

感謝以下文化平臺：

[漢典網](https://www.zdic.net/)、[葉典網](http://yedict.com/zslf.htm)、[字統網](https://zi.tools/)、[天珩字庫](http://cheonhyeong.com/Simplified/download.html)、[思源宋體](https://source.typekit.com/source-han-serif/cn/)

---

感謝以下網頁框架和信息技術軟件：

[Vitepress](https://vitepress.dev/zh/)、[Just the docs](https://just-the-docs.com/)、[Python](https://www.python.org/)〔[Pandas](https://pandas.pydata.org/)〕、[Visual Studio Code](https://code.visualstudio.com/)、[FontForge](https://fontforge.org/en-US/)

---

感謝所有致力於中華文化傳承發揚的前輩。

**知識的傳承和發展，是人類通天的階梯**

:::