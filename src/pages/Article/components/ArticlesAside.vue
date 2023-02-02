<script setup>
const props = defineProps({
  data: {
    type: Object,
    default: [],
  },
});
</script>

<template>
  <div class="articles-aside">
    <h3>相关笔记</h3>
    <ul>
      <li v-for="i in props.data">
        <router-link :to="i.path">{{ i.name }}</router-link>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.articles-aside {

  h3 {
    font-weight: 600;
    font-size: 1.5em;
    margin-bottom: 0.5em;
  }

  ul {
    li {
      a {
        display: block;
        color: inherit;
        font-size: 0.9em;
        line-height: 2.3em;
        white-space: nowrap;
        padding: 0 .5em;
        transition: 0.3s;
        border-left: 3px solid transparent;

        &:hover {
          color: #397cee;
        }
      }

      .router-link-active {
        border-left-color: #397cee;
        background-color: #ffbbec52;
        pointer-events: none;
      }
    }
  }
}
</style>
