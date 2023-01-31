<script setup>
import ArticleTitlesAside from "./components/ArticleTitlesAside.vue";
import ArticlesAside from "./components/ArticlesAside.vue";

import ajax from "../../hook/ajax";
import { marked } from "marked";
import "../../assets/css/markdownstyle.less";

import { ref, reactive, computed, watch, onUnmounted } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const aside = ref([]); // 左侧的相关文件列表
const htmlText = ref("");
const articleTitle = ref("");
const titles = computed(() => {
  let matchTitles = htmlText.value.match(/<h\d id=(.*)<\/h\d>/g);
  if (matchTitles) {
    return matchTitles.map((e) => {
      let temp = e.match(/(h\d) id="(.*?)"/);
      return {
        title: temp[2],
        h: temp[1],
      };
    });
  }
  return [];
});

// 阅读进度
const ArticleMain = ref();
const readingProgress = reactive({
  titlesDomArray: [],
  titleIndex: 0,
  titlesLength: 0,
});

// 跳转切换 这里需要整理
watch(
  () => route.fullPath,
  (to, from) => {
    if (to.indexOf("notebook") == -1) return;

    let indexJsonUrl = to;
    let mdUrl = to;
    let indexChange = true;

    if (to.indexOf(".md") != -1) {
      indexJsonUrl = to.split("/").slice(0, -1).join("/");
      indexChange =
        from && from.split("/").slice(0, -1).join("/") == indexJsonUrl
          ? false
          : true;
    } else {
      mdUrl = to + "/index.md";
    }

    // 文档标题
    articleTitle.value = decodeURIComponent(to)
      .replace(".md", "")
      .split("/")
      .pop();

    // 请求文档
    ajax(mdUrl)
      .then((res) => {
        htmlText.value = marked(res);
      })
      .then(() => {
        // 获取 reading process 需要的数据
        readingProgress.titlesDomArray = ArticleMain.value.querySelectorAll(
          "h1, h2, h3, h4, h5, h6"
        ); // 替换操作
        readingProgress.titlesLength = readingProgress.titlesDomArray.length;
        return readingProgress.titlesLength;
      })
      .then((titlesLength) => {
        // 添加监听事件
        window.removeEventListener("scroll", readingProgressListener);

        if (titlesLength > 1) {
          window.addEventListener("scroll", readingProgressListener);
        }
      });

    // 同级目录是否刷新
    if (indexChange) {
      ajax(indexJsonUrl + "/index.json").then((res) => {
        aside.value = JSON.parse(res);
      });
    }
  },
  {
    immediate: true,
  }
);

const hallfClientHeight = window.innerHeight / 2;
function readingProgressListener() {
  if (readingProgress.titlesLength - 1 > readingProgress.titleIndex) {
    let topPre =
      readingProgress.titlesDomArray[
        readingProgress.titleIndex + 1
      ].getBoundingClientRect().top;

    if (topPre && topPre < hallfClientHeight) {
      readingProgress.titleIndex += 1;
    }
  }

  if (readingProgress.titleIndex > 0) {
    let topCurrent =
      readingProgress.titlesDomArray[
        readingProgress.titleIndex
      ].getBoundingClientRect().top;

    if (topCurrent && topCurrent >= hallfClientHeight) {
      readingProgress.titleIndex -= 1;
    }
  }
}

function changeTitleIndex(index) {
  readingProgress.titlesDomArray[index].scrollIntoView({
    block: "center",
  });
  readingProgress.titleIndex = index;
}

onUnmounted(() => {
  window.removeEventListener("scroll", readingProgressListener);
});
</script>

<template>
  <div class="article">
    <ArticlesAside :data="aside"></ArticlesAside>
    <div class="article-main">
      <div class="article-main-header">{{ articleTitle }}</div>
      <div class="markdownstyle" v-html="htmlText" ref="ArticleMain"></div>
    </div>

    <ArticleTitlesAside
      @return-title-index="changeTitleIndex"
      :titles="titles"
      :active-title-index="readingProgress.titleIndex"
    ></ArticleTitlesAside>
  </div>
</template>

<style scoped lang="less">
.article {
  min-height: 100vh;
  width: calc(100vw - 17px);
  padding: 0 1em;
  margin: 0 auto;

  .articles-aside,
  .article-titles-aside {
    width: 100%;
    padding-top: 16px;
  }
  .article-titles-aside {
    display: none;
  }

  .article-main {
    padding-top: 16px;
    padding-bottom: 3em;
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

    .articles-aside,
    .article-titles-aside {
      position: sticky;
      top: 26px;
      max-height: calc(100vh - 26px);
      width: 150px;
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
    }
  }
}
</style>
