console.clear()




const readline = require('readline-sync')

const idade = readline.questionInt('Digite sua idade: ')


let = idade

if(idade < 16){
    console.log('Não pode votar')
}else if(idade < 18 ){
    console.log('Voto opcional')
}else if( idade < 65){
    console.log('O voto é obrigatório')
}else
        console.log('Não é obrigado a votar')



