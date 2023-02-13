import { onMounted, onUnmounted, ref } from "vue";

export default function () {
  const scrollY = ref(null);
  const scrollX = ref(null);

  function update() {
    scrollY.value = window.scrollY;
    scrollX.value = window.scrollX;
  }

  onMounted(() => window.addEventListener("scroll", update));
  onUnmounted(() => window.removeEventListener("scroll", update));

  return {
    scrollY,
    scrollX,
  };
}
