function mesa (array) {
    const args = Array.from(array)
    args.forEach(element => {
        console.log('hello'+ args)
    });
}

mesa('ticket to ride', 'clank', 'arkham horror')