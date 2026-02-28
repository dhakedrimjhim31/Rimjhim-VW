import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    address: ""
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    localStorage.setItem("username", formData.name);

    navigate("/welcome");
  };

  return (
    <div className="container mt-5">
      <div className="card shadow p-4">
        <h2 className="text-center mb-4">Registration Form</h2>

        <form onSubmit={handleSubmit}>
          <input
            type="text"
            name="name"
            placeholder="Enter Name"
            className="form-control mb-3"
            onChange={handleChange}
            required
          />

          <input
            type="email"
            name="email"
            placeholder="Enter Email"
            className="form-control mb-3"
            onChange={handleChange}
            required
          />

          <input
            type="text"
            name="phone"
            placeholder="Enter Phone"
            className="form-control mb-3"
            onChange={handleChange}
            required
          />

          <textarea
            name="address"
            placeholder="Enter Address"
            className="form-control mb-3"
            onChange={handleChange}
            required
          />

          <button className="btn btn-primary w-100">
            Register
          </button>
        </form>
      </div>
    </div>
  );
}

export default Register;