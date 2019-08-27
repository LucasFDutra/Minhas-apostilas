function testeVar() {
  console.log(i);
  for (var i = 0; i < 3; i++) {
    console.log(i);
  }
  console.log(i);
}

function testeLet() {
  for (let i = 0; i < 3; i++) {
    console.log(i);
  }
}

function testeConst() {
  for (let i = 0; i < 2; i++) {
    const x = 3;
    console.log(x);
  }
}

testeVar();
testeLet();
testeConst();
