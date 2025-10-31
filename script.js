function searchNumber () {
  return new Promise ((resolve, reject) => {
    setTimeout(() => {
      let randomNum = Math.random();

      if (randomNum > 0.1) {
        resolve(randomNum)
      }else {
        reject(randomNum)
      }
    }, 2000)
  })
}

searchNumber()
.then(() => {
  console.log("Deu certo")
})
.catch(() => {
  console.log("Errado")
})