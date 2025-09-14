// 1. SELECIONE OS ELEMENTOS DO DOM


// Pegue o input de busca e a lista <ul> 
const searchInput = document.getElementById('searchInput');
const itemList = document.getElementById('itemList');
const items = itemList.getElementsByTagName('li'); // Pega todos os <li> da list

// 2. ADICIONE O EVENT LISTENER
// Adicione um evento 'input' ao searchInput que irá chamar uma função para filtrar a lista
searchInput.addEventListener('input', () => {
    // 3. IMPLEMENTE A LÓGICA DE FILTRAGEM
    const filterText = searchInput.value.toLowerCase(); 
    
    // Percorra cada item <li> da lista
    for (let i = 0; i < items.length; i++) {
        const item = items[i];
        const itemText = item.textContent.toLowerCase();
        // Verifique se o texto do item inclui o texto do filtro
        // Se incluir, o item deve ser exibido (style.display = '')
        // Se não, o item deve ser escondido (style.display = 'none')
        // SEU CÓDIGO VEM AQUI..
        if (itemText.includes(filterText)) {
            item.style.display = ''
        
        }else {
           item.style.display = 'none'
        }

        
    }
});