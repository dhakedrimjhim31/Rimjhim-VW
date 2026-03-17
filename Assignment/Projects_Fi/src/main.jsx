import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/global.css";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);




##############################################
store.jsx
import React, { createContext, useContext, useState, useCallback } from "react";

const AppContext = createContext();

export const useApp = () => useContext(AppContext);

export const AppProvider = ({ children }) => {

  const [user, setUser] = useState({
    id: 1,
    name: "Admin",
    role: "Admin"
  });

  const [users] = useState([
    { id: 1, name: "Admin", role: "Admin" },
    { id: 2, name: "John", role: "Employee" },
    { id: 3, name: "Sara", role: "Employee" }
  ]);

  const [assets, setAssets] = useState([
    { id: 1, name: "Laptop", status: "Available", assignedTo: null },
    { id: 2, name: "Monitor", status: "Available", assignedTo: null },
    { id: 3, name: "Keyboard", status: "Available", assignedTo: null }
  ]);

  const [assignments, setAssignments] = useState([]);

  const [issues, setIssues] = useState([]);

  // LOGIN
  const login = (name) => {
    const found = users.find(u => u.name === name);
    if (found) setUser(found);
  };

  // LOGOUT
  const logout = () => setUser(null);

  // ADD ASSET
  const addAsset = (name) => {

    const newAsset = {
      id: assets.length + 1,
      name,
      status: "Available",
      assignedTo: null
    };

    setAssets([...assets, newAsset]);
  };

  // ASSIGN ASSET
  const assignAsset = useCallback((assetId, userId, notes) => {

    const asset = assets.find(a => a.id === parseInt(assetId));

    if (!asset) {
      return { success: false, message: "Asset not found" };
    }

    if (asset.status === "Assigned") {
      return { success: false, message: "Asset already assigned" };
    }

    const newAssignment = {
      id: assignments.length + 1,
      assetId: parseInt(assetId),
      userId: parseInt(userId),
      assignedDate: new Date().toISOString(),
      returnDate: null,
      notes
    };

    setAssignments([...assignments, newAssignment]);

    const updatedAssets = assets.map(a =>
      a.id === parseInt(assetId)
        ? { ...a, status: "Assigned", assignedTo: parseInt(userId) }
        : a
    );

    setAssets(updatedAssets);

    return { success: true };

  }, [assets, assignments]);

  // RETURN ASSET
  const returnAsset = useCallback((assignmentId) => {

    const updatedAssignments = assignments.map(a => {
      if (a.id === assignmentId) {
        return {
          ...a,
          returnDate: new Date().toISOString()
        };
      }
      return a;
    });

    setAssignments(updatedAssignments);

    const assignment = assignments.find(a => a.id === assignmentId);

    if (!assignment) return;

    const updatedAssets = assets.map(asset =>
      asset.id === assignment.assetId
        ? { ...asset, status: "Available", assignedTo: null }
        : asset
    );

    setAssets(updatedAssets);

  }, [assignments, assets]);

  const value = {
    user,
    users,
    assets,
    assignments,
    issues,

    login,
    logout,

    addAsset,

    assignAsset,
    returnAsset
  };

  return (
    <AppContext.Provider value={value}>
      {children}
    </AppContext.Provider>
  );
};









#####################################
assignmentpage.jsx
import React, { useState } from "react";
import { useApp } from "../../core/store";

