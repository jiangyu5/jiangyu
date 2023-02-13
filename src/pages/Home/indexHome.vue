<script setup>
import { defineAsyncComponent } from "vue";
import isLoading from "../../components/isLoading.vue";
import errorComponent from "../../components/errorComponent.vue";

const MainHome = defineAsyncComponent({
  loader: () => import("./components/mainHome.vue"),
  delay: 200,
  loadingComponent: isLoading,
  errorComponent: errorComponent,
  timeout: 30000,
});
</script>

<template>
  <MainHome />
</template>

<style scoped></style>
