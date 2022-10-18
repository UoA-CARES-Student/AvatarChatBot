import './App.css';
import React from 'react';
import {
  Routes,
  Route,
} from "react-router-dom";
import Home from './pages/Home/Home';
import Vid2Vid from './pages/Vid2Vid/Vid2Vid';
import Img2Vid from './pages/Img2Vid/Img2Vid';


export const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="vid2vid" element={<Vid2Vid />} />
      <Route path="img2vid" element={<Img2Vid />} />
    </Routes>

  );
}

export default App;
