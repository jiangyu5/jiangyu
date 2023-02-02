export default [
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
    path: "/notebook",
    name: "Notebook",
    component: () => import("../pages/Article/indexArticle.vue"),
    meta: {
        title: '笔记本',
        nav: true
    },
    children: [
      {
        path: ":catalogue(.*)",
        component: () => import("../pages/Article/indexArticle.vue"),
      },
    ],
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
    component: () => import("../pages/About/indexAbout.vue"),
    meta: {
      title: "关于",
      nav: true,
    },
  },
];
