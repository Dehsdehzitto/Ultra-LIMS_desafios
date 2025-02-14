const botaoPesquisar = document.getElementById('pesquisar');
const campoPesquisa = document.getElementById('campoPesquisa');
const botaoCidade = document.getElementById('cidade');
const botaoEstado = document.getElementById('estado');
const botaoBairro = document.getElementById('bairro');
const caixaEnderecos = document.getElementById('enderecos')
let filtroAtivo = 'cidade'
let enderecos = []
let cidadeAscendente = true
let estadoAscendente = true
let bairroAscendente = true

const mostrarResultado = () => {
  const htmls = enderecos.map(endereco => {
      const html = `
        <div class="endereco">
          <span class="cep">${endereco.cep}</span>
          <span class="cidade-estado">${endereco.localidade} - ${endereco.estado}</span>
          <span class="bairro">${endereco.bairro}</span>
        </div>
      `
    return html
  })
  caixaEnderecos.innerHTML = htmls.join('')
}

const obterHistoricoDePesquisa = async () => {
  let ordenarPor = ''
  if(filtroAtivo == 'cidade') 
    ordenarPor = cidadeAscendente ? 'localidade=asc' : 'localidade=desc'
  if(filtroAtivo == 'bairro')
    ordenarPor = bairroAscendente ? 'bairro=asc' : 'bairro=desc'
  if(filtroAtivo == 'estado')
    ordenarPor = estadoAscendente ? 'estado=asc' : 'estado=desc'
  const resposta = await fetch(`http://localhost:8000/historico?${ordenarPor}`)
  enderecos = await resposta.json()
  mostrarResultado()
}

obterHistoricoDePesquisa()

botaoPesquisar.onclick = async () => {
  const cep = campoPesquisa.value
  const resposta = await fetch(`http://localhost:8000/cep/${cep}`)
  if(resposta.ok) {
    const endereco = await resposta.json()
    enderecos = [endereco, ...enderecos]
    mostrarResultado()
  } else {
    alert("Deu algum erro")
  }
}

botaoCidade.onclick = () => {
  botaoCidade.innerHTML = 'Cidade '
  cidadeAscendente = !cidadeAscendente
  if(cidadeAscendente) {
    botaoCidade.innerHTML += '↑'
  } else {
    botaoCidade.innerHTML += '↓'
  }
  filtroAtivo = 'cidade'
  obterHistoricoDePesquisa()
  botaoCidade.classList.add('marcado')
  botaoEstado.classList.remove('marcado')
  botaoBairro.classList.remove('marcado')
}

botaoEstado.onclick = () => {
  botaoEstado.innerHTML = 'Estado '
  estadoAscendente = !estadoAscendente
  if(estadoAscendente) {
    botaoEstado.innerHTML += '↑'
  } else {
    botaoEstado.innerHTML += '↓'
  }
  filtroAtivo = 'estado'
  obterHistoricoDePesquisa()
  botaoEstado.classList.add('marcado')
  botaoCidade.classList.remove('marcado')
  botaoBairro.classList.remove('marcado')

}

botaoBairro.onclick = () => {
  botaoBairro.innerHTML = 'Bairro '
  bairroAscendente = !bairroAscendente
  if(bairroAscendente) {
    botaoBairro.innerHTML += '↑'
  } else {
    botaoBairro.innerHTML += '↓'
  }
  filtroAtivo = 'bairro'
  obterHistoricoDePesquisa()
  botaoBairro.classList.add('marcado')
  botaoCidade.classList.remove('marcado')
  botaoEstado.classList.remove('marcado')
}

