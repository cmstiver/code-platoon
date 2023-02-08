function toRoman(num) {
  let input = num;
  let output = "";
  let romanNumerals = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  };

  for (const romanNumeral in romanNumerals) {
    const arabicNumber = romanNumerals[romanNumeral];
    const evenlyDivisibleTimes = input / arabicNumber;

    if (evenlyDivisibleTimes >= 1) {
      for (let i = 0; i < Math.floor(evenlyDivisibleTimes); i++) {
        output += romanNumeral;
        input -= arabicNumber;
      }
    }
  }

  return output;
}

console.log(toRoman(50)); // L
console.log(toRoman(14)); // XIV
console.log(toRoman(44)); // XLIV
console.log(toRoman(944)); // CMXLIV