export default function AssignmentsPage() {

  const {
    assets,
    users,
    assignments,
    assignAsset,
    returnAsset,
    user
  } = useApp();

  const [assetId, setAssetId] = useState("");
  const [userId, setUserId] = useState("");
  const [notes, setNotes] = useState("");

  const handleAssign = () => {

    const result = assignAsset(assetId, userId, notes);

    if (!result.success) {
      alert(result.message);
      return;
    }

    alert("Asset assigned successfully");

    setAssetId("");
    setUserId("");
    setNotes("");
  };

  const assignmentData = assignments.map(a => {

    const asset = assets.find(asset => asset.id === a.assetId);
    const userData = users.find(u => u.id === a.userId);

    return {
      ...a,
      assetName: asset?.name,
      userName: userData?.name
    };
  });

  const visibleAssignments =
    user.role === "Employee"
      ? assignmentData.filter(a => a.userId === user.id)
      : assignmentData;

  return (
    <div className="container mt-4">

      <h3>Asset Assignments</h3>

      {user.role !== "Employee" && (
        <div className="card p-3 mb-4">

          <h5>Assign Asset</h5>

          <div className="row">

            <div className="col-md-4">
              <select
                className="form-select"
                value={assetId}
                onChange={(e) => setAssetId(e.target.value)}
              >
                <option value="">Select Asset</option>

                {assets
                  .filter(a => a.status === "Available")
                  .map(a => (
                    <option key={a.id} value={a.id}>
                      {a.name}
                    </option>
                  ))}
              </select>
            </div>

            <div className="col-md-4">
              <select
                className="form-select"
                value={userId}
                onChange={(e) => setUserId(e.target.value)}
              >
                <option value="">Select Employee</option>

                {users
                  .filter(u => u.role === "Employee")
                  .map(u => (
                    <option key={u.id} value={u.id}>
                      {u.name}
                    </option>
                  ))}
              </select>
            </div>

            <div className="col-md-3">
              <input
                type="text"
                className="form-control"
                placeholder="Notes"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
              />
            </div>

            <div className="col-md-1">
              <button
                className="btn btn-primary"
                onClick={handleAssign}
              >
                Assign
              </button>
            </div>

          </div>
        </div>
      )}

      <table className="table table-bordered">

        <thead>
          <tr>
            <th>Asset</th>
            <th>Assigned To</th>
            <th>Assigned Date</th>
            <th>Return Date</th>
            <th>Action</th>
          </tr>
        </thead>

        <tbody>

          {visibleAssignments.map(a => (

            <tr key={a.id}>

              <td>{a.assetName}</td>
              <td>{a.userName}</td>

              <td>
                {new Date(a.assignedDate).toLocaleDateString()}
              </td>

              <td>
                {a.returnDate
                  ? new Date(a.returnDate).toLocaleDateString()
                  : "-"}
              </td>

              <td>

                {!a.returnDate && user.role !== "Employee" && (
                  <button
                    className="btn btn-danger btn-sm"
                    onClick={() => returnAsset(a.id)}
                  >
                    Return
                  </button>
                )}

              </td>

            </tr>

          ))}

        </tbody>

      </table>

    </div>
  );
}




######################################
app.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Dashboard from "./features/dashboard/Dashboard";
import AssetList from "./features/assets/AssetList";
import IssueReport from "./features/issues/IssueReport";
import AssignmentsPage from "./features/assignments/AssignmentsPage";

export default function App() {

  return (
    <Router>

      <Routes>

        <Route path="/" element={<Dashboard />} />

        <Route path="/assets" element={<AssetList />} />

        <Route path="/issues" element={<IssueReport />} />

        <Route path="/assignments" element={<AssignmentsPage />} />

      </Routes>

    </Router>
  );
}






















###################################################################################
LoginPage.jsx
import { useState } from "react";

function LoginPage() {

const [email,setEmail] = useState("");
const [password,setPassword] = useState("");

const handleLogin = (e) =>{
e.preventDefault();

if(email === "" || password === ""){
alert("Please enter email and password");
}else{
alert("Login successful");
}

}

return(

<div style={{
display:"flex",
justifyContent:"center",
alignItems:"center",
height:"100vh",
background:"#f2f2f2"
}}>

<div style={{
background:"white",
padding:"30px",
borderRadius:"10px",
boxShadow:"0px 0px 10px gray",
width:"300px"
}}>

<h2 style={{textAlign:"center"}}>Login</h2>

<form onSubmit={handleLogin}>

<input
type="email"
placeholder="Enter Email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
style={{width:"100%",padding:"10px",marginBottom:"10px"}}
/>

<input
type="password"
placeholder="Enter Password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
style={{width:"100%",padding:"10px",marginBottom:"10px"}}
/>

<button
type="submit"
style={{
width:"100%",
padding:"10px",
background:"#4CAF50",
color:"white",
border:"none"
}}
>
Login
</button>

</form>

</div>

</div>

)

}

