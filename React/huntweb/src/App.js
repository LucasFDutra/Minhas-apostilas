import React, { useState, useEffect } from "react";

function App() {
  const [i, setI] = useState(0);

  useEffect(()=>{
    window.alert('O valor de i foi alterado');
  }, [i])

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
