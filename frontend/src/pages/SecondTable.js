import React, { useState } from 'react';
import './Table.css';
import { data, data2 } from '../data.js';


const SecondTable = () => {
    const [tableData, setData] = useState(data2);
    return (
        <table>
          <caption>Final 2022 Midwest Conference Woman's Basketball Rankings </caption>
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

export default SecondTable;