export default LoginPage;



##############################
RegisterPage.jsx
import { useState } from "react";

function RegisterPage(){

const [name,setName] = useState("");
const [email,setEmail] = useState("");
const [password,setPassword] = useState("");

const handleRegister = (e)=>{
e.preventDefault();

if(name==="" || email==="" || password===""){
alert("Please fill all fields");
}else{
alert("Account created successfully");
}

}

return(

<div style={{
display:"flex",
justifyContent:"center",
alignItems:"center",
height:"100vh",
background:"#f2f2f2"
}}>

<div style={{
background:"white",
padding:"30px",
borderRadius:"10px",
boxShadow:"0px 0px 10px gray",
width:"300px"
}}>

<h2 style={{textAlign:"center"}}>Sign Up</h2>

<form onSubmit={handleRegister}>

<input
type="text"
placeholder="Enter Name"
value={name}
onChange={(e)=>setName(e.target.value)}
style={{width:"100%",padding:"10px",marginBottom:"10px"}}
/>

<input
type="email"
placeholder="Enter Email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
style={{width:"100%",padding:"10px",marginBottom:"10px"}}
/>

<input
type="password"
placeholder="Enter Password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
style={{width:"100%",padding:"10px",marginBottom:"10px"}}
/>

<button
type="submit"
style={{
width:"100%",
padding:"10px",
background:"#2196F3",
color:"white",
border:"none"
}}
>
Register
</button>

</form>

</div>

</div>

)

}

export default RegisterPage;
























#####################################################################################################
import { useState } from "react";
import "./login_style.css";

function LoginPage() {

const [email,setEmail] = useState("");
const [password,setPassword] = useState("");

const [username,setUsername] = useState("");
const [role,setRole] = useState("");

const handleLogin = (e)=>{
e.preventDefault();
console.log("Login Data:",email,password);
}

const handleSignup = (e)=>{
e.preventDefault();
console.log("Signup Data:",username,email,password,role);
}

return (

<div className="container">

<input type="checkbox" id="flip" />

<div className="cover">

<div className="front">
<img src="/image.png" alt="" />
<div className="text">
<span className="text-1">
Because <br/> better health <br/> begins with better <br/> CARE
</span>
<span className="text-2">Let's get started.</span>
</div>
</div>

<div className="back">
<div className="text">
<span className="text-1">
Complete miles of journey <br/> with one step
</span>
<span className="text-2">Let's get started</span>
</div>
</div>

</div>


<div className="forms">
<div className="form-content">


{/* LOGIN FORM */}

<div className="login-form">

<div className="title">Login</div>

<form onSubmit={handleLogin}>

<div className="input-boxes">

<div className="input-box">
<i className="fas fa-envelope"></i>

<input
type="email"
placeholder="Enter your email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
required
/>

</div>


<div className="input-box">
<i className="fas fa-lock"></i>

<input
type="password"
placeholder="Enter your password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
required
/>

</div>


<div className="text">
<label htmlFor="flip">Forgot password?</label>
</div>


<div className="button input-box">
<input type="submit" value="Submit"/>
</div>


<div className="text sign-up-text">
Don't have an account?
<label htmlFor="flip"> Signup now</label>
</div>

</div>

</form>

</div>



{/* SIGNUP FORM */}

<div className="signup-form">

<div className="title">Signup</div>

<form onSubmit={handleSignup}>

<div className="input-boxes">


<div className="input-box">
<i className="fas fa-user"></i>

<input
type="text"
placeholder="Enter your name"
value={username}
onChange={(e)=>setUsername(e.target.value)}
required
/>

</div>


<div className="input-box">
<i className="fas fa-envelope"></i>

<input
type="email"
placeholder="Enter your email"
value={email}
onChange={(e)=>setEmail(e.target.value)}
required
/>

</div>


<div className="input-box">
<i className="fas fa-lock"></i>

<input
type="password"
placeholder="Enter your password"
value={password}
onChange={(e)=>setPassword(e.target.value)}
required
/>

</div>


<div className="input-box">
<i className="fas fa-user"></i>

<input
type="text"
placeholder="Enter your role"
value={role}
onChange={(e)=>setRole(e.target.value)}
required
/>

</div>


<div className="button input-box">
<input type="submit" value="Submit"/>
</div>


<div className="text sign-up-text">
Already have an account?
<label htmlFor="flip"> Login now</label>
</div>


</div>

</form>

</div>


</div>
</div>

</div>

);

}

