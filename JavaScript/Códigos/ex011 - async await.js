const minhaPromise = function() {
  return new Promise(function(resolve, reject) {
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "http://api.github.com/users/LucasFDutra");
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

const promessa = async () => {
  try {
    const resposta = await minhaPromise();
    console.log(resposta);
  } catch (error) {
    console.log(error);
  }
};

promessa();
