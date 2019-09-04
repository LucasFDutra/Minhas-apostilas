import React, { useState } from "react";

function App() {
  const [i, setI] = useState(0);

  function click(i) {
    setI(i + 1);
    console.log(i);
  }

  return (
    <div className="App">
      <button onClick={() => click(i)}>Incremento</button>
      <p>O valor de i é: {i}</p>
    </div>
  );
}

export default App;