export default LoginPage;





































#######################################################################assignmentpage.jsx
import { useState } from "react";
import { useApp } from "../../core/useApp";
import DataTable from "../../shared/components/DataTable";
import ErrorBoundary from "../../shared/components/ErrorBoundary";
import { ROLES } from "../../core/constants";

export default function AssignmentsPage() {
  const {
    user,
    assignments,
    assets,
    users,
    assignAsset,
    returnAsset,
    hasPermission,
    PERMISSIONS
  } = useApp();

  const [showAssignForm, setShowAssignForm] = useState(false);

  const currentUser = user;

  const isAdmin = currentUser?.role === ROLES.ADMIN || currentUser?.role === ROLES.IT_MANAGER;

  const handleAssign = (assetId, userId, notes) => {

    const alreadyAssigned = assignments.find(
      a => a.assetId === assetId && !a.returnDate
    );

    if (alreadyAssigned) {
      alert("This asset is already assigned.");
      return;
    }

    assignAsset(assetId, userId, notes);
    setShowAssignForm(false);
  };

  const handleReturn = (assignmentId) => {
    if (window.confirm("Return this asset?")) {
      returnAsset(assignmentId);
    }
  };

  const visibleAssignments = isAdmin
    ? assignments
    : assignments.filter(a => a.userId === currentUser.id);

  // Prepare table data
  const assignmentData = visibleAssignments.map(assignment => {

    const asset = assets.find(a => a.id === assignment.assetId);
    const user = users.find(u => u.id === assignment.userId);
    const assignedBy = users.find(u => u.id === assignment.assignedBy);

    return {
      ...assignment,
      assetName: asset?.name || "Unknown",
      assetCategory: asset?.category || "",
      userName: user?.name || "",
      userEmail: user?.email || "",
      assignedByName: assignedBy?.name || "System"
    };

  });

  const columns = [

    {
      key: "assetName",
      header: "Asset",
      render: (value, assignment) => (
        <div>
          <div className="fw-semibold">{value}</div>
          <small className="text-muted">{assignment.assetCategory}</small>
        </div>
      )
    },

    {
      key: "userName",
      header: "Employee",
      render: (value, assignment) => (
        <div>
          <div>{value}</div>
          <small className="text-muted">{assignment.userEmail}</small>
        </div>
      )
    },

    {
      key: "assignedDate",
      header: "Assigned",
      render: value =>
        <span className="badge bg-primary">
          {new Date(value).toLocaleDateString()}
        </span>
    },

    {
      key: "returnDate",
      header: "Status",
      render: value =>
        value
          ? <span className="badge bg-success">Returned</span>
          : <span className="badge bg-warning text-dark">Active</span>
    },

    {
      key: "assignedByName",
      header: "Assigned By"
    },

    {
      key: "notes",
      header: "Notes",
      render: value => value || "—"
    },

    {
      key: "actions",
      header: "Actions",
      render: (value, assignment) => (

        <div className="d-flex gap-2">

          {!assignment.returnDate && isAdmin && (
            <button
              className="btn btn-sm btn-warning"
              onClick={() => handleReturn(assignment.id)}
            >
              Return
            </button>
          )}

        </div>

      )
    }
  ];

  // Dashboard stats
  const totalAssignments = assignments.length;
  const activeAssignments = assignments.filter(a => !a.returnDate).length;
  const returnedAssignments = assignments.filter(a => a.returnDate).length;

  return (

    <ErrorBoundary>

      <div className="container-fluid">

        <div className="mb-4">

          <h3 className="fw-bold">Asset Assignments</h3>
          <p className="text-muted">
            Manage and track employee asset allocations
          </p>

        </div>

        {/* Stats Cards */}

        <div className="row mb-4">

          <div className="col-md-4">
            <div className="card shadow-sm border-0">
              <div className="card-body text-center">
                <h5>Total Assignments</h5>
                <h2 className="fw-bold text-primary">{totalAssignments}</h2>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card shadow-sm border-0">
              <div className="card-body text-center">
                <h5>Active</h5>
                <h2 className="fw-bold text-warning">{activeAssignments}</h2>
              </div>
            </div>
          </div>

          <div className="col-md-4">
            <div className="card shadow-sm border-0">
              <div className="card-body text-center">
                <h5>Returned</h5>
                <h2 className="fw-bold text-success">{returnedAssignments}</h2>
              </div>
            </div>
          </div>

        </div>

        {/* Assign Button */}

        {isAdmin && (

          <div className="mb-3 text-end">
            <button
              className="btn btn-primary px-4 shadow-sm"
              onClick={() => setShowAssignForm(true)}
            >
              + Assign Asset
            </button>
          </div>

        )}

        {/* Table */}

        <div className="card shadow-sm border-0">

          <div className="card-body">

            <DataTable
              data={assignmentData}
              columns={columns}
              searchable
              sortable
              paginated
              pageSize={10}
              emptyMessage="No assignments found"
            />

          </div>

        </div>

        {showAssignForm && (

          <AssignmentForm
            onSave={handleAssign}
            onCancel={() => setShowAssignForm(false)}
            assets={assets}
            users={users}
          />

        )}

      </div>

    </ErrorBoundary>

  );

}

