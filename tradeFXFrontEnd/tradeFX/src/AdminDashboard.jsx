import React, { useEffect, useState } from 'react';
// import Chart from 'chart.js';
import ReactTable from 'react-table';
import io from 'socket.io-client';

const AdminDashboard = () => {
  // State to store trader data
  const [traders, setTraders] = useState([]);

  
  // const fetchTraders = async () => {
  //   try {
  //     const response = await fetch('http://127.0.0.1:8000/api/trders/');
  //     if (response.status === 200) {
  //       const data = await response.json();
  //       console.log('Fetch successful');
  //       setTraders(data);
  //     } else {
  //       console.error('Failed to fetch traders');
  //     }
  //   } catch (error) {
  //     console.error('Error fetching traders:', error);
  //   }
  // };

  // setInterval(() => {
  //   console.log("fetchTraders called");
  //   fetchTraders();
  // }, 60000);

  // useEffect(() => {

  // }, []);

  useEffect(() => {
    const socket = new WebSocket('ws://localhost:8000/ws/traders/'); // Import WebSocket

    socket.onopen = () => {
      console.log('WebSocket connected');
      socket.send(JSON.stringify({ type: 'get_trader_data' }));
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log('Received trader data:', data);
      const updatedTraders = [...traders, ...data];

      setTraders(updatedTraders);
    };

    socket.onclose = () => {
      console.log('WebSocket disconnected');
    };

    // return () => socket.close();
  }, []);

  const style = {
    width: '100vw',
    padding: '50px',
    textAlign: 'center',
    fontSize: '16px',
};
const body = {
  padding: '20px',
}
const data = {
  marginBottom: '50px',
}
const center = {
  textAlign: 'center',
}
console.log('test');

  return (
    <div style={center}>
      <h1>Admin Dashboard</h1>
      <table style={style}>
        <thead style={data}>
          <tr>
            <th>Trader ID</th>
            <th>Username</th>
            <th>Initial Funding</th>
            <th>Date Started Trading</th>
            <th>Current Balance</th>
            <th>Total Profit</th>
            <th>Last Trade Profit</th>
            <th>Last Trade Time</th>
          </tr>
        </thead>
        <tbody style={body}>
          {traders.map((trader) => (
            <tr key={trader.id}>
              <td style={data}>{trader.id}</td>
              <td style={data}>{trader.name}</td>
              <td style={data}>$100.00</td>
              <td style={data}>{trader.timestamp}</td>
              <td style={data}>${trader.balance}</td>
              <td style={data}>${trader.total_profit}</td>
              <td style={data}>${trader.last_trade_profit}</td>
              <td style={data}>{trader.last_trade_time}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AdminDashboard;

