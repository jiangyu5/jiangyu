<script setup></script>

<template>
  <div class="about">
    <div class="sentence sentence-0 font_bg">像这样空着......</div>
    <div class="sentence sentence-1 font_bg">
      我也<span class="jiangbu font_bg">不</span><span class="jiangku font_bg">想</span>
    </div>
    <div class="sentence-2 font_bg">
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
    line-height: 2em;
    color: #fff;
    padding: 0;
    text-shadow: 1px 1px 2px rgb(76, 76, 76);
  }

  .jiangbu {
    display: inline-block;
    color: #fff;
    animation: jiangbu 3s 2s linear forwards;
  }

  @keyframes jiangbu {
    0% {
      transform: rotateZ(0deg) scale(1) translateY(0);
    }
    20% {
      transform: rotateZ(45deg) scale(0.8) translateY(0);
    }

    50% {
      transform: rotateZ(200deg) scale(0.6) translateY(-0.5em);
    }

    80% {
      transform: rotateZ(180deg) scale(0.6) translateY(-0.5em);
      opacity: 1;
    }

    100% {
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

  .font_bg {
    background-image: linear-gradient(30deg, #73a6ff 0%, #ff95e1 100%);
    background-clip: text;
    -webkit-background-clip: text;
    color: transparent;
    text-shadow: unset;
    line-height: 1.5em;
  }
}
</style>