function AssignmentForm({ onSave, onCancel, assets, users }) {

  const [formData, setFormData] = useState({
    assetId: "",
    userId: "",
    notes: ""
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.assetId || !formData.userId) {
      alert("Please select asset and employee");
      return;
    }

    onSave(formData.assetId, formData.userId, formData.notes);
  };

  const availableAssets = assets.filter(a => a.status === "Available");

  return (

    <div className="modal show d-block" style={{ background: "rgba(0,0,0,0.5)" }}>

      <div className="modal-dialog modal-lg modal-dialog-centered">

        <div className="modal-content shadow-lg border-0">

          <div className="modal-header bg-primary text-white">

            <h5 className="modal-title">Assign Asset</h5>

            <button className="btn-close btn-close-white" onClick={onCancel}></button>

          </div>

          <form onSubmit={handleSubmit}>

            <div className="modal-body">

              <div className="row">

                <div className="col-md-6 mb-3">

                  <label className="form-label fw-semibold">Select Asset</label>

                  <select
                    className="form-select"
                    value={formData.assetId}
                    onChange={(e) =>
                      setFormData({ ...formData, assetId: e.target.value })
                    }
                  >

                    <option value="">Choose asset</option>

                    {availableAssets.map(asset => (

                      <option key={asset.id} value={asset.id}>
                        {asset.name} ({asset.category})
                      </option>

                    ))}

                  </select>

                </div>

                <div className="col-md-6 mb-3">

                  <label className="form-label fw-semibold">Employee</label>

                  <select
                    className="form-select"
                    value={formData.userId}
                    onChange={(e) =>
                      setFormData({ ...formData, userId: e.target.value })
                    }
                  >

                    <option value="">Choose employee</option>

                    {users.map(user => (

                      <option key={user.id} value={user.id}>
                        {user.name} ({user.email})
                      </option>

                    ))}

                  </select>

                </div>

              </div>

              <div className="mb-3">

                <label className="form-label fw-semibold">Notes</label>

                <textarea
                  className="form-control"
                  rows="3"
                  placeholder="Optional notes"
                  value={formData.notes}
                  onChange={(e) =>
                    setFormData({ ...formData, notes: e.target.value })
                  }
                />

              </div>

            </div>

            <div className="modal-footer">

              <button
                type="button"
                className="btn btn-light"
                onClick={onCancel}
              >
                Cancel
              </button>

              <button
                type="submit"
                className="btn btn-primary"
              >
                Assign Asset
              </button>

            </div>

          </form>

        </div>

      </div>

    </div>

  );

}








