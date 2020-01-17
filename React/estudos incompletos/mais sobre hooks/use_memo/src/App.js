import React, { useState } from 'react';

const App = () => {
  const [count, setCount] = useState(0);

  return (
    <div className='App'>
      <div>
count:
        {' '}
        {count}
      </div>
      <button onClick={() => setCount(count + 1)}>increment</button>
    </div>
  );
};

export default App;
