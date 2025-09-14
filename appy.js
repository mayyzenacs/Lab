const readline = require('readline')

const rl = readline.Interface({
    input: process.stdin,
    output: process.stdout
})

function showMenu() {
    console.log('\n===== MENU =====')
    console.log('1 Calculadora comercial')
    console.log('2 Ver calculo anterior')
    console.log('0 Sair')
    rl.question('\nEscolha uma opção', opcao => {
        options(opcao)
    })
}

function calculator(op, value) {
    if (op === 1) {
        let percent = 0.15
        var originalValue = value / (percent - 1)
        var finalValue = (originalValue * 100) / 100 
        return finalValue
    }
}

function options(op) {
    switch (opcao) {
        case '1':
            calculator()
    }
}



