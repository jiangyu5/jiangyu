<script setup>
import ArticleTitlesAside from "./components/ArticleTitlesAside.vue";
import ArticlesAside from "./components/ArticlesAside.vue";

import ajax from "../../hook/ajax";
import { marked } from "marked";
import "../../assets/css/markdownstyle.less";

import {
  ref,
  reactive,
  watch,
  onMounted,
  onUnmounted,
  computed,
  nextTick,
} from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const dirInfo = reactive({}); // 文件夹数据,该数据还未用到
const aside = computed(() => {
  return dirInfo["files"];
});

const articleData = reactive({
  title: "",
  content: "",
});
// 更新 articleData 和 dirInfo 数据
watch(
  () => route.path,
  (to, from) => {
    if (!to.startsWith("/notebook")) return;
    let articleUrl = "";
    if (to.includes(".md")) {
      articleUrl = to;
      articleData.title = decodeURIComponent(
        to.slice(to.lastIndexOf("/") + 1, -3)
      );
    } else {
      articleData.title = decodeURIComponent(to.slice(to.lastIndexOf("/") + 1));
      articleUrl = to + "/index.md";
    }

    ajax(articleUrl)
      .then((res) => {
        articleData.content = marked(res);
      })
      .then(() => {
        progress.init();
      });

    let fromParent = from ? from.split("/").slice(0, -1) : from;
    let toParent = articleUrl.split("/").slice(0, -1);
    if (fromParent != toParent) {
      ajax("/data/" + toParent.join("/") + "/index.json").then((res) => {
        Object.assign(dirInfo, JSON.parse(res));
      });
    }
  },
  { immediate: true }
);

// 文档所有标题
const titles = computed(() => {
  let matchTitles = articleData.content.match(/<h\d id=(.*)<\/h\d>/g);
  if (!matchTitles) return [];
  return matchTitles.map((e) => {
    let temp = e.match(/(h\d) id="(.*?)"/);
    return {
      title: temp[2],
      h: temp[1],
    };
  });
});

// 阅读进度与锚点
// 需要完善视口的判定
const ArticleMain = ref();
const progress = {
  doms: [],
  index: ref(0),
  length: 0,
  viewHeight: window.innerHeight / 2,
  init() {
    // 路由变化时,接收完数据后触发
    this.doms = ArticleMain.value.querySelectorAll("h1, h2, h3, h4, h5, h6");
    this.index.value = 0;
    this.length = this.doms.length;
  },
  changeIndex(index) {
    this.index.value = index;
    this.doms[this.index.value].scrollIntoView(true);
  },
  titleTop() {
    return this.doms[this.index.value].getBoundingClientRect().top;
  },
  titleBottom() {
    return this.doms[this.index.value].getBoundingClientRect().bottom;
  },
  viewUp() {
    if (this.index.value >= this.length - 1) return;
    if (this.titleBottom() < this.viewHeight) this.index.value++;
  },
  viewDown() {
    if (this.index.value <= 0) return;
    if (this.titleTop() > this.viewHeight) this.index.value--;
  },
  listener() {
    this.viewUp();
    this.viewDown();
  },
};

function changeTitleIndex(index) {
  progress.changeIndex(index);
}

function progressListener() {
  progress.listener();
}

onMounted(() => {
  window.addEventListener("scroll", progressListener);
});

onUnmounted(() => {
  window.removeEventListener("scroll", progressListener);
});
</script>

<template>
  <div class="article">
    <ArticlesAside :data="aside"></ArticlesAside>
    <div class="article-main">
      <div class="article-main-header">{{ articleData.title }}</div>
      <div
        class="markdownstyle"
        v-html="articleData.content"
        ref="ArticleMain"
      ></div>
    </div>

    <ArticleTitlesAside
      :titles="titles"
      :active-title-index="progress.index.value"
      @change-title-index="changeTitleIndex"
    ></ArticleTitlesAside>
  </div>
</template>

<style scoped lang="less">
.article {
  user-select: text;
  -webkit-user-select: text;
  -moz-user-select: text;
  min-height: 100vh;
  width: calc(100vw - 17px);
  padding: 0 1em;
  margin: 0 auto;

  .articles-aside,
  .article-titles-aside {
    display: none;
    width: 100%;
    padding-top: 16px;
  }

  .article-main {
    padding-top: 16px;
    padding-bottom: 6em;
    .article-main-header {
      padding: 8px 16px;
      margin-bottom: 32px;
      font-size: 2.3em;
      line-height: 1.5em;
      color: white;
      font-weight: 600;
      align-self: end;
      background: url(../../assets/bg_header.jpg) center;
      background-size: cover;
    }
  }
}

@media (min-width: 667px) {
  .article {
    display: flex;
    flex-direction: row;
    flex-wrap: nowrap;
    justify-items: center;

    .articles-aside {
      width: 180px;
      display: block;
    }

    .articles-aside,
    .article-titles-aside {
      position: sticky;
      top: 26px;
      max-height: calc(100vh - 26px);
      width: 190px;
      overflow: auto;
      flex: 1 auto 0;
      padding-bottom: 20%;
    }

    .article-main {
      padding-left: 2em;
      padding-right: 2em;
      width: 500px;
      flex: 1 1;

      .article-main-header {
        @height: 3em;
        padding: @height 16px 8px;
        margin-bottom: 32px;
      }
    }
  }
}

@media (min-width: 1024px) {
  .article {
    .articles-aside {
      width: 220px;
    }

    .article-titles-aside {
      display: block;
      width: 220px;
    }

    .article-main {
      padding-left: 2.5em;
      padding-right: 2.5em;
      padding-bottom: 20vh;
    }
  }
}
</style>
