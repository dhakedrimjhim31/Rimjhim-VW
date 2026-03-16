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
