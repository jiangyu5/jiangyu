<script setup>
import IntroductoryCard from "./components/IntroductoryCard.vue";

import defaultImg from "../../assets/bg_header.jpg";
import HomeTop from "./components/HomeTop.vue";

const cards = [
  {
    title: "文档目录",
    catologue: "文档",
    url: "notebook/",
    introduction:
      "这里是我的笔记本，对所学习的内容进行了选择性地复制粘贴，一点点只适合自己的理解上的修改。文档简洁，能够帮助我快速复习知识点。同时，这里也对笔记本的使用进行了不必要的简单说明。",
  },
  {
    title: "分类",
    catologue: "导航",
    url: "catalogue",
    introduction: "在这里，对文档进行了分类，我自己可以快速找到相关的文档。",
  },
  {
    title: "网址收藏",
    catologue: "导航",
    url: "links",
    introduction: "这里是我的个人网站收藏夹，或许有你一直在找的工具网站。",
  },
  {
    title: "关于",
    catologue: "导航",
    url: "about",
    introduction: "本站所使用到的图片等素材，都会在关于页标注来源。",
  },
];

cards.forEach((e, index) => {
  if (index % 2) {
    e["reverse"] = true;
  } else {
    e["reverse"] = false;
  }
  e["imgUrl"] = defaultImg;
});
</script>

<template>
  <div class="home">
    <HomeTop />
    <div ref="CardsView">
      <IntroductoryCard v-for="card in cards" v-bind="card" />
    </div>
  </div>
</template>

<style scoped lang="less">

</style>
