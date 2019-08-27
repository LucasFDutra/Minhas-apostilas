import React from "react";
import ReactDOM from "react-dom";

import "./styles.css";

// elemento
const elemento = <h2>Olá mundo</h2>;

// componente
function App() {
  return (
    <div className="App">
      <h1>Hello CodeSandbox</h1>
      <h2>Start editing to see some magic happen!</h2>
      {elemento}
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
