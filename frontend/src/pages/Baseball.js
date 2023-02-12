import React, { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState([]);

  useEffect(() => {
    async function fetchData() {
      const response = await fetch("https://backend.mwcsportsanalytics.com/");
      const json = await response.json();
      console.log(json)
      setData(json);
    }
    fetchData();
  }, []);

  return (
    <table>
    <thead>
    <tr>
    <th>Rank</th>
    <th>Player</th>
    <th>Team</th>
    <th>AVG</th>
    <th>GP-GS</th>
    <th>AB</th>
    <th>R</th>
    <th>H</th>
    <th>1B</th>
    <th>2B</th>
    <th>3B</th>
    <th>HR</th>
    <th>RBI</th>
    <th>TB</th>
    <th>SLG%</th>
    <th>BB</th>
    <th>HBP</th>
    <th>SO</th>
    <th>GDP</th>
    <th>OB%</th>
    <th>SF</th>
    <th>SH</th>
    <th>SB-ATT</th>
    <th>SO%</th>
    <th>BB%</th>
    <th>BB/K</th>
    <th>OPS</th>
    <th>ISO</th>
    <th>BABIP</th>
    <th>RC</th>
    <th>wOBA</th>
    <th>OPS+</th>
    <th>AVG+</th>
    <th>bRating</th>
    </tr>
    </thead>
    <tbody>
    {data.map((item, index) => {
      if (index == 0 || index > 184) return;
      return (
    <tr key={index}>
    <td>{item[1]}</td>
    <td>{item[2]}</td>
    <td>{item[3]}</td>
    <td>{item[4]}</td>
    <td>{item[5]}</td>
    <td>{item[6]}</td>
    <td>{item[7]}</td>
    <td>{item[8]}</td>
    <td>{item[9]}</td>
    <td>{item[10]}</td>
    <td>{item[11]}</td>
    <td>{item[12]}</td>
    <td>{item[13]}</td>
    <td>{item[14]}</td>
    <td>{item[15]}</td>
    <td>{item[16]}</td>
    <td>{item[17]}</td>
    <td>{item[18]}</td>
    <td>{item[19]}</td>
    <td>{item[20]}</td>
    <td>{item[21]}</td>
    <td>{item[22]}</td>
    <td>{item[23]}</td>
    <td>{item[24]}</td>
    <td>{item[25]}</td>
    <td>{item[26]}</td>
    <td>{item[27]}</td>
    <td>{parseFloat(item[28]).toFixed(3)}</td>
    <td>{item[29]}</td>
    <td>{item[30]}</td>
    <td>{item[31]}</td>
    <td>{item[32]}</td>
    <td>{item[33]}</td>
    {/* <td>{item[34]}</td> */}
    <td>{parseFloat(item[34]).toFixed(3)}</td>

    </tr>
    )})}
    </tbody>
    </table>
    );
}

export default App;
