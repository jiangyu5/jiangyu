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
    line-height: 1.4em;
    // background-color: var(--main-1);
    // background: url("../assets/bg_header.jpg") no-repeat center;
    // background-clip: text;
    // -webkit-background-clip: text;
    // background-size: cover;
    // color: rgba(0, 0, 0, 0);
    color: var(--mid-6);
  }
  .nav {
    text-align: right;
  }
}

@media screen and (min-width: 550px) {
  .header {
    display: grid;
    grid-template-columns: 1fr auto;
    align-items: end;
  }
}
</style>
