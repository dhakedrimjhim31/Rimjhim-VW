import { Link } from "react-router-dom";

function Sidebar() {

  return (

    <div className="sidebar">

      <h2>Asset Manager</h2>

      <Link to="/dashboard">Dashboard</Link>
      <Link to="/assets">Assets</Link>
      <Link to="/issues">Issues</Link>
      <Link to="/assignments">Assignments</Link>

    </div>

  );
}

export default Sidebar;