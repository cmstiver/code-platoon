exports.isCharacterMatch = function (string1, string2) {
  let counter = {};
  string1 = string1.toLowerCase();
  string2 = string2.toLowerCase();

  for (let char of string1) {
    if (char === " ") {
      continue;
    }
    if (!counter[char]) {
      counter[char] = 1;
    } else {
      counter[char] += 1;
    }
  }

  for (let char of string2) {
    if (char === " ") {
      continue;
    }
    if (!counter[char]) {
      return false;
    } else {
      counter[char] -= 1;
    }
  }

  let arr = Object.values(counter);

  let bool = true;
  for (x of arr) {
    if (x !== 0) {
      return false;
    }
  }

  return bool;
};

exports.anagramsFor = function (word, listOfWords) {
  let arr = listOfWords.filter((elem) => exports.isCharacterMatch(word, elem));

  return arr;
};
