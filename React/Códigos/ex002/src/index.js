import React, { useState } from "react";
import ReactDOM from "react-dom";

import "./styles.css";

// componente
function App() {
  const [i, setI] = useState(0);

  function click() {
    setI(i + 1);
  }

  return (
    <div className="App">
      <h1>O valor de i é: {i}</h1>
      <button onClick={click}>Incrementar</button>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
