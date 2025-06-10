console.clear()

const readline = require('readline-sync')
let pares = 0;
let impares = 0;

for (let i = 0; i < 6; i++) {
    
    let numero = readline.questionFloat(`Digite seu numero:` )

  if (numero % 2 === 0) { 
    pares++;
  } else {
    impares++;
  }
}

console.log(`Você digitou ${pares} números pares e ${impares} números ímpares.`);
