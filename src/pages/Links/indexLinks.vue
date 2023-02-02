<script setup>
import ajax from "../../hook/ajax";
import { ref } from "vue";

const data = ref([]);
ajax("/data/links/links.json").then((res) => {
  data.value = JSON.parse(res);
});
</script>

<template>
  <div class="links">
    <div class="links-wrapper" v-for="obj in data">
      <h3>{{ obj.catologue }}</h3>
      <ul>
        <li v-for="link in obj.links">
          <a :href="link.url" target="_blank">{{ link.link }}</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped lang="less">
.links {
  display: flex;
  flex-flow: row wrap;
  justify-items: center;
  gap: 2em;
  padding: 2em;

  .links-wrapper {
    min-width: 150px;
    display: flex;
    flex-flow: column nowrap;

    h3 {
      line-height: 2em;
      padding-left: 0.5em;
      background-color: #a9c9ff94;
      background-image: linear-gradient(135deg, #a9c9ff92 0%, #ffbbec92 100%);
      color: #fff;
      text-shadow: 1px 1px 0 rgb(81, 81, 81);
      box-shadow: 1px 2px 10px #c0c0c06d;
      border-radius: 6px;
    }

    ul {
      margin-top: 5px;
      flex: 1 auto;
      padding: 0.5em 16px 0.6em;
      box-shadow: 1px 2px 10px #c0c0c06d;
      border-radius: 6px;


      li {
        &:hover {
          a {
            transform: translateX(5px);
            // padding-left: 1em;
            background-color: #a9c9ff94;
            background-image: linear-gradient(
              135deg,
              #a9c9ff92 0%,
              #ffbbec92 100%
            );
          }
        }
        a {
          display: block;
          padding: 3px;
          font-size: 0.9em;
          color: inherit;
          border-bottom: 1px solid;
          border-image: linear-gradient(135deg, #a9c9fffc 0%, #ffbbec 100%) 1;
          transition: all 0.2s;
        }
      }
    }
  }
}
</style>
