import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";
import Charts from "./Charts";

function Dashboard() {

  return (

    <>

      <Sidebar />

      <div className="main">

        <Navbar />

        <h1>Dashboard</h1>

        <div className="card-container">

          <div className="card">
            <h3>Total Assets</h3>
            <h2>25</h2>
          </div>

          <div className="card">
            <h3>Assigned Assets</h3>
            <h2>15</h2>
          </div>

          <div className="card">
            <h3>Open Issues</h3>
            <h2>4</h2>
          </div>

        </div>

        <Charts />

      </div>

    </>

  );
}

export default Dashboard;