<script setup>
import { reactive, computed } from "vue";
import ajax from "../../hook/ajax";
import LinkCard from "../../components/LinkCard.vue";
import { ref } from "vue";

const data = reactive({
  files: [],
  navActive: 0,
  ctime: "",
  mtime: "",
  atime: "",
  description: "",
});

const showFiles = computed(() => {
  return data.files.length ? data.files[data.navActive]["files"] : null;
});

ajax("data/notebook/index.json").then((res) => {
  let jsonParse = JSON.parse(res);
  data.files = jsonParse["files"];
  data.count = jsonParse["count"];
});

const Catalogue = ref(null);
function navActiveChange(index) {
  data.navActive = index;

  if (document.documentElement.scrollTop > 20) {
    Catalogue.value.scrollIntoView({
      block: "start",
      behavior: "smooth",
    });
  }
}

function navActiveClass(index) {
  return { active: data.navActive == index };
}
</script>

<template>
  <div class="catalogue" ref="Catalogue">
    <ul class="catalogue-nav">
      <li
        v-for="(catalogue, index) in data.files"
        @click="navActiveChange(index)"
        :class="navActiveClass(index)"
      >
        {{ catalogue.name }}<span>{{ catalogue.count }}</span>
      </li>
    </ul>
    <ul class="article-list">
      <template v-if="showFiles">
        <li v-for="article in showFiles" :key="article['name']">
          <link-card :title="article['name']" :href="article['path']">
            <ul class="link-info" style="text-align: right">
              <li>{{ article["mtime"].slice(2) }}</li>
            </ul>
          </link-card>
        </li>
      </template>
    </ul>
  </div>
</template>

<style scoped lang="less">
.catalogue {
  text-align: left;
  padding-top: 0.5em;
  height: 100%;
  .catalogue-nav {
    position: sticky;
    top: 26px;
    z-index: 9;
    background-color: var(--mid-0);
    padding-top: 0.5em;

    li {
      display: inline-block;
      width: fit-content;
      line-height: 1em;
      box-sizing: border-box;
      position: relative;
      padding: 5px 6px;
      margin: 0 0.8em;
      background-color: #a9c9fffc;
      background-image: linear-gradient(30deg, #73a6ff 0%, #ff95e1 100%);
      background-clip: text;
      -webkit-background-clip: text;
      color: transparent;
      border-bottom: 2px dashed rgba(0, 0, 0, 0);
      transition: all 0.2s;

      &:first-child {
        margin-left: 2em;
      }

      &:hover {
        cursor: pointer;
      }

      &.active {
        color: var(--main-3);
        border-color: var(--main-3);
        cursor: default;
      }

      span {
        display: block;
        position: absolute;
        left: 100%;
        bottom: 0;
        color: var(--main-3);
        font-size: 0.5em;

        height: 2em;
        line-height: 2em;
        box-sizing: border-box;
        padding-left: 1px;
        padding-right: 2px;
      }
    }
  }

  .article-list {
    display: flex;
    gap: 6px;
    flex-flow: row wrap;
    padding: 1em 1.5em 3em;
  }
}
</style>
