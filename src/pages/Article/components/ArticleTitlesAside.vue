<script setup>
const props = defineProps({
  titles: {
    type: Object,
    default: [],
  },
  activeTitleIndex: {
    type: Number,
    default: 0,
  },
});

const emits = defineEmits(["returnTitleIndex"]);
function gotoAnchor(index) {
  emits("returnTitleIndex", index);
}
</script>

<template>
  <div class="article-titles-aside">
    <div class="article-catalog-header">目录</div>
    <ul>
      <li
        v-for="(title, index) in props.titles"
        :class="[title.h, { active: activeTitleIndex == index }]"
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
  .article-catalog-header {
    font-weight: 600;
    font-size: 1.5em;
    margin-bottom: .5em;
  }

  ul {
    // max-width: 150px;
    overflow: auto;

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
