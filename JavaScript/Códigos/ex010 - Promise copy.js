const minhaPromise = function() {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://api111.github.com/users/LucasFDutra");
    xhr.send(null);

    xhr.onreadystatechange = function() {
      if (xhr.readyState === 4) {
        if (xhr.status === 200) {
          // 200 indica sucesso na requisição
          resolve(JSON.parse(xhr.responseText));
        } else {
          reject("erro na requisição");
        }
      }
    };
  });
};

minhaPromise()
  .then(function(response) {
    console.log(response);
  })
  .catch(function(error) {
    console.log(error);
  });
