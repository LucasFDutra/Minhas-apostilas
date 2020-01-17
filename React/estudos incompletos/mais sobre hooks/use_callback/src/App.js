import React, { useState, useCallback } from 'react';
// import Hello from './hello';
import Square from './Square';

const App = () => {
  const [count, setCount] = useState(0);
  const favoriteNums = [7, 21, 31];

  const increment = useCallback((n) => {
    setCount((c) => c + n);
  }, [setCount]);

  return (
    <>
      {/* <Hello increment={increment} /> */}
      <div>
count:
        {' '}
        {count}
      </div>
      {
        favoriteNums.map((n) => (
          <Square increment={increment} n={n} key={n} />
        ))
      }
    </>
  );
};

export default App;
