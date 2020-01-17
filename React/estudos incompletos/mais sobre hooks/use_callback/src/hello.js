import React from 'react';
import { useCountRenders } from './useCountRenders';

const Hello = React.memo(({ increment }) => {
  useCountRenders();
  return (
    <div>
      <div>hello</div>
      <button onClick={() => increment(5)}>+</button>
    </div>
  );
});
export default Hello;
