var i = 0;

// for
for (i = 0; i < 10; i++) {
  console.log(i);
}
console.log(`o valor de i após o for: ${i}`);

// while
i = 0;
while (i < 10) {
  console.log(i);
  i++;
}
console.log(`o valor de i após o while: ${i}`);

// do while
i = 0;
do {
  console.log(i);
  i++;
} while (i < 10);
console.log(`o valor de i após o while: ${i}`);

// break
for (i = 0; i < 10; i++) {
  console.log(i);
  if (i == 5) {
    break;
  }
}
