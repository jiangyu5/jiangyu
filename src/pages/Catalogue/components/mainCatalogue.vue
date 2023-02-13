<script setup>
import LinkCard from "../../../components/LinkCard.vue";
import { ref, computed } from "vue";

const data = await fetch("data/notebook/index.json").then((res) => res.json());
const navActive = ref(0);

const showFiles = computed(() => {
  return data["files"][navActive.value].files;
});

const Catalogue = ref(null);
function navActiveChange(index) {
  navActive.value = index;

  if (document.documentElement.scrollTop > 20) {
    Catalogue.value.scrollIntoView({
      block: "start",
      behavior: "smooth",
    });
  }
}

function navActiveClass(index) {
  return { active: navActive.value == index };
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
      <li v-for="article in showFiles" :key="article['name']">
        <link-card :title="article['name']" :href="article['path']">
          <ul class="link-info" style="text-align: right">
            <li>{{ article["mtime"].slice(2) }}</li>
          </ul>
        </link-card>
      </li>
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
        margin-left: 1em;
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
    gap: 10px;
    flex-flow: row wrap;
    padding: 1em 1em 3em;
  }
}
</style>
