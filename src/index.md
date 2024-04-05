---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "宇浩输入法"
  text: "情系汉字 沟通古今"
  tagline: 全汉字字形输入・繁简通打・极低选重
  image:
    dark: /logo_purple.png
    light: /logo_blue.png
    alt: yuhao-logo
  actions:
    - theme: brand
      text: 介绍信
      link: /docs/
    - theme: alt
      text: 说明书
      link: /learn/
    - theme: alt
      text: 练习簿
      link: /practice/root
    - theme: alt
      text: 安装包
      link: /install

<!-- features:
  - title: 繁简通打
    details: 繁简汉字编码分离，故而繁简混合文本也能极少选重。
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

::: tip 致有缘人

<svg style="width: 75px; height: 75px; margin-right: 5px;"><g transform="translate(0, 65.91796875) scale(0.0732421875, -0.0732421875)"><path d="M 276 522 Q 228 518 190 513 Q 163 510 176 529 Q 236 635 294 713 Q 307 731 305 738 Q 302 753 262 782 Q 246 795 227 791 Q 217 788 223 773 Q 241 734 163 582 Q 147 548 111 515 Q 93 499 96 487 Q 102 468 117 451 Q 127 441 140 449 Q 162 465 238 490 Q 248 493 258 495 C 287 502 306 525 276 522 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 327 404 Q 282 395 229 377 Q 207 367 221 387 Q 255 436 336 535 Q 361 571 385 591 Q 397 601 391 610 Q 381 628 349 645 Q 334 654 325 651 Q 315 648 318 633 Q 321 600 276 522 L 258 495 Q 168 371 149 360 Q 136 351 139 338 Q 140 325 166 308 Q 176 298 190 309 Q 244 351 334 388 L 336 388 C 364 398 356 410 327 404 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 336 388 Q 345 369 361 362 Q 371 358 379 370 Q 383 380 381 397 Q 377 415 358 428 Q 331 453 318 460 Q 311 464 308 455 Q 304 448 327 404 L 336 388 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 100 165 Q 118 119 135 66 Q 139 50 154 42 Q 163 38 173 46 Q 183 56 191 85 Q 197 110 175 144 Q 150 175 119 207 Q 107 217 101 218 Q 95 218 90 206 Q 89 196 100 165 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 203 220 Q 216 198 228 172 Q 235 159 246 155 Q 255 154 261 161 Q 268 171 270 195 Q 270 222 212 256 Q 202 263 196 262 Q 192 261 190 251 Q 189 242 203 220 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 291 300 Q 318 246 340 240 Q 350 237 358 251 Q 362 261 357 280 Q 345 307 299 321 Q 292 324 289 315 Q 286 308 291 300 Z" style="fill: rgb(174, 1, 1);"></path><path d="M 563 734 Q 581 759 600 781 Q 613 797 610 804 Q 609 817 572 846 Q 557 858 540 854 Q 530 851 536 837 Q 549 803 491 695 Q 479 671 454 649 Q 436 636 438 625 Q 442 607 455 591 Q 465 581 476 588 Q 507 603 612 619 Q 619 620 627 620 C 657 622 669 643 639 643 Q 579 643 529 641 Q 496 640 513 661 Q 534 695 555 723 L 563 734 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 600 534 Q 622 559 670 618 Q 715 676 758 708 Q 774 718 764 730 Q 752 742 719 762 Q 710 765 646 747 Q 582 735 563 734 C 543 732 543 732 555 723 Q 564 713 585 709 Q 594 708 658 716 Q 667 717 669 715 Q 673 711 667 698 Q 652 670 639 643 L 627 620 Q 605 580 588 552 Q 579 539 576 529 C 564 501 580 511 600 534 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 551 491 Q 671 521 860 520 Q 879 520 884 529 Q 888 539 873 551 Q 822 587 754 566 Q 697 554 615 537 Q 606 536 600 534 L 576 529 Q 491 517 398 500 Q 379 497 394 483 Q 407 471 423 467 Q 442 463 457 467 Q 484 476 514 483 L 551 491 Z" style="fill: rgb(255, 189, 5);"></path><path d="M 513 403 Q 568 451 569 457 L 569 460 Q 569 469 553 489 L 551 491 C 532 514 523 511 514 483 Q 502 437 393 344 Q 384 340 382 335 Q 378 328 388 327 Q 412 327 491 385 L 513 403 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 642 313 Q 641 314 641 313 L 627 329 Q 579 380 513 403 C 485 414 465 401 491 385 Q 500 379 511 373 L 560 340 Q 573 328 586 314 L 616 258 Q 634 192 607 96 Q 597 56 584 50 Q 577 46 518 54 Q 478 63 476 56 Q 475 49 487 35 Q 544 -14 566 -48 Q 581 -67 597 -64 Q 648 -37 669 84 Q 681 162 668 246 C 664 276 662 292 642 313 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 511 373 Q 493 307 344 190 Q 328 178 349 181 Q 415 187 519 296 Q 538 317 560 340 C 581 362 520 402 511 373 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 586 314 Q 526 182 336 47 Q 323 35 332 33 Q 351 24 427 68 Q 497 107 579 209 Q 615 252 614 255 Q 615 256 616 258 C 631 284 599 341 586 314 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 641 313 Q 732 377 780 402 Q 799 406 795 418 Q 789 434 770 454 Q 751 473 728 476 Q 712 476 713 456 Q 714 441 705 425 Q 677 388 627 329 C 608 306 616 296 641 313 Z" style="fill: rgb(44, 150, 255);"></path><path d="M 668 246 Q 735 167 815 84 Q 834 68 861 70 Q 957 82 986 90 Q 995 93 996 97 Q 996 101 983 108 Q 845 150 758 217 Q 704 259 642 313 C 619 333 649 269 668 246 Z" style="fill: rgb(44, 150, 255);"></path></g></svg>

