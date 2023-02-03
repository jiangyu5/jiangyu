<script setup>
import { ref } from "vue";
import router from "../router/router";

const searchValue = ref("");
const props = defineProps({
  size: {
    type: String,
    default: "normal",
  },
});

function searchToUrl() {
  let value = searchValue.value.trim();
  if (value) {
    window.open(`https://cn.bing.com/search?q=${value}`, "_blank");
  } else {
    alert('输入为空，请重新输入！')
  }

}
</script>

<template>
  <div class="search-input" :class="size">
    <input type="text" v-model="searchValue" @keyup.enter="searchToUrl" />
  </div>
</template>

<style scoped lang="less">
.search-input {
  input {
    max-width: 320px;
    width: 50%;
    height: 2.6rem;
    font-size: 1rem;
    color: inherit;
    border-color: white;
    border-radius: 1.5em;
    padding-left: 1.5em;
    padding-right: 1.5em;

    &:focus {
      box-shadow: 0 0 6px rgba(192, 192, 192, 0.25);
    }
  }
}

div.mini-search-input {
  input {
    width: 50px;
    height: 2em;
    font-size: 0.8em;
    color: inherit;
    border-color: silver;
    padding: 3px 1em;
    transition: width 0.2s;
    display: block;
    margin-bottom: 2px;

    &:focus {
      width: 120px;
      border-color: rgb(54, 132, 242);
      outline: 3px solid rgba(8, 217, 244, 0.1);
    }
  }
}
</style>
