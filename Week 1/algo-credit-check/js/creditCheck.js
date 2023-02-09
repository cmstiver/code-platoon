exports.creditCheck = function (str) {
  arr = str.split("");
  arr = arr.map((x) => parseInt(x));

  // Step 1
  for (let i = arr.length - 2; i >= 0; i -= 2) {
    arr[i] *= 2;

    // Step 2
    if (arr[i] > 9) {
      let digits = Array.from(String(arr[i]), Number);
      let sum = digits.reduce((acc, val) => acc + val);
      arr[i] = sum;
    }
  }

  // Step 3
  let sum = arr.reduce((acc, val) => acc + val);

  // Step 4
  if (sum % 10 === 0) {
    return "The number is valid!";
  }
  return "The number is invalid!";
};
