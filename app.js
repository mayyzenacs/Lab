var car1 = {
  name: "toyota",
  price: 1500,
  condition: "new",
};

var car2 = {
  name: "ford",
  price: 500,
  condition: "old",
};

var car3 = {
  name: "fiat",
  price: 120,
  condition: "ready",
};

var arrayCar = [car1, car2, car3];

for (var car of arrayCar) {
  console.log(car);
}

function cars(arg) {
  arrayCar[0].price = arg;
  var concat = arrayCar[0].name + arrayCar[0].price;
  if (arrayCar[0].price > 600) {
    return "é caro";
  } else {
    return "nao asatisfas";
  }
}

function boaMadrugada(name) {
  for (let i = 0; i < 10; i++) {
    console.log("boa madrugada " + name);
  }
}

boaMadrugada("mayra");

console.log(cars(200));

var person = {
  name: "Lucas",
  age: 24,
};

function checkAge(idade) {
  if (idade > 18) {
    return console.log(18 - person.age);
  }
}

checkAge(person.age);

var objeto = {
  name: "mayra",
  greet() {
    console.log(this);
  },
};

// isso é um comentário

function contagem() {
  console.log("contagem iniciada");
  setTimeout(function () {
    console.log("area limpa");
  }, 5000);
}

contagem();
