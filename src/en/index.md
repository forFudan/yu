---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "Yuhao Input Method"
  text: "Communicate the past and the present"
  tagline:  Effectively input 99000 Chinese Charaters
  image:
    dark: /logo_purple.png
    light: /logo_blue.png
    alt: yuhao-logo
  actions:
    - theme: brand
      text: intro
      link: /tw/docs/
    - theme: alt
      text: tutorial
      link: /tw/learn/
    - theme: alt
      text: practice
      link: /practice/root
    - theme: alt
      text: Install
      link: /install
---

<script setup>
import Search from '@/search/FetchSearch.vue'
</script>
<Search zigenUrl="/zigen-star.csv" supplement />

---
