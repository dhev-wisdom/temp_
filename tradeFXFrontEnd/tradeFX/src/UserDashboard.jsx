import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Chart from "chart.js/auto";
import { Line } from 'react-chartjs-2';

// const UserDashboard = () => {
//     const [data, setData] = useState({
//         labels: [1,2,3,4,5,6],
//         datasets: [
//             {
//                 label: 'Profit/Loss',
//                 data: [],
//                 fill: false,
//                 borderColor: 'rgb(250, 252, 192)',
//                 tension: 10,
//             },
//         ],
//     });


//     useEffect(() => {
        
//         // Make an API request to fetch user data, including profit/loss and timestamps
//         fetch('http://127.0.0.1:8000/api/tader/1/')
//             .then((response) => {
//                 const labels = response.data.map((entry) => entry.timestamp);

//                 const profitLossData = response.data.map((entry) => (entry.balance - 100));
//                 setData({
//                     ...data,
//                     labels: labels,
//                     datasets: [
//                         {
//                             ...data.datasets[0],
//                             data: profitLossData,
//                         },
//                     ],
//                 });
//             })
//             .catch((error) => {
//                 console.error(error);
//             });
//     }, []);

//     return (
//         <div>
//             <h1>User Dashboard</h1>
//             <Line data={data} />
//         </div>
//     );
// };



const UserDashboard = () => {
    const config= {
        type: 'line',
        data: data,
        options: {
            scales: {
                y: {beginAtZero: true}
            }
        }
    }
    return (
        <h1>UserDashboard</h1>
    )
}

export default UserDashboard;