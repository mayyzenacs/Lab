const word = "sabonete";

const vogais = ["a", "e", "i", "o", "u"];

const temvogal = [];

for (let i = 0; i < word.length; i++) {
  if (vogais.find((element) => element === word[i])) {
    temvogal.push(word[i]);
  }
}

console.log(temvogal);
