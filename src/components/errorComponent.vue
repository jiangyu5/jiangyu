<script setup></script>

<template>
  <div class="error">
    <div>访问超时</div>
    <p>请检查您的网络</p>
    <p>或本站无该资源</p>
    <p>您也可以 <a href="mailto:lingyou.ly@outlook.com">向我发送邮件</a>。</p>
  </div>
</template>

<style scoped lang="less">
.error {
  text-align: center;
  padding: 60px;
  div {
    font-size: 1.5em;
    color: red;
    padding: 0.5em;
  }
  a {
    text-decoration: underline;
  }
}
</style>
