function resolveNumber(number) {

  return new Promise((resolve, reject) => {
    if (number > 2) {
      resolve(number)
    } else {
      reject(number)
    }

  })

}

resolveNumber(1).then((resultado) => {
  console.log(resultado)
})
.catch((err) => {
  console.log(err)
})