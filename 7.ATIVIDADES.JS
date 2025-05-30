console.clear()




const nt1 = [7.5, 8.5, 9.0] 
const nt2 = [7.4, 8.5, 9.0] 
const nt3 = [7.1, 8.5, 9.0] 


function mostrarMediaNotas(nt1, nt2, nt3) {
    let soma = 0;
    for (let i = 0; i < notas.length ;i++) {
      soma += notas[i];
    }
    const media = soma / notas.length;
    console.log(`A média das notas é ${media.toFixed(3)}`);
  }