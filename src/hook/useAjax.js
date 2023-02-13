import { isRef, ref, unref, watchEffect } from "vue";

export default function (url, type = "GET") {
  const data = ref(null);
  const error = ref(null);

  function doAjax() {
    const httpRequest = window.XMLHttpRequest
      ? new XMLHttpRequest()
      : new ActiveXObject("Microsoft.XMLHTTP");
    httpRequest.open(type, unref(url), true);
    httpRequest.responseType = unref(url).endsWith(".json") ? "json" : "text";
    httpRequest.onreadystatechange = () => {
      if (httpRequest.readyState == 4 && httpRequest.status === 200) {
        data.value = httpRequest.response;
      } else {
        error.value = {
          error: "错误",
          readyState: httpRequest.readyState,
          statue: httpRequest.status,
          url: unref(url),
        };
      }
    };
    httpRequest.send();
  }

  if (isRef(url)) {
    watchEffect(doAjax);
  } else {
    doAjax();
  }

  return { data, error };
}
