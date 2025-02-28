<!-- do not translate -->
# 展望未來

本頁面展示「宇浩拆分」和「宇浩方案」正在開發的功能。[下載安裝包請移步綱盤](http://zhuyuhao.ysepan.com/) 。

## 測試中

Unicode post 16.0 預備計劃，拓展宇浩拆分至 Unicode ext-J 區塊的新漢字。

[拆分工作進展詳見此頁](https://github.com/forFudan/ids/blob/main/ids.txt)

## 功能變化

- 增加 `/` 引導的特殊符號範圍。包括不限於：
  - 旗識。
  - 漢語拼音音節。
  - 繪文字。
- 爲 `/` 引導的特殊符號提供注解。
- 現在可輸入 `/gh`, `/xc`, `qy` + 字母來查詢字根編碼。此前卿雲中的 `zaa` 等命令停止使用，這使得 `Z` 鍵上屏歷史字詞不再受到影響。
- 方案默認優先極常用字以及包含極常用字的詞語。
- 優化詞庫，不再單設文學詞庫，其中的常用成語和詩詞併入核心詞庫中。

## 拆分更新

### 增加

諺文字母和音節。

### 修正

```
至 CJK 改變 2 个: 兂齑   
至 CJK-A 改變 0 个:    
至 CJK-B 改變 9 个: 𠕢𡆪𡔥𡯔𢛭𣓟𥜭𩨧𪓴   
至 CJK-C 改變 0 个:    
至 CJK-D 改變 0 个:    
至 CJK-E 改變 0 个:    
至 CJK-F 改變 0 个:    
至 CJK-G 改變 1 个: 𱀲   
至 CJK-H 改變 5 个: 𱞜𱟞𱨾𱹌𱻀   
至 CJK-I 改變 0 个:    
```

## 方案更新

修改卿雲方案的字根編碼如下：

- <span class="yuniversus"></span>字根編碼由`Dg`改爲`Sv`。受此影響，`就`代替`被`成爲`S`上的一級簡碼。
- <span class="yuniversus">了</span>字根編碼由`Ll`改爲`Vl`。受此影響，`了`代替`原`成爲`V`上的一級簡碼，`道`代替`了`成爲`L`上的一級簡碼。
- <span class="yuniversus">水氺</span>字根編碼由`Ns`改爲`Es`。受此影響，`没`代替`水`成爲`Ns`上的二級簡碼。
- <span class="yuniversus"><ruby>巳<rt>sì</rt></ruby></span>字根編碼由`Os`改爲`Ns`。
- <span class="yuniversus"><ruby>曲<rt>sì</rt></ruby></span>字根編碼由`Vq`改爲`Nq`。
- <span class="yuniversus"><ruby><rt>luò</rt></ruby></span>字根編碼由`Dl`改爲`Sl`。
- <span class="yuniversus"></span>（第二筆是點或捺）字根編碼由`Ae`改爲`Je`。<span class="yuniversus">二冫</span>（第二筆是撗或提）字根編碼不變。
- <ruby>爿<rt>pán</rt></ruby>字根編碼由`Tq`改爲`Tp`，和「<ruby>片<rt>piàn</rt></ruby>」字根歸併。
- <ruby>ㄩ<rt>yū</rt></ruby>（這是個注音符號）字根編碼由`Jk`改爲`Jv`。
- <ruby>咼<rt>guō wāi hé wǒ wō guǎ kuāi</rt></ruby>字根編碼由`Cg`改爲`Ck`。
- <ruby>罒<rt>wǎng sì mù</rt></ruby>字根編碼由`Xw`改爲`Xm`。

卿雲重碼變化：
```
GB0 重码: 510  国字常用重码: 184  GBK 重码: 6119  全字集重码: 66626
GB0 new 承曰凵遇爿樗榱缎
GB0 old 荣寒龋刳齿衾茧祀荬孓寨灏让纣泓水导匏斥汨龅近沓蠃
Guoyu new 炮燬
Guoyu old 巳寒孓寨上斥
GB0 + Guoyu new 承曰跫燬凵遇爿樗榱間炮涼缎
GB0 + Guoyu old 荣寒龋刳齿衾茧祀荬孓寨灏让纣泓水导匏尽斥鈞汨龅蠃
```

## 命名

相關測試版本命名規則爲`vx.y.z-beta.{%YY%mm%dd}`。
