<script setup>
import IntroductoryCard from "./components/IntroductoryCard.vue";

import HomeTop from "./components/HomeTop.vue";
import { ref, watch, computed, onMounted, onUnmounted } from "vue";

const cards = [
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

const viewProgress = {
  offsetTop: [0],
  elements: [],
  index: 0,
  length: 0,
  scrollY: ref(0),
  _toviewIng: false,
  listenerTimer: null,
  correctIndex() {
    let correction = Math.floor(window.scrollY / window.innerHeight);
    if (correction == this.index) return;
    this.index = correction;
  },
  correctIndexUp() {
    let correction = Math.floor(window.scrollY / window.innerHeight);
    if (correction == this.index) return false;
    this.index = correction;
    return true;
  },
  addIndex() {
    let correction = Math.floor(window.scrollY / window.innerHeight) + 1;
    if (correction >= this.length || correction == this.index) return false;
    this.index = correction;
    return true;
  },
  scrollTo() {
    window.scrollTo({
      top: this.index == 0 ? 0 : this.elements[this.index].offsetTop,
      behavior: "smooth",
    });
  },
  toView() {
    // console.log('before', this.index)
    if (this._toviewIng || !this.addIndex()) return;
    this.scrollTo();
    this._toviewIng = true;
    this.listenerTimer = setTimeout(() => {
      this._toviewIng = false;
      this.correctIndex();
    }, 600);
  },
  toUpView() {
    if (!this.correctIndexUp()) return;
    // this.scrollTo();
  },
};

watch(
  () => viewProgress.scrollY.value,
  (top, preTop) => {
    if (top > preTop) {
      viewProgress.toView();
      return;
    }
    viewProgress.toUpView();
  }
);

function scrollListerner() {
  viewProgress.scrollY.value = window.scrollY;
}

const CardsView = ref(null);
const Home = ref(null);
onMounted(() => {
  let homeChildren = Home.value.children;
  let ls = [homeChildren[0], ...homeChildren[1].children];
  ls.forEach((e) => {
    viewProgress.elements.push(e);
    viewProgress.length++;
  });

  // pc 上加入切换动画
  if (
    !/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(
      navigator.userAgent
    )
  ) {
    window.addEventListener("scroll", scrollListerner);
  }
});
onUnmounted(() => {
  window.removeEventListener("scroll", scrollListerner);
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
