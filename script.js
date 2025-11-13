// --- FUNÇÕES DE APOIO (COPIE E COLE NO SEU CÓDIGO) ---

// Simula a busca de dados de um usuário após 2 segundos
function buscarUsuario(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id === 1) {
                resolve({ id: 1, nome: 'Mayra', email: 'mayra@email.com' });
            } else {
                reject(new Error('Usuário não encontrado'));
            }
        }, 2000);
    });
}

// Simula a busca dos pedidos de um usuário
function buscarPedidos(usuarioId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (usuarioId === 1) {
                resolve([
                    { id: 101, produto: 'Notebook' },
                    { id: 102, produto: 'Mouse' }
                ]);
            } else {
                reject(new Error('Pedidos não encontrados'));
            }
        }, 1500);
    });
}

// Simula a busca de detalhes de um pedido
function buscarDetalhesPedido(pedidoId) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (pedidoId === 101) {
                resolve({ id: 101, produto: 'Notebook', preco: 5000, status: 'Enviado' });
            } else {
                reject(new Error('Detalhes do pedido não encontrados'));
            }
        }, 1000);
    });
}
// --- FIM DAS FUNÇÕES DE APOIO ---

// transformando em async/await
async function jornadaUsuario() {
  const usuario = await buscarUsuario(1);
  console.log(usuario.id)

  const pedido = await buscarPedidos(usuario.id); 
  console.log(pedido[0].id)

  const detalhes = await buscarDetalhesPedido(pedido[0].id);
  console.log(detalhes)
}

jornadaUsuario()

//Chame buscar usuario
buscarUsuario(1).then(usuario => {
  console.log(usuario.nome)

  buscarPedidos(usuario.id).then(pedido => {
      console.log(pedido[0].id)

    buscarDetalhesPedido(pedido[0].id).then(detalhes => { 
      console.log(detalhes)
    })
})
}).catch(Error => {
  console.log(Error)
})

//crie sua propria promise 
function checarTemp(temp) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (temp > 30) {
        resolve('está quente', temp)
      } else if (temp <= 30) {
        reject('está agradavel', temp)
      }
    }, 2000);
  })
}

checarTemp(30).then(result => { 
  console.log(result)
}).catch(err => {
  console.log(err)
}) 



