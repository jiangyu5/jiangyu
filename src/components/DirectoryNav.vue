<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";

const route = useRoute();
const paths = computed(() => {
  let fullPath = decodeURIComponent(route.fullPath);
  let fullPaths = fullPath.slice(1).replace(".md", "").split("/");

  return fullPaths.map((e, index) => {
    return {
      link: e,
      url: "/" + fullPaths.slice(0, index + 1).join("/"),
    };
  });
});
</script>

<template>
  <div class="directory-nav">
    <router-link to="/">~</router-link>
    <template v-for="(link, index) in paths" :key="'d-n' + index">
      <span>/</span>
      <router-link :to="link.url" replace>{{ link.link }}</router-link>
    </template>
  </div>
</template>

<style scoped>
a {
  color: inherit;
  font-weight: 600;
}

span {
  font-weight: 600;
  margin: 0 6px;
}
</style>
