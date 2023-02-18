import { computed, isRef } from "vue";
import { useRoute } from "vue-router";

import useAjax from "./useAjax";
import { marked } from "marked";

export default function () {
  const route = useRoute();

  // 文档链接
  const articleUrl = computed(() => {
    if (!route.path.includes("/notebook")) return "";
    if (route.path.includes(".")) {
      return route.path;
    }
    return route.path + "/index.md";
  });

  // 文档标题
  const articleTitle = computed(() => {
    let a = route.params.article;
    return a ? a.at(-1).replace(/\..+/, "") : route.path.substring(1);
  });

  // 获得文档
  const articleData = useAjax(articleUrl)["data"];
  const articleContent = computed(() => {
    if (articleData.value) return marked(articleData.value);
    return "";
  });

  // 左侧推荐链接
  const asideUrl = computed(() => {
    let a = route.params.article;
    if (!a) return "/data/notebook/index.json";
    a = a.at(-1).includes(".") ? a.slice(0, -1).join("/") : a.join("/");
    return "/data/notebook/" + a + "/index.json";
  });

  // 获得左侧显示的文档
  const asideData = useAjax(asideUrl)["data"];
  const aside = computed(() => {
    if (asideData.value) {
      return asideData.value["files"];
    }
    return null;
  });

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

  return {
    articleUrl,
    articleTitle,
    articleContent,
    asideUrl,
    aside,
    titles,
  };
}
