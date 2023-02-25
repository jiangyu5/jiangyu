<script setup>
import IntroductoryCard from "./IntroductoryCard.vue";

import HomeTop from "./HomeTop.vue";
const cards = [
  {
    title: "简版 网易云音乐",
    catologue: "作品",
    href: 'https://github.com/jiangyu5/netease-cloud-music',
    introduction: "网页版网易云音乐。Vite + Vue + BootStrap 5，图标素材阿里图标，API 地址见作品 README。",
    imgUrl: "/assets/imgs/pc1.png",
  },
  {
    title: "文档",
    catologue: "笔记本",
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
    introduction: "或许，这里会很酷。",
  },
];

cards.forEach((e, index) => {
  if (index % 2) {
    e["reverse"] = true;
  } else {
    e["reverse"] = false;
  }
  //   e["imgUrl"] = defaultImg;
  e["num"] = index;
});
</script>

<template>
  <div class="home" ref="Home">
    <HomeTop />
    <div ref="CardsView">
      <IntroductoryCard v-for="card in cards" v-bind="card" />
    </div>
  </div>
</template>

<style scoped lang="less"></style>
