<script setup>
import Header from "./components/Header.vue";
import Footer from "./components/Footer.vue";
import DirectoryNav from "./components/DirectoryNav.vue";
</script>

<template>
  <Header></Header>
  <DirectoryNav></DirectoryNav>
  <main>
    <router-view></router-view>
  </main>
  <Footer></Footer>
</template>

<style>
#app {
  min-width: 320px;
  min-height: 100vh;
  display: grid;
  grid-template-rows: auto auto 1fr auto;
  color: var(--mid-6);
  background-color: var(--mid-0);
}

.directory-nav {
  position: sticky;
  top: 0;
  z-index: 9;
}

main {
  min-height: calc(100vh - 220px);
}

.directory-nav,
.footer {
  padding: 0 1rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--mid-4);
  border-top: 1px solid var(--mid-3);
  border-bottom: 1px solid var(--mid-3);
  background-color: var(--mid-2);
}
</style>
