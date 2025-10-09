
const mesa = ["Ticket to ride", "Lhama", "Mansions of madness"]

function games () {
    mesa.map(game => {
        console.log(game.toUpperCase())
    })
}

games()