<script setup>
import Nav from "./Nav.vue";
</script>

<template>
  <div class="header">
    <h1>张航的主页</h1>
    <!-- <SearchInput size="mini"></SearchInput> -->
    <Nav></Nav>
  </div>
</template>

<style scoped lang="less">
.header {
  padding: 6px 6px 3px 1em;
  h1 {
    font-size: 1.8em;
    line-height: 1.2em;
    background-color: #3333;
    background: url("../assets/bg_header.jpg") no-repeat center;
    background-clip: text;
    -webkit-background-clip: text;
    background-size: cover;
    color: rgba(139, 153, 230, 0);
    text-shadow: 0 3px 10px rgba(162, 173, 247, 0.2);
  }
  .nav {
    text-align: right;
  }
}

@media screen and (min-width: 500px) {
  .header {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: end;
  }
}
</style>
