function factorial(num) {
  let total = num;
  let nextNum = total - 1;
  while (nextNum > 0) {
    total *= nextNum;
    nextNum--;
  }
  return total;
}

console.log(factorial(4)); // 24
