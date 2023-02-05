<script setup>
import { ref, onMounted } from "vue";

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
    alert("输入为空，请重新输入！");
  }
}

const SearchInput = ref(null);
onMounted(() => {
  SearchInput.value.focus();
});
</script>

<template>
  <div class="search-input" :class="size">
    <input
      type="text"
      v-model="searchValue"
      @keyup.enter="searchToUrl"
      ref="SearchInput"
    />
    <div class="search-btn"></div>
  </div>
</template>

<style scoped lang="less">

.search-input {
  position: relative;
  width: 90%;
  max-width: 420px;
  margin: 0 auto;

  input {
    width: 100%;
    height: 2.6rem;
    font-size: 1rem;
    border-radius: 1.5em;
    border-color: var(--mid-4);
    color: var(--mid-5) !important;
    padding-left: 1.5em;
    padding-right: 3em;
    transition: all 0.2s;

    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(6px);
    -webkit-backdrop-filter: blur(6px);

    &:focus {
      box-shadow: 0 0 6px var(--alpha-5);
    }
  }

  .search-btn {
    width: calc(2.6rem - 2px);
    height: calc(2.6rem - 2px);
    position: absolute;
    right: 1px;
    top: 1px;
    background-color: var(--alpha-5);
    cursor: pointer;
    border-radius: 50%;
    transition: all 0.2s;

    &:hover {
      background-color: var(--alpha-2);
      &::before {
        border-color: #fff;
      }

      &::after {
        background-color: #fff;
      }
    }

    &::before,
    &::after {
      display: inline-block;
      content: "";
      border-radius: 50%;
      transition: all 0.2s;
    }

    &::before {
      width: 46%;
      height: 46%;
      border: 2px solid;
      border-color: var(--main-1);
      margin-top: 27.5%;
      margin-left: 9%;
    }
    &::after {
      width: 4px;
      height: 4px;
      background-color: var(--main-4);
    }
  }
}

@media screen and (min-width: 500px) {
  .search-input {
    input {
      font-size: 1.2rem;
      height: 3.2rem;
    }

    .search-btn {
      width: calc(3.2rem - 2px);
      height: calc(3.2rem - 2px);
    }
  }
}
</style>
