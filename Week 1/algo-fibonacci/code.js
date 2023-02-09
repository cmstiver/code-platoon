function findFibonacci(num) {
  if (num < 2) {
    return num;
  }

  return findFibonacci(num - 1) + findFibonacci(num - 2);
}

console.log(findFibonacci(7));
