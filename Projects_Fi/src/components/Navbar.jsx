import { useNavigate } from "react-router-dom";

function Navbar() {

  const navigate = useNavigate();

  function logout(){
    localStorage.removeItem("currentUser");
    navigate("/");
  }

  return (
    <div className="navbar">

      <h2>Asset Management System</h2>

      <button onClick={logout}>
        Logout
      </button>

    </div>
  );
}

export default Navbar;