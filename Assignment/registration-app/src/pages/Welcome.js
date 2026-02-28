import React from "react";
import { useNavigate } from "react-router-dom";

function Welcome() {
  const navigate = useNavigate();
  const username = localStorage.getItem("username");

  const handleLogout = () => {
    localStorage.removeItem("username");
    navigate("/");
  };

  return (
    <div>
      <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <span className="navbar-brand">Dashboard</span>

          <div className="text-white">
            Welcome {username}
            <button
              className="btn btn-danger btn-sm ms-3"
              onClick={handleLogout}
            >
              Logout
            </button>
          </div>
        </div>
      </nav>

      <div className="container mt-5">
        <h2>This is Second Page</h2>
      </div>
    </div>
  );
}

export default Welcome;