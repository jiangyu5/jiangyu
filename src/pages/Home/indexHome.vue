<script setup>
import SearchInput from "../../components/SearchInput.vue";
import IntroductoryCard from "./components/IntroductoryCard.vue";

import defaultImg from "../../assets/img_default.jpg";
import defaultImg2 from "../../assets/img_default2.jpg";
// import { ref, onMounted, nextTick, onUnmounted } from "vue";

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
    introduction:
      "本站所使用到的图片等素材，都会在关于页标注来源。",
  },
];

cards.forEach((e, index) => {
  if (index % 2) {
    e["reverse"] = true;
    e["imgUrl"] = defaultImg;
  } else {
    e["reverse"] = false;
    e["imgUrl"] = defaultImg2;
  }
});

// cardView 出现效果
// const Views = {
//   cards: [],
//   activeIndex: -1,
//   length: 0,
//   clientHeight: window.innerHeight,
//   offsetTop: 0,
//   preViewRect() {
//     if (this.activeIndex > 0) {
//       return this.cards[this.activeIndex - 1].getBoundingClientRect();
//     } else {
//       return null;
//     }
//   },
//   currentViewRect() {
//     if (this.activeIndex != -1) {
//       return this.cards[this.activeIndex].getBoundingClientRect();
//     } else {
//       return null;
//     }
//   },
//   _addActiveIndex() {
//     this.activeIndex += this.activeIndex < this.length - 1 ? 1 : 0;
//   },
//   _subActiveIndex() {
//     this.activeIndex -= this.activeIndex > 0 ? 1 : 0;
//   },
//   _viewShow() {
//     window.scrollTo({
//       top: this.offsetTop + this.clientHeight * this.activeIndex,
//       behavior: "smooth",
//     });
//   },
//   nextViewShow() {
//     if (this.activeIndex >= this.length - 1) return;
//     this._addActiveIndex();
//     this._viewShow();
//   },
//   preViewShow() {
//     if (this.activeIndex < 0) return;
//     this._subActiveIndex();
//     // this._viewShow();
//   },
// };

// function cardViewToTop() {
//   if (Views.activeIndex < 0) {
//     Views.nextViewShow();
//     return;
//   }

//   if (Views.currentViewRect().bottom < Views.clientHeight) {
//     Views.nextViewShow();
//   }

//   if (Views.activeIndex == Views.length - 1) {
//     window.removeEventListener("scroll", cardViewToTop);
//   }
// }

// const CardsView = ref(null);
// onMounted(() => {
//   [...CardsView.value.children].forEach((e) => {
//     Views.cards.push(e);
//     Views.length++;
//   });
//   Views.offsetTop = CardsView.value.offsetTop;
//   window.addEventListener("scroll", cardViewToTop);
// });

// onUnmounted(() => {
//   window.removeEventListener("scroll", cardViewToTop);
// });
</script>

<template>
  <div class="home">
    <div class="home-top">
      <div class="personal-signature">
        <p>“多情自古空余恨，</p>
        <p>好梦由来最易醒。”</p>
      </div>
      <SearchInput />
    </div>
    <div ref="CardsView">
      <IntroductoryCard v-for="card in cards" v-bind="card" />
    </div>
  </div>
</template>

<style scoped lang="less">
.home {
  .home-top {
    color: rgb(253, 253, 253);
    height: fit-content;
    background: url("../../assets/bg_header.jpg") no-repeat center;
    // background-attachment: fixed;
    background-size: cover;
    padding: 1rem 1rem 2rem;
    .personal-signature {
      font-size: 1em;
      line-height: 1.5em;
      font-weight: 600;
      letter-spacing: 0.05em;
      margin-bottom: 2rem;

      p:last-child {
        text-indent: 3.2em;
      }
    }

    .search-input {
      text-align: center;
    }
  }
}

@media screen and (min-width: 500px) {
  .home {
    .home-top {
      padding: 2rem 3rem 4rem;
      .personal-signature {
        font-size: 1.5em;
        margin-bottom: 3rem;
      }
    }
  }
}
</style>
