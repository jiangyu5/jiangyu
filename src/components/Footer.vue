<script setup>
const linkList = [
  {
    link: "MDN",
    url: "https://developer.mozilla.org/zh-CN",
  },
  {
    link: "Vue",
    url: "https://cn.vuejs.org/",
  },
  {
    link: "PDF24",
    url: "https://tools.pdf24.org/zh/",
  },
  {
    link: "哔哩哔哩",
    url: "https://www.bilibili.com/",
  },
  {
    link: "陵游的小屋",
    url: "https://yustudy.cn",
  },
];
</script>

<template>
  <footer class="footer">
    <ul class="footer-nav">
      <li>首页</li>
      <li>关于我</li>
      <li>网站说明</li>
    </ul>
    <ul class="link-list">
      <li v-for="link in linkList">
        <a :href="link.url">{{ link.link }}</a>
      </li>
    </ul>
    <div class="basic">
      <div class="copyright">©2023 张航</div>
      <address>
        <a href="mailto:lingyou.ly@outlook.com">lingyou.ly@outlook.com</a><br />
      </address>
    </div>
  </footer>
</template>

<style scoped lang="less">
.footer {
  display: grid;
  grid-template-areas:
    "nav nav nav"
    "list list basic";
  color: rgb(128, 128, 128);
  font-size: 0.5em;
  line-height: 2.5em;
  padding-top: 0.5rem;
  padding-bottom: 1rem;
  .footer-nav {
    grid-area: nav;
    color: rgb(130, 137, 143);

    li {
      display: inline-block;

      &:nth-child(even) {
        margin: 0 10px;
      }
    }

    &::after {
      display: block;
      content: "";
      width: 100%;
      height: 1px;
      background-color: rgb(210, 210, 210);
      margin: 0.5rem 0;
    }
  }

  .link-list {
    grid-area: list;
  }

  .basic {
    grid-area: basic;
    text-align: center;
    place-self: end;
  }

  a {
    color: inherit;
    font-weight: inherit;
  }
}
</style>
