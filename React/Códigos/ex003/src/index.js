import React, { useState } from "react";
import ReactDOM from "react-dom";

import "./styles.css";

// componente
function App() {
  // estado do jogo: Entrada, rodando, final
  const [estado, setEstado] = useState("ENTRADA");

  // Palpite da máquina
  const [palpite, setPalpite] = useState(150);

  // Quantidade de palpites a maquina fez
  const [numPalpites, setNumPalpites] = useState(1);

  // Definindo limites para os chutes 0 a 300
  const [min, setMin] = useState(0);
  const [max, setMax] = useState(300);

  // Setando parametros iniciais do jogo
  const iniciarJogo = () => {
    setEstado("RODANDO");
    setPalpite(150);
    setNumPalpites(1);
    setMin(0);
    setMax(300);
  };

  // Modifica o maior numero
  const menor = () => {
    setNumPalpites(numPalpites + 1);
    setMax(palpite);
    const proxPalpite = parseInt((min + palpite) / 2);
    setPalpite(proxPalpite);
  };

  // modifica o menor numero
  const maior = () => {
    setNumPalpites(numPalpites + 1);
    setMin(palpite);
    const proxPalpite = parseInt((palpite + max) / 2);
    setPalpite(proxPalpite);
  };

  // Quando acertar o numero
  const acertar = () => {
    setEstado("FIM");
  };

  // Caso o estado seja ENTRADA não quero que reenderize os três botões,
  // quero que reenderize apenas um, que será um botão para iniciar o jogo.
  // E caso seja FIM quero que apareça o resultado final e um botão de reset
  if (estado === "ENTRADA") {
    return (
      <div>
        <p>{estado}</p>
        <button onClick={iniciarJogo}>Iniciar</button>
      </div>
    );
  } else if (estado === "FIM") {
    return (
      <div>
        <p>
          Acertei o número {palpite} com um total de {numPalpites} chutes
        </p>
        <button onClick={iniciarJogo}>Reiniciar</button>
      </div>
    );
  }

  // Caso o return tenha que vim parar aqui, ou seja, se não estamos no começo
  // e nem no final, então vamos executar esse bloco
  return (
    <div className="App">
      <p>{estado}</p>
      <p>O seu numero é {palpite}?</p>
      <p>min: {min} / max: {max}</p>
      <button onClick={maior}>Maior</button>
      <button onClick={acertar}>Acertou</button>
      <button onClick={menor}>Menor</button>
      <p>Numero de Chutes: {numPalpites}</p>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
