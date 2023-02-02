import { createRouter, createWebHashHistory } from "vue-router";
import routes_nav from "./routes_nav";

const routes = [...routes_nav];

export default createRouter({
  history: createWebHashHistory(),
  mode: "hash",
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});
