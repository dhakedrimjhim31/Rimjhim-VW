import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";
import StatsCard from "../../components/StatsCard";
import Charts from "./Charts";

function Dashboard(){

return(

<>
<Sidebar/>

<div className="main">

<Navbar/>

<div className="stats">

<StatsCard title="Total Assets" value="40"/>
<StatsCard title="Assigned Assets" value="20"/>
<StatsCard title="Available Assets" value="15"/>
<StatsCard title="Open Issues" value="5"/>

</div>

<Charts/>

</div>

</>

)

}

export default Dashboard