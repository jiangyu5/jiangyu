<script setup>
import { ref, watch, onUnmounted } from "vue";
import SearchInput from "./SearchInput.vue";

const sentence = [
  {
    s1: "“如今我努力奔跑",
    s2: "不过是为了追上那个曾经被寄予厚望的自己。”",
  },
  {
    s1: "“不管发生什么事，都请安静且愉快地接受人生，",
    s2: "勇敢地、大胆地，而且永远地微笑着。”",
  },
  { s1: "“但愿每次回忆，", s2: "对生活都不感到负疚。”" },
  { s1: "“你只管努力，", s2: "剩下的交给时间。”" },
];

let sentence1 = "";
let sentence2 = "";
const sentenceAni1 = ref("");
const sentenceAni2 = ref("");
const sentenceAdd = ref(true);
let sentenceInterId = null;
watch(
  sentenceAdd,
  (v) => {
    clearInterval(sentenceInterId);
    if (v) {
      let _s = sentence[~~(Math.random() * sentence.length)];
      sentence1 = _s.s1;
      sentence2 = _s.s2;
      sentenceInterId = setInterval(sentenceAddFun, 200);
    } else {
      sentenceInterId = setInterval(sentenceDecFun, 100);
    }
  },
  { immediate: true }
);
function sentenceAddFun() {
  let lengthAni1 = sentenceAni1.value.length;
  let lengthAni2 = sentenceAni2.value.length;
  if (lengthAni1 < sentence1.length) {
    sentenceAni1.value += sentence1.at(lengthAni1);
  } else if (lengthAni2 < sentence2.length) {
    sentenceAni2.value += sentence2.at(lengthAni2);
  } else {
    sentenceAdd.value = false;
  }
}
function sentenceDecFun() {
  let lengthAni1 = sentenceAni1.value.length;
  let lengthAni2 = sentenceAni2.value.length;
  if (lengthAni2 > 0) {
    sentenceAni2.value = sentence2.substring(0, lengthAni2 - 1);
  } else if (lengthAni1 > 0) {
    sentenceAni1.value = sentence1.substring(0, lengthAni1 - 1);
  } else {
    sentenceAdd.value = true;
  }
}

function scrollView() {
  window.scrollTo({
    top: window.innerHeight,
    behavior: "smooth",
  });
}

onUnmounted(() => {
  clearInterval(sentenceInterId);
});
</script>

<template>
  <div class="home-top">
    <div class="wrapper">
      <div class="personal-signature">
        <p>{{ sentenceAni1 }}</p>
        <p>{{ sentenceAni2 }}</p>
      </div>
      <SearchInput />
    </div>
    <div class="down" @click="scrollView"><span></span></div>
  </div>
</template>

<style scoped lang="less">
.theme-dark .home-top {
  &::before {
    // background: -webkit-linear-gradient(to right, #a9c9ff, #ffbbec);
    // background: linear-gradient(to right, #a9c9ff2c, #ffbbec45);

    background: #757f9a; /* fallback for old browsers */
    background: -webkit-linear-gradient(
      to right,
      rgb(117, 127, 154),
      rgb(205, 210, 220)
    );
    background: linear-gradient(
      to right,
      rgb(117, 127, 154),
      rgb(205, 210, 220)
    );
  }
}
.home-top {
  min-height: calc(100vh - 99.51px);
  color: #fff;
  height: calc(100vh - 99.53px);
  padding: 60px 1em 1em;
  position: relative;
  overflow: hidden;

  &::before {
    display: block;
    content: "";
    position: absolute;
    left: -500px;
    bottom: 6em;
    width: 1130px;
    height: 1200px;
    border-radius: 50%;
    animation: ani 8s linear infinite;
    // background: var(--main-1);
    background: -webkit-linear-gradient(to right, var(--main-1), var(--main-8));
    background: linear-gradient(to right, var(--main-1), var(--main-8));
  }

  @keyframes ani {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .wrapper {
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    z-index: 1;
  }
  .personal-signature {
    font-size: 0.8em;
    line-height: 1.5em;
    height: 3em;
    letter-spacing: 0.05em;
    margin-bottom: 4em;

    p:last-child {
      text-indent: 3.2em;
    }
  }

  .search-input {
    text-align: center;
  }

  .down {
    position: absolute;
    margin: 0 auto;
    text-align: center;
    bottom: 64px;
    left: 50%;
    height: 40px;
    width: 50px;
    transform: translateX(-50%);
    color: var(--main-12);
    animation: downain 2s linear infinite;
    cursor: pointer;

    span {
      display: block;
      width: 16px;
      height: 16px;
      margin: 8px auto;
      border-left: 4px solid;
      border-bottom: 4px solid;
      border-radius: 3px;
      box-sizing: border-box;
      transform: rotateZ(-45deg);
    }
  }

  @keyframes downain {
    0% {
      bottom: 64px;
    }
    25% {
      bottom: 56px;
    }
    75% {
      bottom: 72px;
    }
    100% {
      bottom: 64px;
    }
  }
}

@media screen and (min-width: 500px) {
  .home-top {
    min-height: calc(100vh - 69.52px);
    padding: 4rem 3rem 4rem;

    &::before {
      left: -860px;
      bottom: 100px;
      width: 2160px;
      height: 2130px;
    }
    .personal-signature {
      font-size: 1em;
    }
  }
}

@media screen and (min-width: 870px) {
  .home-top {
    &::before {
      left: -1200px;
      bottom: 100px;
      width: 3160px;
      height: 3190px;
    }
  }
}
</style>
