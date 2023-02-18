import { onMounted, onUnmounted, ref } from "vue";

class readingProgress {
  criticalHeight = window.innerHeight / 3;

  constructor(container) {
    this.container = container;
    this.init();
  }

  init() {
    if (!this.container.value) return;
    this.titleDoms = readingProgress.getTitleDoms(this.container);
    this.length = this.titleDoms.length;
    this.index = 0;
    this.correctContainerBottom();
  }

  static getTitleDoms(container) {
    if (!container.value) return [];
    return container.value.querySelectorAll("h2, h3, h4, h5");
  }

  // 为 container 设置 padding-bottom
  // 使最后的 title 能够正常跟踪
  // 后续修改样式时，根据需要删除此操作
  correctContainerBottom() {
    let gap = window.innerHeight - this.criticalHeight;
    this.container.value.style.paddingBottom = gap + "px";
  }

  currentTitleTop() {
    return this.titleDoms[this.index].getBoundingClientRect().top;
  }

  nextTitleTop() {
    let nextIndex = this.index + 1;
    if (nextIndex >= this.length) return false;
    return this.titleDoms[nextIndex].getBoundingClientRect().top;
  }

  indexUp() {
    if (this.index + 1 >= this.length) return;
    return ++this.index;
  }

  indexDown() {
    if (this.index <= 0) return;
    return --this.index;
  }

  changeTitleIndex(index) {
    this.index = index;
  }

  scrollChangeTitleIndex() {
    if (!this.length) return;
    if (this.nextTitleTop() < this.criticalHeight) {
      this.indexUp();
    }
    if (this.currentTitleTop() > this.criticalHeight) {
      this.indexDown();
    }
  }

  titleScrollIntoView() {
    window.scrollTo({
      top: this.currentTitleTop() + window.scrollY - this.criticalHeight + 1, // +1 避免误差
      behavior: "smooth",
    });
  }
}

export default function (container) {
  const progress = new readingProgress(container);
  const titleIndex = ref(0); // 与 progress 的 index 一致

  // 文档滚动后对应标题位置
  function scrollChangeTitleIndex() {
    progress.scrollChangeTitleIndex();
  }

  // 设置响应式 title 的 index
  function refIndex() {
    if (progress.index != titleIndex.value) {
      titleIndex.value = progress.index;
    }
  }

  // 滑动到指定标题
  let refIndexTimer = null;
  function changeTitleIndex(index) {
    titleIndex.value = index;
    window.removeEventListener("scroll", refIndex);
    clearTimeout(refIndexTimer);
    refIndexTimer = setTimeout(() => {
      window.addEventListener("scroll", refIndex);
      refIndex();
    }, 1200); // 防止闪烁，这个时间待优化
    progress.changeTitleIndex(index);
    progress.titleScrollIntoView();
  }

  onMounted(() => {
    window.addEventListener("scroll", scrollChangeTitleIndex);
    window.addEventListener("scroll", refIndex);
  });
  onUnmounted(() => {
    window.removeEventListener("scroll", scrollChangeTitleIndex);
    window.removeEventListener("scroll", refIndex);
  });

  return { progress, titleIndex, changeTitleIndex };
}
