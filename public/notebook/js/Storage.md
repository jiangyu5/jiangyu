# sessionStorage

> 数据在页面会话结束时会被清除

### 保存

```
sessionStorage.setItem('key', 'value');
```

### 读取

```
let data = sessionStorage.getItem('key');
```

### 移除

```
sessionStorage.removeItem('key');
```

### 清除

```
sessionStorage.clear();
```





# localStorage

> 没有过期时间设置

### 创建

```js
localStorage.setItem('myCat', 'Tom');
```

### 读取

```js
let cat = localStorage.getItem('myCat');
```

### 移除

```js
localStorage.removeItem('myCat');
```

### 清空

```js
// 移除所有
localStorage.clear();
```