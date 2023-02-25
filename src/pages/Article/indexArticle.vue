<script setup>
import ArticleTitlesAside from "./components/ArticleTitlesAside.vue";
import ArticlesAside from "./components/ArticlesAside.vue";
import IsLoading from "../../components/isLoading.vue";

import "../../assets/css/markdownstyle.less";
import useArticle from "../../hook/useArticle";
import articleReadingProgress from "../../hook/articleReadingProgress";

import { ref, watch, nextTick } from "vue";

// 文档数据
const { articleUrl, articleTitle, articleContent, aside, titles } =
  useArticle();

// is-loading 是否出现
const isLoading = ref(true);
watch([articleUrl, articleContent], (v, o) => {
  isLoading.value = v[0] == o[0] ? false : true;
});

// 阅读进度
const ArticleMain = ref(null);
const { progress, titleIndex, changeTitleIndex } =
  articleReadingProgress(ArticleMain);
watch(
  articleContent,
  () => {
    nextTick(() => {
      progress.init();
    });
  },
  { immediate: true }
);
function eChangeTitleIndex(index) {
  changeTitleIndex(index);
}
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
      :title-index="titleIndex"
      @changeTitleIndex="eChangeTitleIndex"
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
    position: relative;

    .markdownstyle {
      padding-bottom: 6em;
    }

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
    }
  }
}
</style>
