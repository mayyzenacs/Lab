const promise = new Promise((resolve, reject) => {
    const numberID = 256

    if (numberID === 256) {
        resolve('Correto')
    } else {
        reject('Incorreto')
    }
})

promise.then((data) => {
    console.log(data)
})


const arr = [31, 16, 45, 98, 87, 39, 49]
const valorProcurado = 87

for (i = 0; i < arr.length; i++) {
    if (arr[i] === valorProcurado) {
        return console.log(arr[i])
    }
}



