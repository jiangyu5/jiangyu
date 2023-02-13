<script setup>
import MainLinks from "./components/mainLinks.vue";
import IsLoading from "../../components/isLoading.vue";
</script>

<template>
  <Suspense>
    <MainLinks />
    <template #fallback>
      <IsLoading />
    </template>
  </Suspense>
</template>

<style scoped></style>
