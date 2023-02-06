function bottleSong(bottles) {
  while (bottles !== 0) {
    if (bottles === 1) {
      console.log(`1 bottle of beer on the wall, 1 bottle of beer.`);
    } else {
      console.log(`${bottles} bottles of beer on the wall, ${bottles} bottles of beer.`);
    }

    bottles -= 1;

    if (bottles === 0) {
      console.log(`Take one down and pass it around, no more bottles of beer on the wall.`);
      console.log("No more bottles of beer on the wall, no more bottles of beer.")
      console.log("Go to the store and buy some more, 99 bottles of beer on the wall.")
    } else if (bottles === 1) {
      console.log(`Take one down and pass it around, 1 bottle of beer on the wall.`);
    } else {
      console.log(`Take one down and pass it around, ${bottles} bottles of beer on the wall.`);
    }
  }
};

bottleSong(99);