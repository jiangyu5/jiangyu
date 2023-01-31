<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const activeIndex = ref(0);
function setActive(index) {
  return activeIndex.value == index ? "active" : "";
}
function changeActive(index) {
  activeIndex.value = index;
}
// 获取 routes 作为 nav 的 Array
// 只获取作为根目录的 route，且 / 目录舍去
const defaultValue = (oneRoute) => oneRoute.path.split("/")[1].toUpperCase(); // 设置默认值
const routes = router.getRoutes().reduce((previousRoute, currentRoute) => {
  if (currentRoute.meta.nav) {
    previousRoute.push({
      path: currentRoute.path,
      name: currentRoute.name || defaultValue(currentRoute),
      title: currentRoute.meta.title || defaultValue(currentRoute),
    });
  }
  return previousRoute;
}, []);
</script>

<template>
  <div class="nav">
    <ul>
      <li v-for="(link, index) in routes">
        <router-link
          :to="link.path"
          :key="'nav' + index"
          :class="setActive(index)"
          @click="changeActive(index)"
          replace
          >{{ link.title }}</router-link
        >
      </li>
    </ul>
  </div>
</template>

<style scoped lang="less">
.nav {
  ul {
    li {
      display: inline-block;
      margin: 0 3px;

      a {
        // background-image: linear-gradient(30deg, #a9c9fffc 0%, #ffbbec 100%);
        // color: rgba(139, 153, 230, 0);
        // background-clip: text;
        // -webkit-background-clip: text;
        color: inherit;
        position: relative;
        display: block;
        font-weight: 600;
        border-radius: 3px;
        padding: 3px 7px;
        transition: 0.3s;

        // router-link 被选择时自动触发
        &.active {
          pointer-events: none;
          background-color: none;

          &::after {
            display: block;
            position: absolute;
            bottom: 0;
            left: 0;
            content: "";
            width: 100%;
            height: 2px;
            background-color: #a9c9ff94;
            background-image: linear-gradient(
              135deg,
              #a9c9fffc 0%,
              #ffbbec 100%
            );
            border-radius: 1px;
            animation: activeAni 0.6s forwards;
          }

          @keyframes activeAni {
            0% {
              transform: rotateZ(0);
            }
            15% {
              transform: rotateZ(10deg);
            }
            40% {
              transform: rotateZ(-5deg);
            }
            70% {
              transform: rotateZ(2.5deg);
            }
            100% {
              transform: rotateZ(0);
            }
          }
        }
      }
    }
  }
}
</style>
