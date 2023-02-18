<script setup>
import { ref, watch, nextTick } from "vue";

const props = defineProps({
  titles: {
    type: Object,
    default: [],
  },
  titleIndex: {
    type: Number,
    default: 0,
  },
});

const emits = defineEmits(["changeTitleIndex"]);
function gotoAnchor(index) {
  emits("changeTitleIndex", index);
}

function activeClass(index) {
  return props.titleIndex != index ? "" : "active";
}

// 矫正标题的位置
const UL = ref(null);
const CONTAINER = ref(null);
const titleDoms = [];
watch(
  () => props.titles,
  () => {
    titleDoms.length = 0;
    if (!UL.value) return;
    nextTick(() => {
      [...UL.value.children].forEach((el) => titleDoms.push(el));
    });
  }
);

watch(
  () => props.titleIndex,
  (index) => {
    if (!index || !titleDoms) return;
    let clientHeight = CONTAINER.value.clientHeight;
    if (
      clientHeight + CONTAINER.value.scrollTop ===
      CONTAINER.value.scrollHeight
    )
      return;
    CONTAINER.value.scrollTo({
      top: titleDoms[index].offsetTop - clientHeight / 3,
      behavior: "smooth",
    });
  }
);
</script>

<template>
  <div class="article-titles-aside" ref="CONTAINER">
    <div class="article-catalog-header">目录</div>
    <ul ref="UL">
      <li
        v-for="(title, index) in props.titles"
        :class="[title.h, activeClass(index)]"
        @click="gotoAnchor(index)"
      >
        {{ title.title }}
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.article-titles-aside {
  font-size: 0.9em;
  position: relative;
  .article-catalog-header {
    font-weight: 600;
    font-size: 1.5em;
    margin-bottom: 0.5em;
  }

  ul {
    // max-width: 150px;
    overflow-y: auto;

    li {
      font-weight: normal;
      line-height: 2em;
      border-left: 3px solid rgba(210, 210, 210, 0);
      padding: 0 1em;
      cursor: pointer;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;

      &.active {
        border-left-color: #397cee;
        background-color: #ffbbec52;
        pointer-events: none;
      }

      :hover {
        color: #397cee;
      }
    }

    .h2 {
      padding-left: 1em;
    }
    .h3 {
      padding-left: 2em;
    }
    .h4 {
      padding-left: 3em;
    }
    .h5 {
      padding-left: 4em;
    }
    .h6 {
      padding-left: 5em;
    }
  }
}
</style>
