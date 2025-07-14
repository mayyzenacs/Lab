const carro = {
    marca: 'toyota',
    modelo: 'yaris',
    ano: 2019
}

class Carro{
    constructor(marca, modelo, ano) {
        this.marca = marca
        this.modelo = modelo
        this.ano = ano
    }
    gasolina(empty) {
        if (empty) {
            return "vazio"
        }
    }
}

const carro1 = new Carro('fiat', 'uno', 2005)

console.log(carro1.modelo)
console.log(carro1.gasolina(1))