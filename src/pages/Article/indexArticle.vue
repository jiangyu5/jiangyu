<script setup>
import ArticleTitlesAside from "./components/ArticleTitlesAside.vue";
import ArticlesAside from "./components/ArticlesAside.vue";

import useAjax from "../../hook/useAjax";
import { marked } from "marked";
import "../../assets/css/markdownstyle.less";

import { ref, watch, onMounted, onUnmounted, computed, nextTick } from "vue";
import { useRoute } from "vue-router";
import IsLoading from "../../components/isLoading.vue";

const route = useRoute();
const articleUrl = ref("");
const articleTitle = ref("");
const articleData = useAjax(articleUrl)["data"];
const articleContent = computed(() => {
  if (articleData.value) return marked(articleData.value);
  return "";
});

const asideUrl = computed(() => {
  let tempPath = articleUrl.value.split("/").slice(0, -1).join("/");
  if (tempPath == "/notebook" || tempPath == "")
    return "/data/notebook/index.json";
  return "/data" + tempPath + "/index.json";
});
const asideData = useAjax(asideUrl)["data"];
const aside = computed(() => {
  if (asideData.value) {
    return asideData.value["files"];
  }
  return null;
});

watch(
  () => route.path,
  (to) => {
    if (!to.startsWith("/notebook")) return;
    if (to.includes(".md")) {
      articleUrl.value = to;
      articleTitle.value = decodeURIComponent(
        to.slice(to.lastIndexOf("/") + 1, -3)
      );
    } else {
      articleTitle.value = decodeURIComponent(
        to.slice(to.lastIndexOf("/") + 1)
      );
      articleUrl.value = to + "/index.md";
    }
  },
  { immediate: true }
);

// 文档所有标题
const titles = computed(() => {
  let matchTitles = articleContent.value.match(/<h\d id=(.*)<\/h\d>/g);
  if (!matchTitles) return;
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
const ArticleMain = ref(null);
const titleIndex = ref(0);
const progress = {
  doms: [],
  index: 0,
  length: 0,
  viewHeight: window.innerHeight / 2,
  init() {
    // 路由变化时,接收完数据后触发
    this.doms = ArticleMain.value.querySelectorAll("h1, h2, h3, h4, h5, h6");
    this.length = this.doms.length;
    this.index = 0;
    titleIndex.value = 0;
  },
  changeIndex(index) {
    this.index = index;
    this.doms[this.index].scrollIntoView(true);
  },
  titleTop() {
    return this.doms[this.index].getBoundingClientRect().top;
  },
  titleBottom() {
    return this.doms[this.index].getBoundingClientRect().bottom;
  },
  viewUp() {
    if (this.index >= this.length - 1) return;
    if (this.titleBottom() < this.viewHeight) this.index++;
  },
  viewDown() {
    if (this.index <= 0) return;
    if (this.titleTop() > this.viewHeight) this.index--;
  },
  listener() {
    this.viewUp();
    this.viewDown();
    if (titleIndex.value != this.index) {
      titleIndex.value = this.index;
    }
  },
};

watch(articleContent, () => {
  nextTick(() => {
    progress.init(); // 初始化阅读进度
  });
});

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

// is-loading 是否出现
const isLoading = ref(true);
watch([articleUrl, articleContent], (v, o) => {
  isLoading.value = v[0] == o[0] ? false : true;
});
</script>

<template>
  <div class="article">
    <ArticlesAside :data="aside"></ArticlesAside>
    <div class="article-main">
      <div class="article-main-header">{{ articleTitle }}</div>
      <IsLoading v-show="isLoading" />
      <div
        v-show="!isLoading"
        class="markdownstyle"
        v-html="articleContent"
        ref="ArticleMain"
      ></div>
    </div>

    <ArticleTitlesAside
      :titles="titles"
      :activeTitleIndex="titleIndex"
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
    position: relative;

    .is-loading {
      height: calc(80vh - 11em);
    }
    .article-main-header {
      padding: 1em 16px 8px;
      margin-bottom: 32px;
      font-size: 1.5em;
      line-height: 1.5em;
      color: white;
      font-weight: 600;
      align-self: end;
      background-color: #a9c9fffc;
      background-image: linear-gradient(90deg, #73a6ff 0%, #ff95e1 100%);
      border-radius: 0.2em;
      opacity: 0.7;
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
