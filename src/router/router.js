import { createRouter, createWebHashHistory } from "vue-router";

const routes = [
  { path: "/", redirect: "/home" },
  {
    path: "/home",
    name: "Home",
    component: () => import("../pages/Home/indexHome.vue"),
    meta: {
      title: "首页",
      nav: true,
    },
  },
  {
    path: "/catalogue",
    name: "Catalogue",
    component: () => import("../pages/Catalogue/indexCatalogue.vue"),
    meta: {
      title: "分类",
      nav: true,
    },
  },
  {
    path: "/links",
    name: "Link",
    component: () => import("../pages/Links/indexLinks.vue"),
    meta: {
      title: "链接",
      nav: true,
    },
  },
  {
    path: "/about",
    name: "About",
    redirect: "/notebook/关于",
    meta: {
      title: "关于",
      nav: true,
    },
  },
  {
    path: "/notebook",
    name: "Notebook",
    component: () => import("../pages/Article/indexArticle.vue"),
    children: [
      {
        path: ":catalogue(.*)",
        component: () => import("../pages/Article/indexArticle.vue"),
      },
    ],
  },
];

export default createRouter({
  history: createWebHashHistory(),
  mode: "hash",
  routes,
  scrollBehavior() {
    return { top: 0 };
  },
});
