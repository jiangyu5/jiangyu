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
  color: rgb(253, 253, 253);
  min-height: calc(100vh - 99.53px);
  background: url("../../../assets/bg_header.jpg") no-repeat center;
  background-attachment: fixed;
  background-size: cover;
  padding: 80px 1em 1em;
  position: relative;
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
    .personal-signature {
      font-size: 1.5em;
    }
  }
}
</style>
