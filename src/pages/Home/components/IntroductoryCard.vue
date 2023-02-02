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
});

const introductionStyle = reactive({
  transform: 0,
});
const cardTop = ref(0);

watch(cardTop, (top) => {
  let height = window.innerHeight;
  if (top > height / 2 || top < -(height / 4)) return;
  introductionStyle.transform = `translateX(${(30 * top) / (height / 2)}%)`;
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
        <div v-if="!imgUrl"></div>
        <img v-else :src="imgUrl" alt="图片" />
      </div>
      <div class="right introduction" :style="introductionStyle">
        <h5>{{ props.catologue }}</h5>
        <h2>{{ props.title }}</h2>
        <div>
          {{ props.introduction }}
        </div>
        <router-link :to="props.url"> 了解更多<span>→</span> </router-link>
      </div>
    </div>
  </div>
</template>

<style scoped lang="less">
@marginBig: 3rem;
.introductory-card {
  height: 100vh;
  padding-top: 26px;
  padding-left: 0.5em;
  padding-right: 0.5em;
  display: flex;
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
        //   box-shadow: 0 0 16px rgba(81, 81, 81, 0.7);
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
      min-height: 300px;
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
      min-height: 40vh;
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
