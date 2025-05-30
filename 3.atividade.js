console.clear()

const readline = require('readline-sync')

const n1 = readline.questionInt  ('Digite seu número: ')
const n2 = readline.questionInt  ('Digite seu número: ')

let resultado

if (n1 === n2){
    resultado = n1 + n2
    console.log (` ${n1} + ${n2} = ${resultado}`)
}else{
    resultado = (n1 * n2)
    console.log(`${n1} x ${n2} = ${resultado}`)
}