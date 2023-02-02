<script setup>
import { ref, reactive, computed, onMounted, watch } from "vue";
import { useRoute, useRouter } from "vue-router";

const router = useRouter();
const route = useRoute();
const navData = reactive({
  navs_offset: [],
  active_index: 0,
});

const navBarStyle = computed(() => {
  return navData.navs_offset[navData.active_index];
});

// 路由变化，navData['active_index'] 也变化
watch(
  () => route.path,
  (to) => {
    for (let i in routes) {
      if (to == routes[i].path) {
        navData.active_index = i;
        break;
      }
    }
  }
);

// 从 router 中获得 nav 数
// 作为 nav 的路由 meta.nav = true
const routes = router.getRoutes().reduce((previousRoute, currentRoute) => {
  if (currentRoute.meta.nav) {
    previousRoute.push({
      path: currentRoute.path,
      name: currentRoute.name,
      title: currentRoute.meta.title,
    });
  }
  return previousRoute;
}, []);

// 获得 nav 元素距离，放入 navData['navs_offset']
const Nav = ref();
onMounted(() => {
  for (let e of Nav.value) {
    navData.navs_offset.push({
      left: e.offsetLeft + "px",
      width: e.offsetWidth + "px",
    });
  }
});
</script>

<template>
  <div class="nav">
    <div class="active-bar" :style="navBarStyle"></div>
    <ul>
      <li v-for="(link, index) in routes" ref="Nav">
        <router-link :to="link.path" :key="'nav' + index" replace>{{
          link.title
        }}</router-link>
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.nav {
  position: relative;
  overflow: hidden;
  .active-bar {
    position: absolute;
    bottom: 1px;
    left: -3px;
    transition: left 0.3s, opacity 0.2s;
    width: 45.97px;
    height: 3px;
    background-color: #a9c9ff94;
    background-image: linear-gradient(135deg, #a9c9fffc 0%, #ffbbec 100%);
    border-radius: 1.5px;
  }

  ul {
    li {
      display: inline-block;
      margin: 0 3px;

      a {
        color: inherit;
        position: relative;
        display: block;
        font-weight: 600;
        border-radius: 3px;
        padding: 3px 7px;
        transition: 0.3s;

        // router-link 被选择时自动触发
        &.router-link-active {
          pointer-events: none;
          background-color: none;
        }
      }
    }
  }
}
</style>
