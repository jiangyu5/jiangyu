## 默认

```vue
// jbtn
<button type="submit">
  <slot>留空或设置默认的内容</slot>
</button>
```

使用

```vue
<jbtn>...</jbtn>
```



## 具名插槽

```vue
// jbtn
<button type="submit">
  <slot name=‘context’></slot>
  <slot name='tip'></slot>
</button>
```

使用

```vue
<jbtn>
	<template v-slot:context>内容</template>
    <template #tip>简写形式</template>
</jbtn>
```



## 动态插槽名

```vue
<base-layout>
  <template v-slot:[dynamicSlotName]>
    ...
  </template>

  <!-- 缩写为 -->
  <template #[dynamicSlotName]>
    ...
  </template>
</base-layout>
```

