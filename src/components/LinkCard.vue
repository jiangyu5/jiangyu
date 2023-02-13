<script setup>
import { ref, computed, onMounted, nextTick } from "vue";

const props = defineProps({
  title: {
    type: String,
    default: "链接卡片 长链接卡片标题测试 还不够长",
  },
  description: {
    type: String,
    default: "简单描述 slot",
  },
  href: {
    type: String,
    default: "#",
  },
});

const titleWidth = ref();
const LinkTitle = ref();
onMounted(() => {
  titleWidth.value = LinkTitle.value.offsetWidth;
});

const titleScroll = computed(() => {
  if (titleWidth.value && titleWidth.value > 154) {
    return {
      class: "title-scroll",
      style: { "animation-duration": titleWidth.value * 0.05 + "s" },
    };
  }

  return {
    class: "",
    style: "",
  };
});
</script>

<template>
  <router-link class="link-card" :to="props.href">
    <div class="link-card-decoration"></div>
    <div class="wrapper">
      <div class="link-card-title-container">
        <div
          class="link-card-title"
          :class="titleScroll.class"
          :style="titleScroll.style"
          ref="LinkTitle"
        >
          {{ props.title }}
        </div>
      </div>
      <div class="link-card-description">
        <slot>{{ props.description }}</slot>
      </div>
    </div>
  </router-link>
</template>

<style scoped lang="less">
@keyframes titleScroll {
  0% {
    transform: translateX(0);
  }
  6% {
    transform: translateX(0);
  }
  100% {
    transform: translateX(calc(-99%));
  }
}

.link-card {
  display: block;
  width: 180px;
  height: 66.22px;
  color: inherit;
  box-shadow: 2px 3px 6px var(--mid-3);
  border-radius: 8px;
  position: relative;
  transition: 0.3s;
  overflow: hidden;

  &:hover {
    box-shadow: -2px 2px 10px var(--alpha-2);

    .link-card-decoration {
      top: -6em;
      right: -10em;
      transform: rotateZ(50deg);
    }

    .title-scroll {
      white-space: nowrap;
      animation-name: titleScroll;
      animation-timing-function: linear;
      animation-iteration-count: infinite;
    }
  }

  .link-card-decoration {
    position: absolute;
    top: 1em;
    right: -14em;
    width: 27em;
    height: 30em;
    border-radius: 50%;
    background-color: var(--main-1);
    background-image: linear-gradient(
      30deg,
      var(--main-1) 0%,
      var(--main-4) 100%
    );
    transform: rotateZ(-90deg);
    transition: 0.4s;

    @keyframes infoRotate {
      0% {
        transform: rotateZ(-90deg);
      }
      100% {
        transform: rotateZ(0deg);
      }
    }
  }

  .wrapper {
    position: absolute;
    z-index: 1;
    padding: 0.8em;
    width: 180px;
  }
  .link-card-title-container {
    overflow: hidden;
    max-width: 195px;
    width: fit-content;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
  }

  .link-card-description {
    font-size: 0.8em;
    line-height: 1.3em;
    text-indent: 2em;
    overflow: hidden;
    text-overflow: ellipsis;
    -ms-text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: auto;
  }
}

.theme-dark .link-card .link-card-decoration {
  background-image: linear-gradient(to left, #909ec3, #a04eb098);
}
</style>
