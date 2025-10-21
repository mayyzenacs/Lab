
const mesa = [ 
    {nome:"Mansions of madness", nota: 10},
    {nome:"Massive darkness 2", nota: 7},
    {nome:"Lhama", nota: 10},
    {nome:"Destinos", nota: 6},
]

const mesanote = mesa.reduce((prev, curr) => {
    return prev + curr.nota
}, 0)

let c = mesa.every(mesas => mesas.nota === 10)


console.log(c)