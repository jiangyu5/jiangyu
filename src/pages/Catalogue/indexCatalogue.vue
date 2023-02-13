<script setup>
import MainCatalogue from "./components/mainCatalogue.vue";
import IsLoading from "../../components/isLoading.vue";
</script>

<template>
  <Suspense>
    <MainCatalogue />
    <template #fallback>
      <IsLoading />
    </template>
  </Suspense>
</template>

<style scoped></style>
