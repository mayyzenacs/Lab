class Clientes{
    constructor(nome, idade, estado) {
        this.nome = nome, 
        this.idade = idade,
        this.estado = estado

    }
    speak () {
        console.log(`${this.nome} fala`)
}
}

const c = new Clientes('lucas', 10, 'ceara')

c.speak()