当你点开这个页面的时候，你就是一名有缘人。

从第一次牙牙学语，到知道自己名字的写法，再到于洁白的信纸上写下洋洋洒洒的文章。这每一座人生的里程碑，都是一次同母语母文的邂逅和牵连。上下五千年，东西九万里，中国历史上，多少人曾穷经皓首、青灯红烛，在不同的载体上，写下一个又一个的汉字。只在那方寸之间，将灿烂的中华文明，传承了一代又一代。

你是否怀念初中时代的书桌前，用几种颜色的中性笔，书写着自己青春的悸动？你是否记得高中时代，你曾以笔为剑，书写着生活、对国家的思考？你是否想起，曾经一笔一划抄录过下唐诗宋词。那些波澜壮阔，抑或是清新隽永的诗句，至今还让你不时地想起而心潮澎湃？

如果你怀念这种一笔一划书写地感觉，那么，你来对了地方。

宇浩输入法，就是这样的一款输入法：他为了创作而设计，对汉字怀有一份脉脉的温情。不同于拼音输入法需要先输入读音，再选择想要的汉字，宇浩输入法将汉字的部首和笔画，安排在键盘的 26 个按键上。当你连续按下一个汉字中若干部首，这个汉字便会跳到屏幕上。在宇浩输入法中，每一个汉字，都基本对应着唯一的编码。因此在输入地过程中，你并不需要进行「选择汉字」这个操作。就像你在写字的时候，从不会停下来选择汉字。

用了它，你在打字中便不会经历恼人的停顿，在无尽的菜单栏中搜索想要的那个汉字；你可以如同在纸上书写一般打字，享受一种「下笔如有神」的自由感和「我书我所想」的掌控度。你甚至可以忽略输入框，享受闭眼创作的乐趣，自由书写古今汉字，在现代文、文言文之间随心徜徉。

文字不再是一匹匹无羁的野马，而是你指间缓缓流淌的旋律。

「确定带来自由」。如果你心动于这种体验，说明你是一个既浪漫又有品味的人，不妨加入我们吧！

:::

![yustar](/yustar.png)

![assess](/assess.png)

::: info 鸣谢

感谢以下字形输入法的发明人、改编人、维护人、各平台方案制作者、插件作者、网页作者等：

[王码五笔字形](http://www.wangma.net.cn/)、[郑码](https://www.china-e.com.cn/li/main/zhengma/jj.htm)、[仓颉](http://www.cbflabs.com/)、[山人全息](https://siuze.github.io/ShanRenMaLTS/)、[尔雅徐码](http://xumax.cn/)〔[五二顶](https://github.com/Ace-Who/rime-xuma?tab=readme-ov-file)〕、真码、[C42](https://github.com/tansongchen/c42)〔[汉字自动拆分系统](https://chaifen.app/)〕、092、[三码郑码](http://zzzm.ysepan.com/?xzpd=1)、[小鹤音形](https://flypy.com/)、蓝宝石、[虎码](https://www.tiger-code.com/)〔[虎码测评网](http://assess.tiger-code.com/)〕、[逸码](https://yb6b.github.io/yima/graceful-code/)、[易码](https://yb6b.github.io/yima/)〔[测评工具](https://yb6b.github.io/#/)〕、[吉蛋饼](https://lost-melody.github.io/wafel/)〔[仓输入法工具
](https://lost-melody.github.io/hamster-tools/)〕、[云码](https://github.com/orbitoo/kumo)、天码、[声笔系列](https://sbxlm.github.io/)、[星空键道](https://xkinput.gitee.io/)〔[星猫键道](https://github.com/hugh7007/xmjd6-rere)〕

---

感谢在输入法的制作过程中，参与初期讨论和构思、帮助测试和宣传、提供技术支持、参与生态建设的朋友：

钱多多、阿吉、王牌饼干、宋天、yb。

还有不少朋友为输入法的优化提出了众多宝贵的意见和建议，此处不一一致谢。

---

感谢以下输入平台：

[Rime中州韵](https://rime.im/)、[仓输入法](https://ihsiao.com/apps/hamster/)、[小小输入法](https://yong.dgod.net/)、大大输入法、百度输入法、搜狗输入法

---

感谢以下文化平台：

[汉典网](https://www.zdic.net/)、[叶典网](http://yedict.com/zslf.htm)、[字统网](https://zi.tools/)、[天珩字库](http://cheonhyeong.com/Simplified/download.html)、[思源宋体](https://source.typekit.com/source-han-serif/cn/)

---

感谢以下网页框架和信息技术软件：

[Vitepress](https://vitepress.dev/zh/)、[Just the docs](https://just-the-docs.com/)、[Python](https://www.python.org/)〔[Pandas](https://pandas.pydata.org/)〕、[Visual Studio Code](https://code.visualstudio.com/)、[FontForge](https://fontforge.org/en-US/)

---

感谢所有致力于中华文化传承发扬的前辈。

**知识的传承和发展，是人类通天的阶梯**

:::