<script setup>
import { computed } from "vue";
import { useRoute } from "vue-router";
import useWinScroll from "../hook/useWinScrollYX";

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

const { scrollY } = useWinScroll();
const toTopisShow = computed(() => {
  return scrollY.value ? true : false;
});
function toTop() {
  window.scrollTo({
    top: 0,
    behavior: "smooth",
  });
}
</script>

<template>
  <div class="directory-nav">
    <router-link to="/">~</router-link>
    <template v-for="(link, index) in paths" :key="'d-n' + index">
      <span>/</span>
      <router-link :to="link.url" replace>{{ link.link }}</router-link>
    </template>
    <Transition name="to-top">
      <div class="to-top" v-show="toTopisShow" @click="toTop">Top</div>
    </Transition>
  </div>
</template>

<style scoped>
.to-top-enter-active {
  transition: all 0.3s ease-out;
}

.to-top-leave-active {
  transition: all 0.3s ease-in;
}

.to-top-enter-from,
.to-top-leave-to {
  transform: translateX(20px);
  opacity: 0;
}
a {
  color: inherit;
  font-weight: 600;
}

span {
  font-weight: 600;
  margin: 0 6px;
}

.to-top {
  float: right;
  cursor: pointer;
}
</style>
