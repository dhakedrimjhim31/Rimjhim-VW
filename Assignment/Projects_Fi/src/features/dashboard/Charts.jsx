import { Bar } from "react-chartjs-2";
import { Chart, CategoryScale, LinearScale, BarElement } from "chart.js";

Chart.register(CategoryScale, LinearScale, BarElement);

function Charts() {

  const data = {

    labels: ["Laptop", "Printer", "Monitor"],

    datasets: [
      {
        label: "Assets",
        data: [12, 5, 8],
        backgroundColor: "#3b82f6"
      }
    ]
  };

  return (

    <div className="chart">

      <Bar data={data} />

    </div>

  );

}

export default Charts;