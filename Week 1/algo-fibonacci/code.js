function findFibonacci(num) {
  if (num < 2) {
    return num;
  }

  return findFibonacci(num - 1) + findFibonacci(num - 2);
}

console.log(findFibonacci(0) === 0);
console.log(findFibonacci(2) === 1);
console.log(findFibonacci(5) === 5);
console.log(findFibonacci(8) === 21);
console.log(findFibonacci(11) === 89);
console.log(findFibonacci(14) === 377);
console.log(findFibonacci(17) === 1597);
console.log(findFibonacci(20) === 6765);
