<script setup>
import { watch, ref, computed, reactive, onMounted, onUnmounted } from "vue";

const props = defineProps({
  catologue: {
    type: String,
    default: "",
  },
  title: {
    type: String,
    default: "标题",
  },
  introduction: {
    type: String,
    default: "测试文本".repeat(1),
  },
  url: { type: String, default: "#" },
  imgUrl: {
    type: String,
    default: "",
  },
  reverse: {
    type: Boolean,
    default: false,
  },
  num: {
    type: Number,
    default: 0,
  },
});

const introductionStyle = reactive({
  transform: "",
});
const decorationStyle = reactive({
  transform: "",
});
const decorationClass = computed(() => {
  const decoration = [
    "decoration-rectangle",
    "decoration-triangle",
    "decoration-circle",
    "decoration-irregular",
  ]; // 保持偶数项，否则，因为图形不对称，reserver 难看，待修改

  let length = decoration.length;
  if (props.num < length) return decoration[props.num];
  return decoration[props.num % length];
});
// 未传入图片时的背景
const imgBg = computed(() => {
  const decoration = ["img_bg_1", "img_bg_2", "img_bg_3", "img_bg_4"]; // 保持偶数项，否则，因为图形不对称，reserver 难看，待修改

  let length = decoration.length;
  if (props.num < length) return decoration[props.num];
  return decoration[props.num % length];
});

// 介绍部分的动画效果
const cardTop = ref(0); // scroll 卷起部分
watch(cardTop, (top) => {
  let height = window.innerHeight;
  if (top >= height / 2 || top <= -height) return;
  let translateXValue = (top * 25) / height;
  if (props.reverse) translateXValue *= -1;
  introductionStyle.transform = `translateX(${translateXValue}%)`;
});

const Card = ref(null);
function cardTopListener() {
  cardTop.value = Card.value.getBoundingClientRect().top;
}
onMounted(() => {
  window.addEventListener("scroll", cardTopListener);
});
onUnmounted(() => {
  window.removeEventListener("scroll", cardTopListener);
});
</script>

<template>
  <div class="introductory-card" :class="{ reverse: reverse }" ref="Card">
    <div class="container">
      <div class="left img">
        <div v-if="!imgUrl" :class="imgBg"></div>
        <img v-else :src="imgUrl" alt="图片" />
      </div>
      <div class="right introduction" :style="introductionStyle">
        <h5>{{ props.catologue }}</h5>
        <h2>{{ props.title }}</h2>
        <div>
          {{ props.introduction }}
        </div>
        <router-link :to="props.url"> 了解更多<span>→</span> </router-link>
        <div
          class="decoration"
          :class="decorationClass"
          :style="decorationStyle"
        ></div>
      </div>
      <div
        class="decoration"
        :class="decorationClass"
        :style="decorationStyle"
      ></div>
    </div>
  </div>
</template>

