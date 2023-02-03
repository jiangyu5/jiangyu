<script setup>
import SearchInput from "../../../components/SearchInput.vue";

function scrollView() {
  window.scrollTo({
    top: window.innerHeight,
    behavior: "smooth",
  });
}
</script>

<template>
  <div class="home-top">
    <div class="personal-signature">
      <p>“多情自古空余恨，</p>
      <p>好梦由来最易醒。”</p>
    </div>
    <SearchInput />
    <div class="down" @click="scrollView"><span></span></div>
  </div>
</template>

<style scoped lang="less">
.home-top {
  min-height: calc(100vh - 99.51px);
  color: rgb(253, 253, 253);
  height: calc(100vh - 99.53px);

  background-attachment: fixed;
  background-size: cover;
  padding: 80px 1em 1em;
  position: relative;
  overflow: hidden;

  &::after {
    display: block;
    content: "";
    position: absolute;
    z-index: -9;
    left: -500px;
    bottom: 2em;
    width: 1130px;
    height: 1200px;
    border-radius: 50%;
    animation: ani 8s linear infinite;
    background: rgb(155, 195, 255);
    background: -webkit-linear-gradient(
      to right,
      rgb(155, 195, 255),
      rgb(138, 255, 171)
    );
    background: linear-gradient(
      to right,
      rgb(155, 195, 255),
      rgb(138, 255, 171)
    );
  }

  @keyframes ani {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }
  .personal-signature {
    font-size: 1em;
    line-height: 1.5em;
    font-weight: 600;
    letter-spacing: 0.05em;
    margin-bottom: 3em;

    p:last-child {
      text-indent: 3.2em;
    }
  }

  .search-input {
    text-align: center;
    color: #eee;
  }

  .down {
    position: absolute;
    margin: 0 auto;
    text-align: center;
    bottom: 40px;
    left: 50%;
    height: 40px;
    width: 50px;
    transform: translateX(-50%);
    color: rgb(255, 123, 75);
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
      bottom: 24px;
    }
    25% {
      bottom: 16px;
    }
    75% {
      bottom: 32px;
    }
    100% {
      bottom: 24px;
    }
  }
}

@media screen and (min-width: 500px) {
  .home-top {
    min-height: calc(100vh - 69.52px);
    padding: 2rem 3rem 4rem;

    &::after {
      left: -860px;
      bottom: 100px;
      width: 2160px;
      height: 2130px;
    }
    .personal-signature {
      font-size: 1.6em;
    }
  }
}

@media screen and (min-width: 870px) {
  .home-top {
    &::after {
      left: -1200px;
      bottom: 100px;
      width: 3160px;
      height: 3190px;
    }
  }
}
</style>
