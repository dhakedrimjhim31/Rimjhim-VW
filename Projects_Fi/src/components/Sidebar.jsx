import { Link } from "react-router-dom";

function Sidebar(){

return(

<div className="sidebar">

<h3>Menu</h3>

<ul>

<li>
<Link to="/dashboard">Dashboard</Link>
</li>

<li>
<Link to="/assets">Assets</Link>
</li>

<li>
<Link to="/assignments">Assignments</Link>
</li>

<li>
<Link to="/issues">Issues</Link>
</li>

<li>
<Link to="/users">Users</Link>
</li>

</ul>

</div>

)

}

export default Sidebar