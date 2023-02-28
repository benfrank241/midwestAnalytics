import React, { useState } from 'react';
import { data, data2 } from '../data.js';
import './Table.css'


const Table = () => {
  const [tableData, setData] = useState(data);

  return (
    <table>
      <caption>March 22nd 2023 Midwest Conference Woman's Basketball Rankings </caption>
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
        {tableData.map((item) => (
          <tr key={item.id}>
            <td>{item.rank}</td>
            <td>{item.team}</td>
            <td>{item.eloRating}</td>
            <td>{item.makeChampionshipPct}</td>
            <td>{item.winChampionshipPct}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default Table;
