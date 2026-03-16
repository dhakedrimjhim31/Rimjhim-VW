import Sidebar from "../../components/Sidebar";
import Navbar from "../../components/Navbar";

function IssueBoard() {

  return (

    <>
      <Sidebar />

      <div className="main">

        <Navbar />

        <h1>Issues</h1>

        <table>

          <thead>
            <tr>
              <th>Issue</th>
              <th>Asset</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>

            <tr>
              <td>Screen Broken</td>
              <td>Laptop</td>
              <td>Open</td>
            </tr>

            <tr>
              <td>Paper Jam</td>
              <td>Printer</td>
              <td>Resolved</td>
            </tr>

          </tbody>

        </table>

      </div>

    </>
  );

}

export default IssueBoard;