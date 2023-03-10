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
  href: "",
  imgUrl: {
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

// 区分图片
const imgUrlMain = computed(() => {
  return typeof props.imgUrl == "string" ? props.imgUrl : props.imgUrl[0];
});

const imgUrlSub = computed(() => {
  return typeof props.imgUrl == "string" ? null : props.imgUrl[1];
});

// 介绍部分的动画效果
const cardTop = ref(0); // scroll 卷起部分
watch(cardTop, (top) => {
  let height = window.innerHeight;
  if (top > height || top <= -height / 2) return;
  let translateXValue = props.reverse
    ? -(top * 30) / height
    : (top * 30) / height;
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
      <div
        class="decoration"
        :class="decorationClass"
        :style="decorationStyle"
      ></div>
      <div class="left img">
        <div v-if="!imgUrlMain" :class="imgBg"></div>
        <img v-else :src="imgUrlMain" alt="图片" />
        <!-- <img v-if="imgUrlSub" class="img-sub" :src="imgUrlSub" /> -->
      </div>
      <div class="right introduction" :style="introductionStyle">
        <h5>{{ props.catologue }}</h5>
        <h2>{{ props.title }}</h2>
        <div>
          {{ props.introduction }}
        </div>
        <router-link v-if="props.url != '#'" :to="props.url">
          了解更多<span>→</span>
        </router-link>
        <a v-else-if="props.href" :href="props.href">作品地址<span>→</span></a>

        <div
          class="decoration"
          :class="decorationClass"
          :style="decorationStyle"
        ></div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
@marginBig: 3rem;
.introductory-card {
  background-color: var(--alpha-3);
  height: 100vh;
  max-width: 100%;
  overflow: hidden;
  padding-left: 0.5em;
  padding-right: 0.5em;
  display: flex;
  //   overflow: hidden;
  .container {
    position: relative;
    margin: auto;
    img {
      display: block;
      object-position: 30% bottom;
      object-fit: cover;
    }
    .img {
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);

      .imgBg,
      img {
        width: 300px;
        height: 200px;
        border-radius: 5px;
        background: var(--main-1);
        background-image: linear-gradient(
          30deg,
          var(--main-1) 0%,
          var(--main-4) 100%
        );
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
      box-shadow: inset 0px 0px 6px var(--alpha-4);
      border-radius: 6px;
      overflow: hidden;

      h5 {
        color: var(--main-12);
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
        background-color: #000;
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
    opacity: 0.5;
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
  background-color: #ffffff00;

  .container {
    .img {
      transform: translate(-50%, -50%);

      @media screen and (min-width: 667px) {
        transform: translate(-30%, -50%) !important;
      }
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

.theme-dark .introductory-card .container {
  .img {
    .img_bg_1 {
      background: -webkit-linear-gradient(
        90deg,
        rgb(127, 127, 213),
        rgb(134, 168, 231),
        rgb(145, 213, 234)
      );
      background: linear-gradient(
        90deg,
        rgb(142, 142, 182),
        rgb(157, 170, 193),
        rgb(92, 195, 168)
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
        rgb(210, 150, 161),
        rgb(221, 170, 141)
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
        rgb(182, 150, 207),
        rgb(140, 152, 176)
      );
    }
    .img_bg_4 {
      background: #0cebeb; /* fallback for old browsers */
      background: -webkit-linear-gradient(
        to left,
        rgb(93, 190, 190),
        rgb(108, 205, 181),
        rgb(116, 230, 200)
      );
      background: linear-gradient(
        to left,
        rgb(93, 190, 190),
        rgb(108, 205, 181),
        rgb(116, 230, 200)
      );
    }
  }

  .introduction {
    background: rgba(0, 0, 0, 0.1);
  }
}
.introductory-card {
  padding-left: 10%;
  padding-right: 10%;

  .container .img div {
    width: 80vw;
    height: 200px;
    border-radius: 10px;
  }
}
@media screen and (min-width: 667px) {
  .introductory-card .container .img {
    transform: translate(-70%, -50%);

    div {
      width: 50vw;
      height: 200px;
    }
  }
}

@media screen and (min-width: 760px) {
  .introductory-card {
    padding-left: 20%;
    padding-right: 20%;

    .container {
      .img {
        img {
          width: 550px;
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
          width: 40vw;
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
