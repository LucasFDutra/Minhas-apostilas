var xhr = new XMLHttpRequest();

xhr.open("GET", "https://api.github.com/users/LucasFDutra");
xhr.send(null);

xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    //4 indica que houve retorno
    console.log(JSON.parse(xhr.responseText)); // json pois a api do github retorna um json
  }
};
