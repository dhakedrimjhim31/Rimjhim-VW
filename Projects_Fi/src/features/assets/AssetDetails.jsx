import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";

function AssetDetails() {

  return (

    <>
      <Sidebar />

      <div className="main">

        <Navbar />

        <h1>Assets</h1>

        <table>

          <thead>
            <tr>
              <th>Asset</th>
              <th>Brand</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>

            <tr>
              <td>Laptop</td>
              <td>Dell</td>
              <td>Assigned</td>
            </tr>

            <tr>
              <td>Printer</td>
              <td>HP</td>
              <td>Available</td>
            </tr>

            <tr>
              <td>Monitor</td>
              <td>LG</td>
              <td>Assigned</td>
            </tr>

          </tbody>

        </table>

      </div>

    </>
  );

}

export default AssetDetails;