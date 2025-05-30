console.clear()

const readline = require('readline-sync')

const num1 = readline.questionInt  ('Digite seu primeiro numero: ')
const num2 = readline.questionInt  ('Digite seu segundo numero: ')

function mostrarMedia(num1, num2) {
    const media = (num1 + num2) / 2;
    console.log(`A média entre ${num1} e ${num2} é ${media}`);
}




mostrarMedia(num1, num2)


