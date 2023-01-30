import { useState } from'react';
import axios from "axios"
// import logo from './logo.svg';
// import './App.css';


function App() {

    const [baseballData, setBaseballData] = useState(null)

    function getData() {
      axios({
        method: "GET",
        url:"/offense",
      })
      .then((response) => {
        const res =response.data
        setBaseballData(({
          player: res.Player,
          team: res.Team}))
      }).catch((error) => {
        if (error.response) {
          console.log(error.response)
          console.log(error.response.status)
          console.log(error.response.headers)
          }
      })}





      return (
        <div className="App">
          <header className="App-header">
            <p>
              Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
              className="App-link"
              href="https://reactjs.org"
              target="_blank"
              rel="noopener noreferrer"
            >
              Learn React
            </a>
    
            {/* new line start*/}
            <p>To get your profile details: </p><button onClick={getData}>Click me</button>
            {baseballData && <div>
                  <p>Profile name: {baseballData.player}</p>
                  <p>About me: {baseballData.team}</p>
                </div>
            }
             {/* end of new line */}
          </header>
        </div>
      );
    }
    
    export default App;