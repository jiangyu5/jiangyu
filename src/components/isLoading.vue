<script setup></script>

<template>
  <div class="is-loading">
    <ul>
      <li v-for="i in 6"><span></span></li>
    </ul>
    <div class=""></div>
  </div>
</template>

<style scoped lang="less">
.is-loading {
  position: relative;
  width: 100%;
  height: 100%;
  ul {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
    li {
      display: inline-block;
      width: 0.7em;
      height: 0.7em;
      margin: 0 0.3em;
      border-radius: 50%;
      background-color: #a9c9ff55;
      animation: 1s jump ease infinite;

      &:nth-child(2) {
        background-color: #a9c9ff70;
        animation-delay: 0.15s;
      }
      &:nth-child(3) {
        background-color: #a9c9ff9c;
        animation-delay: 0.25s;
      }
      &:nth-child(4) {
        background-color: #a9c9ffb1;
        animation-delay: 0.35s;
      }
      &:nth-child(5) {
        background-color: #a9c9ffe5;
        animation-delay: 0.45s;
      }
      &:nth-child(6) {
        background-color: #a9c9ff;
        animation-delay: 0.5s;
      }
    }
  }
  @keyframes jump {
    0% {
      transform: translateY(0);
    }
    85% {
      transform: translateY(-1em);
    }
    100% {
      transform: translateY(0);
    }
  }
}
</style>
