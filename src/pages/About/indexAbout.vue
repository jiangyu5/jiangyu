<script setup></script>

<template>
  <div class="about">
    <div class="sentence sentence-0">像这样空着......</div>
    <div class="sentence sentence-1">
      我也<span class="jiangbu">不</span><span class="jiangku">想</span>
    </div>
    <div class="sentence-2">
      <p>完善中</p>
      <p>这一页会不一样</p>
    </div>
  </div>
</template>

<style scoped lang="less">
.about {
  min-height: calc(100% - 69.52px);
  display: flex;
  flex-flow: column nowrap;
  justify-content: center;
  align-items: center;
  gap: 3em;

  .sentence-0 {
    margin-right: 30%;
  }

  .sentence {
    font-size: 2rem;
    color: #fff;
    text-shadow: 3px 3px 3px rgb(136, 136, 136);
  }

  .sentence-2 {
    align-self: end;
    text-align: right;
    margin-right: 10%;
    color: #fff;
    line-height: 2em;
    padding: 0;
    text-shadow: 1px 1px 2px rgb(76, 76, 76);
  }

  .small {
    display: inline-block;
    transform: scale(0.8);
  }
  .rotate-200 {
    display: inline-block;
    transform: rotateZ(200deg);
  }

  .jiangbu {
    display: inline-block;
    color: #fff;
    animation: jiangbu 3s 3s linear forwards;
  }

  @keyframes jiangbu {
    0% {
      transform: rotateZ(0deg) scale(1) translateY(0);
    }
    20% {
      transform: rotateZ(45deg) scale(0.8) translateY(0);
    }

    50% {
      color: black;
      transform: rotateZ(200deg) scale(0.6) translateY(-0.5em);
    }

    80% {
      color: black;
      transform: rotateZ(180deg) scale(0.6) translateY(-0.5em);
      opacity: 1;
    }

    100% {
      color: black;
      transform: rotateZ(180deg) scale(0.6) translateY(-10em);
      opacity: 0;
    }
  }

  .jiangku {
    display: inline-block;
    transform: translateX(0) rotateZ(0deg) scale(1);
    animation: jiangku 3.6s 3s linear forwards;
  }

  @keyframes jiangku {
    0% {
      transform: translateX(0) rotateZ(0deg) scale(1);
    }

    30% {
      transform: translateX(0) rotateZ(0deg) scale(0.6);
    }

    70% {
      transform: translateX(200%) rotateZ(360deg) scale(0.6);
    }

    95% {
      transform: translateX(-100%) rotateZ(0deg) scale(0.9);
    }

    100% {
      transform: translateX(-100%) rotateZ(0deg) scale(1);
    }
  }

  .black {
    color: black;
  }

  .tomato {
    color: tomato;
  }
}
</style>
