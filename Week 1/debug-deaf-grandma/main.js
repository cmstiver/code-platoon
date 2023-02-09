let keepGoing = true;
let goodbyes = 0;

while (keepGoing) {
  let userInput = prompt();

  if (userInput === "") {
    alert("WHAT!?");
  } else if (userInput.toUpperCase() !== userInput) {
    alert("SPEAK UP, KID!");
  } else if (userInput === "GOODBYE!") {
    goodbyes += 1;
    if (goodbyes == 1) {
      alert("LEAVING SO SOON?");
      console.log(goodbyes);
    } else if (goodbyes >= 2) {
      alert("LATER, SKATER!");
      keepGoing = false;
    }
  } else {
    alert("NO, NOT SINCE 1946!");
  }
}