<style scoped lang="less">
@marginBig: 3rem;
.introductory-card {
  height: 100vh;
  max-width: 100%;
  overflow: hidden;
  padding-left: 0.5em;
  padding-right: 0.5em;
  display: flex;
  overflow: hidden;
  .container {
    background-color: rgba(192, 192, 192, 0);
    position: relative;
    margin: auto;
    .img {
      position: absolute;
      top: 0;
      left: 0;
      z-index: -1;
      min-height: 200px;

      div,
      img {
        width: 260px;
        height: 200px;
        border-radius: 5px;
        background-image: linear-gradient(30deg, #73a6ff 0%, #ff95e1 100%);

        background: #7f7fd5; /* fallback for old browsers */
      }

      .img_bg_1 {
        background: -webkit-linear-gradient(
          90deg,
          rgb(127, 127, 213),
          rgb(134, 168, 231),
          rgb(145, 213, 234)
        );
        background: linear-gradient(
          90deg,
          rgb(127, 127, 213),
          rgb(134, 168, 231),
          rgb(145, 213, 234)
        );
      }

      .img_bg_2 {
        background: #ffafbd; /* fallback for old browsers */
        background: -webkit-linear-gradient(
          to left,
          rgb(255, 175, 189),
          rgb(255, 195, 160)
        );
        background: linear-gradient(
          to left,
          rgb(255, 175, 189),
          rgb(255, 195, 160)
        );
      }

      .img_bg_3 {
        background: #b993d6; /* fallback for old browsers */
        background: -webkit-linear-gradient(
          to left,
          rgb(221, 181, 251),
          rgb(165, 190, 240)
        );
        background: linear-gradient(
          to left,
          rgb(221, 181, 251),
          rgb(165, 190, 240)
        );
      }
      .img_bg_4 {
        background: #0cebeb; /* fallback for old browsers */
        background: -webkit-linear-gradient(
          to left top,
          rgb(12, 235, 235),
          rgb(32, 227, 178),
          rgb(41, 255, 198)
        );
        background: linear-gradient(
          to left top,
          rgb(12, 235, 235),
          rgb(32, 227, 178),
          rgb(41, 255, 198)
        );
      }

      img {
        display: block;
        object-position: 30% bottom;
        object-fit: cover;
      }
    }

    .introduction {
      min-width: calc(200px + @marginBig);
      display: grid;
      grid-template-rows: auto auto 1fr auto;
      text-align: left;
      padding: 0.5em 1.5em 1.5em;
      margin: @marginBig 0 0 @marginBig;
      background: rgba(255, 255, 255, 0.5);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      box-shadow: inset 0px 0px 6px rgba(217, 217, 217, 0.7);
      border-radius: 6px;
      overflow: hidden;

      h5 {
        color: rgb(255, 86, 56);
      }

      h5,
      h2 {
        line-height: 2em;
        margin: 0;
      }

      div {
        text-indent: 2em;
      }

      a {
        display: block;
        width: fit-content;
        font-size: 0.8em;
        font-weight: 600;
        color: #fff;
        background-color: rgba(51, 51, 51, 0.9);
        border-radius: 5px;
        padding: 0.3em 0.6em;
        margin-top: 1.5em;

        span {
          display: inline-block;
          font-weight: 700;
          transform: scale(0.8, 1.5);
          padding-left: 0.5em;
        }
      }
    }
  }
  .decoration {
    position: absolute;
    height: 80vh;
    width: 60vw;
    bottom: -40vh;
    right: -50vw;
    opacity: 0.3;
    z-index: -9;
  }
  .decoration-triangle {
    border-top: 50vh solid rgba(0, 0, 0, 0);
    border-bottom: 30vh solid rgba(0, 0, 0, 0);
    border-left: 80vw solid tomato;
  }

  .decoration-circle {
    border-radius: 50%;
    background-color: rgb(159, 62, 204);
    transform: rotateZ(60deg);
  }

  .decoration-rectangle {
    background-color: rgb(49, 210, 197);
    height: 100vh;
    width: 30vw;
    right: -20vw;
    transform: rotateZ(45deg);
  }

  .decoration-irregular {
    border-top: 40vh solid;
    border-bottom: 60vh solid;
    border-left: 50vw solid;
    border-color: rgb(21, 229, 156);
    border-right: 20vw solid rgba(0, 0, 0, 0);
    // transform: rotate3d(1, 1, 1, 45deg);
  }
}
.reverse {
  background-color: rgba(192, 192, 192, 0.15);
  .container {
    .img {
      left: auto;
      right: 0.5rem;
    }

    .introduction {
      margin: @marginBig @marginBig 0 0;
    }
  }

  .decoration {
    right: unset;
    left: -50vw;
  }
}

@media screen and (min-width: 667px) {
  .introductory-card {
    padding-left: 10%;
    padding-right: 10%;
  }
}

@media screen and (min-width: 760px) {
  .introductory-card {
    padding-left: 20%;
    padding-right: 20%;

    .container {
      .img {
        div,
        img {
          width: 400px;
          height: 300px;
          border-radius: 10px;
        }
      }

      .introduction {
        min-width: calc(400px + @marginBig);
        border-radius: 10px;
      }
    }
  }
}

@media screen and (min-width: 1024px) {
  @marginTop: 10vh;
  @marginLeft: 10vw;
  .introductory-card {
    .container {
      .img {
        div,
        img {
          width: 40vwpx;
          height: 40vh;
          border-radius: 10px;
        }
      }

      .introduction {
        min-width: calc(40vw + @marginBig);
        border-radius: 10px;
        margin: @marginTop 0 0 @marginLeft;
      }
    }
  }

  .reverse {
    .container {
      .introduction {
        margin: @marginTop @marginLeft 0 0;
      }
    }
  }
}
</style>
