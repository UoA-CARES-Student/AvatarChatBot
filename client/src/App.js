import './App.css';
import Home from './pages/Home'

function App() {
  return (
    <div style={{
      backgroundColor: "gray",
      padding: "5px",
      height: "100%"
    }}>
    <h1 style={{
        marginLeft : "40px"
    }}> Project 24 Demo</h1>
     
      <div className='content'>
        <Home/>
      </div>

      
    </div>
  );
}

export default App;
