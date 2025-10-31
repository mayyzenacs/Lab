let bin = 0


function pro() {
  return new Promise((resolve, reject) => {
  reject(1)
})
}

const result = pro().then(() => {
  console.log('final')
})
.catch(() => {
  console.log("errp")
})

