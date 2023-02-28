import React, { useState } from 'react';
import Table from './Table';
import SecondTable from './SecondTable';
import { data, data2 } from '../data.js';



const App = () => {
  const [tableData, setTableData] = useState(data);
  const [secondTableData, setSecondTableData] = useState(data2);

  return (
    <div className="app">
      <Table data={tableData} />
      <SecondTable data={secondTableData} />
    </div>
  );
};

export default App;
