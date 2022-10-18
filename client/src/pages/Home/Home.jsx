import React, {useState} from 'react'

import { Link } from "react-router-dom";

const Home = ( ) => {

    return (
    
    <>
        <main>
          <h2>Welcome to the homepage!</h2>
        </main>

        <nav>
          <Link to="/vid2vid">Vid2Vid</Link>
        </nav>

        <nav>
          <Link to="/img2vid">Img2Vid</Link>
        </nav>
      </>
    )
}

export default Home