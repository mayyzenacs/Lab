let guys = [
  { name: "ana", age: 20 },
  { name: "mayra", age: 16 },
  { name: "lucas", age: 24 },
  { name: "carol", age: 17 },
];

for (let i = 0; i < guys.length; i++) {
  if (guys[i].age > 18) {
    console.log(guys[i].name);
  }
}
