const word = "sabonete";

const vogais = ["a", "e", "i", "o", "u"];

const temvogal = [];

for (let i = 0; i < vogais.length; i++) {
  if (vogais[i] === word[i]) {
    temvogal.push(word[i]);
  }
}

console.log(temvogal);
