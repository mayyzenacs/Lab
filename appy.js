function reversa (word) {
    reverse = ''
    for (let i = word.length - 1; i >= 0; i--) {
        reverse += word[i]
    }
    if (reverse === word){
        return 'sabonete'
    }
}

reversa('ana')