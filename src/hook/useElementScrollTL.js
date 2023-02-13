import { isRef, onMounted, onUnmounted, ref } from "vue";

export default function (el) {
  const scrollTop = ref(null);
  const scrollLeft = ref(null);

  if (isRef(el)) {
    el = el.target;
  }

  function update() {
    scrollTop.value = el.scrollTop;
    scrollLeft.value = el.scrollLeft;
  }

  onMounted(() => window.addEventListener("scroll", update));
  onUnmounted(() => window.removeEventListener("scroll", update));

  return {
    scrollTop,
    scrollLeft,
  };
}
