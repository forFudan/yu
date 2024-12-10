---
aside: false
---
# 光華·单字練習

你可以隨時暫停練習。你的練習進度會在同一設備上儲存。

<script setup>
import Train from "@/train/CharTrain.vue"
</script>
<div class="zigen-font">
<Train name="light" chaifenUrl="/chaifen_zhu.csv" zigenUrl="/zigen-light.csv" :range="[0,1000]" :supplement="true" />
</div>

:::details 键位图
![宇浩·光華字根图](/yulight.png)
:::

::: details 单字规则

定义：

- A 为首根大码，a 为首根小码。
- B 为第二根大码，b 为第二根小码。
- C 为第三根大码，b 为第三根小码。
- Z 为末根大码，z 为末根小码。

字根输入时:

- 代表根：大码 + 小码 + 小码
- 附属根：大码 + 小码 + 小码 + 小码

单字输入时：

- 取首、二、三、末根大码。
- 不足四码，末根小码补齐。
- 仍不足四码，首根小码补齐。

详解：
代表字根：

- Aaa
附属根：
- Aaaa
两根字：
- ABba
三根字：
- ABCc
四根及四根以上字：
- ABCZ
:::
