axios
  .get("https://api.github.com/users/LucasFDutra")
  .then(function(response) {
    console.log(response);
    console.log(response.data);
  })
  .catch(function(error) {
    console.log(error);
  });
