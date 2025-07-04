function reverter(word) {
  var stringreversa = "";
  for (let i = word.length - 1; i >= 0; i--) {
    stringreversa += word[i];
  }
  return console.log(stringreversa);
}

reverter("sabonete");
