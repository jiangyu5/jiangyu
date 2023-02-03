<script setup>
import { reactive, computed } from "vue";
import ajax from "../../hook/ajax";
import LinkCard from "../../components/LinkCard.vue";

const data = reactive({
  files: [],
  navActive: 0,
});

const showFiles = computed(() => {
  return data.files.length ? data.files[data.navActive]["files"] : null;
});

ajax("data/notebook/index.json").then((res) => {
  let jsonParse = JSON.parse(res);
  data.files = jsonParse["files"];
  data.count = jsonParse["count"];
});

function navActiveChange(index) {
  data.navActive = index;
}

function navActiveClass(index) {
  return { active: data.navActive == index };
}
</script>

<template>
  <div class="catalogue">
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
        <li v-for="article in showFiles">
          <link-card
            :title="article['name']"
            :href="article['path']"
          ></link-card>
        </li>
      </template>
    </ul>
  </div>
</template>

<style scoped lang="less">
.catalogue {
  text-align: left;
  .catalogue-nav {
    position: sticky;
    top: 26px;
    z-index: 9;
    background-color: white;
    padding-top: 1em;
    padding-bottom: 2px;

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
      border-bottom: 2px dashed #73a6ff;
      transition: all .5s;

      &:first-child {
        margin-left: 2em;
      }

      &:hover {
        cursor: pointer;
      }

      &.active {
        color: #73a6ff;
        cursor: default;
        border-color: #ffbbec;
      }

      span {
        display: block;
        position: absolute;
        left: 100%;
        bottom: 0;
        color: rgb(85, 142, 223);
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
