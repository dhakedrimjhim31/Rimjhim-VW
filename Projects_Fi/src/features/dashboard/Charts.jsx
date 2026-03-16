import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement } from "chart.js";

ChartJS.register(CategoryScale,LinearScale,BarElement);

function Charts(){

const data = {
labels:["Available","Assigned","Maintenance"],

datasets:[
{
label:"Assets",

data:[15,20,5]
}
]
};

return(

<div>

<h3>Asset Statistics</h3>

<Bar data={data}/>

</div>

)

}

export default Charts