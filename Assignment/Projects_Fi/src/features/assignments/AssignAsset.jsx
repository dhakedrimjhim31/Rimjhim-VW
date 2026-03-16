import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";

function AssignAsset() {

  return (

    <>
      <Sidebar />

      <div className="main">

        <Navbar />

        <h1>Assign Asset</h1>

        <form className="assign-form">

          <input placeholder="Employee Name" />

          <input placeholder="Asset Name" />

          <button>Assign</button>

        </form>

      </div>

    </>
  );

}

export default AssignAsset;