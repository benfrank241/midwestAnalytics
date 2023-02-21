import React, { useEffect, useState } from 'react';
import Brython from 'brython';

// TODO: import Brython, import the Python file, and import the data from the Python file, then display it in a table
// Make it so you can switch from previous year to curent year.

const Table = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Load the Brython script
    Brython(1, () => {
      // Import the data from the Python file
      const script = document.createElement('script');
      script.src = 'C:/Users/Ben/CS317/midwestAnalytics/backend/wbbelo.py';
      script.onload = () => {
        const { data } = window.pyodide.globals;
        setData(data);
      };
      document.body.appendChild(script);
    });
  }, []);

  return (
    <table>
      <thead>
        <tr>
          <th>Rank</th>
          <th>Team</th>
          <th>Elo Rating</th>
          <th>Make Championship %</th>
          <th>Win Championship %</th>
        </tr>
      </thead>
      <tbody>
        {data.map((item, index) => (
          <tr key={index}>
            <td>{item.rank}</td>
            <td>{item.team}</td>
            <td>{item.eloRating}</td>
            <td>{item.winChampionshipPct}</td>
            <td>{item.makeChampionshipPct}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
