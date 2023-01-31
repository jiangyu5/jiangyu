## 安装

```shell
npm install vuex@next --save
```



## vuex/store.js

```js
import { createStore } from "vuex";
import card from "./modules/card";
import sites from "./modules/sites";

export default createStore({
  state: {},
  mutations: {},
  actions: {},
  getters: {},
  modules: {
    card,
    sites,
  },
});

```



### modules

```js
// card
export default {
  namespaced: true,
  state: {
    name: "jiang",
  },
  mutations: {
    rename(state, newName) {
      state.name = newName;
    },
  },
  actions: {},
  getters: {},
};

```

```js
// sites
export default {
  namespaced: true,
  state: {
    count: 0,
  },

  mutations: {
    increment(state, n) {
      state.count += n;
    },
  },
  actions: {
    check(context, n) {
      if (n >= 0) {
        context.commit("increment", n);
      }
    },
  },
  getters: {
    num() {
      return 2;
    },
    biger(state, getters) {
      return (state.count + getters.num) * 10;
    },
  },
};
```



## main.js

```js
import { createApp } from "vue";
import App from "./App.vue";
import sotre from "./vuex/store"; /* <== */

const app = createApp(App);
app.use(sotre); /* <== */
app.mount("#app");

```



## template

```vue
<template>
  <h2>state => count: {{ $store.state.sites.count }}</h2>
  <h2>state => name: {{ name }}</h2>
  <button @click="$store.commit('sites/increment', 1)">加 1</button>
</template>
```



## setup()

```vue
<script setup>
const { computed } = require("@vue/runtime-core");
const { useStore } = require("vuex");

const store = useStore();
    store.commit('card/rename', 'yu');
store.dispatch("sites/check", 5);
const name = computed(() => store.state.card.name);
</script>
```

