<!-- do not translate -->
# 展望未來

本頁面展示「宇浩拆分」和「宇浩方案」正在開發的功能。[下載安裝包請移步綱盤](http://zhuyuhao.ysepan.com/) 。

## 測試中

Unicode post 16.0 預備計劃，拓展宇浩拆分至 Unicode ext-J 區塊的新漢字。

[拆分工作進展詳見此頁](https://github.com/forFudan/ids/blob/main/ids.txt)

## 更新和修補

- 卿雲方案中的<span class="yuniversus"></span>字根編碼由`Dg`改爲`Sv`。受此影響，`就`代替`被`成爲`S`上的一級簡碼。
- 卿雲方案中的<span class="yuniversus">了</span>字根編碼由`Ll`改爲`Vl`。受此影響，`了`代替`原`成爲`V`上的一級簡碼，`道`代替`了`成爲`L`上的一級簡碼。
- 卿雲方案中的<span class="yuniversus">水氺</span>字根編碼由`Ns`改爲`Es`。受此影響，`没`代替`水`成爲`Ns`上的二級簡碼。
- 卿雲方案中的<span class="yuniversus"><ruby><rt>luò</rt></ruby></span>字根編碼由`Dl`改爲`Sl`。
- 卿雲方案中的「<ruby>爿<rt>pán</rt></ruby>」字根編碼由`Tq`改爲`Tp`，和「<ruby>片<rt>piàn</rt></ruby>」字根歸併。

重碼變化：
```
GB0 重码: 521  国字常用重码: 186  GBK 重码: 6099  全字集重码: 66642
GB0 new 承遇缎爿樗榱
GB0 old 近斥茧汨泓灏氵蠃水孓沓
Guoyu new 
Guoyu old 孓斥
GB0 + Guoyu new 承涼間遇跫缎爿樗榱
GB0 + Guoyu old 斥茧汨泓灏氵蠃水孓
```

## 命名

相關測試版本命名規則爲`vx.y.z-beta.{%YY%mm%dd}`。
