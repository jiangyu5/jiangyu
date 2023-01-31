export default function (url, type = "GET") {
  return new Promise((resolve, reject) => {
    const httpRequest = window.XMLHttpRequest
      ? new XMLHttpRequest()
      : new ActiveXObject("Microsoft.XMLHTTP");

    httpRequest.open(type, url, true);

    httpRequest.onreadystatechange = () => {
      if (httpRequest.readyState == 4 && httpRequest.status === 200) {
        // let res = httpRequest.responseText;
        resolve(httpRequest.responseText);
      }
    };

    //   httpRequest.setRequestHeader();
    httpRequest.send();
  });
}
