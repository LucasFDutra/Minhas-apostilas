function soma_convencional(a, b) {
  var s = a + b;
  return s;
}

const soma_anônima = function(a, b) {
  var s = a + b;
  return s;
};

const soma_arrow = (a, b) => {
  var s = a + b;
  return s;
};

const soma_arrow_direta = (a, b) => a + b;

(function(a, b) {
  console.log(a + b);
})(1, 2);

console.log(soma_convencional(1, 2));
console.log(soma_anônima(1, 2));
console.log(soma_arrow(1, 2));
console.log(soma_arrow_direta(1, 2));
