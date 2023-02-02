<script setup>
import { ref, computed, onMounted } from "vue";


const props = defineProps({
  title: {
    type: String,
    default: "链接卡片 长链接卡片标题测试 还不够长",
  },
  description: {
    type: String,
    default: "链接卡片的简单描述",
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
  if (titleWidth.value && titleWidth.value > 195) {
    return {
      class: "title-scroll",
      style: { "animation-duration": titleWidth.value * 0.04 + "s" },
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
    <div class="link-card-description">{{ props.description }}</div>
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
    transform: translateX(calc(-100% - 5em));
  }
}
.link-card {
  margin: 0.5em;
  display: block;
  width: 180px;
  color: inherit;
  box-shadow: 2px 3px 6px rgba(84, 84, 84, 0.3);
  border-radius: 8px;
  position: relative;
  transition: 0.3s;
  padding: 0.8em;
  overflow: hidden;

  &:hover {
    // transform: scale(1.05);
    box-shadow: -2px 2px 10px rgba(113, 178, 253, 0.401);

    .link-card-decoration {
      top: -6em;
      right: -10em;
      transform: rotateZ(50deg);
    //   animation: 5s infoRotate linear infinite;
    }

    .title-scroll {
      white-space: nowrap;
      animation: titleScroll linear infinite;
    }
  }

  .link-card-decoration {
    position: absolute;
    z-index: -9;
    top: 2em;
    right: -16em;
    width: 27em;
    height: 30em;
    border-radius: 50%;
    background-color: #a9c9ff;
    background-image: linear-gradient(30deg, #a9c9fffc 0%, #ffbbec 100%);
    transform: rotateZ(-90deg);
    transition: 0.4s;

    @keyframes infoRotate {
      0% {
        transform: rotateZ(-90deg);
      }
      100% {
        transform: rotateZ(270deg);
      }
    }
  }

  .link-card-title-container {
    overflow: hidden;
    width: 195px;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1;
  }

  .link-card-description {
    height: 3em;
    font-size: 0.8em;
    text-indent: 2em;
    overflow: hidden;
    text-overflow: ellipsis;
    -ms-text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 2;
  }
}
</style>
