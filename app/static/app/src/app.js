import React from 'react';
import { createRoot } from 'react-dom/client';
import App1 from './components/App1';
import App2 from './components/App2';

const domNode1 = document.getElementById('container-1');
const root1 = createRoot(domNode1);
root1.render(<App1 />);

// const domNode2 = document.getElementById('container-2');
// const root2 = createRoot(domNode2);
// root2.render(<App2 />);