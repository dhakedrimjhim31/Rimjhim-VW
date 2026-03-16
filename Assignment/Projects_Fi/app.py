#main.jsx

import React from "react"
import ReactDOM from "react-dom/client"
import App from "./App"
import "./styles/global.css"

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)



#app.jsx
import Router from "./core/router"

function App() {
  return <Router />
}

export default App


## api.js
import axios from "axios"

const api = axios.create({
  baseURL: "http://localhost:5000/api",
  headers:{
    "Content-Type":"application/json"
  }
})

export default api



##router.jsx

import { BrowserRouter, Routes, Route } from "react-router-dom"

import Login from "../features/auth/Login"
import Dashboard from "../features/dashboard/Dashboard"
import AssetList from "../features/assets/AssetList"

export default function Router() {

  return (
    <BrowserRouter>

      <Routes>

        <Route path="/" element={<Login />} />

        <Route path="/dashboard" element={<Dashboard />} />

        <Route path="/assets" element={<AssetList />} />

      </Routes>

    </BrowserRouter>
  )

}




###queryKeys.js

export const QUERY_KEYS = {

ASSETS:"ASSETS",
DASHBOARD:"DASHBOARD",
ISSUES:"ISSUES",
ASSIGNMENTS:"ASSIGNMENTS"

}





##store.js

import { createContext } from "react"

export const UserContext = createContext(null)



####button.jsx
import "./Button.css"

export default function Button({title,onClick}){

return(

<button className="btn" onClick={onClick}>
{title}
</button>

)

}





#datatable.jsx

export default function DataTable({columns,data}){

return(

<table>

<thead>
<tr>
{columns.map(col=>(<th key={col}>{col}</th>))}
</tr>
</thead>

<tbody>

{data.map((row,i)=>(
<tr key={i}>

{columns.map(col=>(
<td key={col}>{row[col]}</td>
))}

</tr>
))}

</tbody>

</table>

)

}



###Modal.jsx
export default function Modal({children}){

return(

<div className="modal">

<div className="modal-content">

{children}

</div>

</div>

)

}




##Loader.jsx
              export default function Loader(){

return <div>Loading...</div>

}










##ErrorBoundary.jsx


import React from "react"

class ErrorBoundary extends React.Component{

constructor(props){
super(props)
this.state={hasError:false}
}

static getDerivedStateFromError(){
return {hasError:true}
}

render(){

if(this.state.hasError){

return <h2>Something went wrong</h2>

}

return this.props.children

}

}

export default ErrorBoundary





##Applayout.jsx
import Sidebar from "../Sidebar/Sidebar"
import Navbar from "../Navbar/Navbar"

export default function AppLayout({children}){

return(

<div className="layout">

<Sidebar/>

<div className="main">

<Navbar/>

<div className="content">
{children}
</div>

</div>

</div>

)

}




###sidebar.jsx
import { Link } from "react-router-dom"

export default function Sidebar(){

return(

<div className="sidebar">

<h2>EAM</h2>

<Link to="/dashboard">Dashboard</Link>
<Link to="/assets">Assets</Link>
<Link to="/assignments">Assignments</Link>
<Link to="/issues">Issues</Link>

</div>

)

}




###navbar.jsx

export default function Navbar(){

return(

<div className="navbar">

<h3>Enterprise Asset Manager</h3>

</div>

)

}




######login.jsx
import { useState } from "react"
import api from "../../core/api"

export default function Login(){

const[email,setEmail]=useState("")
const[password,setPassword]=useState("")

const handleLogin=async()=>{

const res=await api.post("/login",{email,password})

console.log(res.data)

}

return(

<div>

<h2>Login</h2>

<input placeholder="Email"
onChange={(e)=>setEmail(e.target.value)}/>

<input type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}/>

<button onClick={handleLogin}>
Login
</button>

</div>

)

}






###assetlist.jsx
import { useEffect,useState } from "react"
import api from "../../core/api"

export default function AssetList(){

const[assets,setAssets]=useState([])

useEffect(()=>{

fetchAssets()

},[])

const fetchAssets=async()=>{

const res=await api.get("/assets")

setAssets(res.data)

}

return(

<div>

<h2>Assets</h2>

<ul>

{assets.map(asset=>(
<li key={asset.id}>{asset.name}</li>
))}

</ul>

</div>

)

}



####global.css

body{
margin:0;
font-family:Arial;
background:#f4f6f9;
}


#######variable.css
:root{

--primary:#2b6cb0;
--background:#f4f6f9;
--text:#333;

}



####button.css
.btn{
padding:10px 18px;
background:#2b6cb0;
color:white;
border:none;
border-radius:6px;
cursor:pointer;
}

.btn:hover{
background:#1a4c8b;
}





####datatable.css

table{
width:100%;
border-collapse:collapse;
}

th,td{
padding:10px;
border:1px solid #ddd;
}

th{
background:#f4f4f4;
}





###modal.css

.modal{
position:fixed;
top:0;
left:0;
right:0;
bottom:0;
background:rgba(0,0,0,0.5);
display:flex;
justify-content:center;
align-items:center;
}

.modal-content{
background:white;
padding:20px;
border-radius:8px;
}




####loader.css
.loader{
text-align:center;
padding:20px;
font-size:18px;
}




######Applayout.css
.layout{
display:flex;
height:100vh;
}

.main{
flex:1;
display:flex;
flex-direction:column;
}

.content{
padding:20px;
}



##navbar.css
.navbar{
height:60px;
background:#2b6cb0;
color:white;
display:flex;
align-items:center;
padding:0 20px;
}




####sidebar.css
.sidebar{
width:220px;
background:#1f2937;
color:white;
padding:20px;
display:flex;
flex-direction:column;
}

.sidebar a{
color:white;
text-decoration:none;
margin:10px 0;
}



###Register.jsx
import {useState} from "react"
import api from "../../core/api"

export default function Register(){

const[name,setName]=useState("")
const[email,setEmail]=useState("")
const[password,setPassword]=useState("")

const handleRegister=async()=>{

await api.post("/register",{
name,
email,
password
})

}

return(

<div>

<h2>Register</h2>

<input placeholder="Name"
onChange={(e)=>setName(e.target.value)}/>

<input placeholder="Email"
onChange={(e)=>setEmail(e.target.value)}/>

<input type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}/>

<button onClick={handleRegister}>Register</button>

</div>

)

}




####auth.css
.login{
max-width:400px;
margin:auto;
background:white;
padding:20px;
border-radius:8px;
}



####assetform.jsx
import {useState} from "react"
import api from "../../core/api"

export default function AssetForm(){

const[name,setName]=useState("")
const[brand,setBrand]=useState("")

const handleSubmit=async()=>{

await api.post("/assets",{name,brand})

}

return(

<div>

<h2>Add Asset</h2>

<input placeholder="Asset Name"
onChange={(e)=>setName(e.target.value)}/>

<input placeholder="Brand"
onChange={(e)=>setBrand(e.target.value)}/>

<button onClick={handleSubmit}>
Add
</button>

</div>

)

}


  


##########assetdetails.jsx
export default function AssetDetails({asset}){

return(

<div>

<h3>{asset.name}</h3>

<p>Brand: {asset.brand}</p>
<p>Status: {asset.status}</p>

</div>

)

}



#######assets.css
.asset-card{
background:white;
padding:15px;
border-radius:6px;
margin-bottom:10px;
}



#####Dashboard.jsx
import StatsCards from "./StatsCards"
import Charts from "./Charts"

export default function Dashboard(){

return(

<div>

<h1>Dashboard</h1>

<StatsCards/>

<Charts/>

</div>

)

}


#######StatsCards.jsx

export default function StatsCards(){

return(

<div className="stats">

<div>Total Assets</div>
<div>Assigned Assets</div>
<div>Open Issues</div>

</div>

)

}




#########Charts.jsx

import {Bar} from "react-chartjs-2"

export default function Charts(){

const data={
labels:["Assets","Issues"],
datasets:[{data:[10,5]}]
}

return <Bar data={data}/>
}



#########dashboard.css

.stats{
display:flex;
gap:20px;
}

.stats div{
background:white;
padding:20px;
border-radius:8px;
}




######IssueReport.jsx
export default function IssueReport(){

return(

<div>

<h2>Report Issue</h2>

<textarea placeholder="Describe issue"/>

<button>Submit</button>

</div>

)

}


###IssueBoard.jsx
export default function IssueBoard(){

return(

<div>

<h2>Issue Board</h2>

<div>Open</div>
<div>In Progress</div>
<div>Resolved</div>

</div>

)

}



#####issues.css
.issue-card{
background:white;
padding:10px;
border-radius:6px;
margin:10px;
}





######AssignAsset.jsx

export default function AssignAsset(){

return(

<div>

<h2>Assign Asset</h2>

<select>
<option>Select Employee</option>
</select>

<select>
<option>Select Asset</option>
</select>

<button>Assign</button>

</div>

)

}




#########AssignmentTable.jsx
export default function AssignmentTable(){

return(

<table>

<thead>
<tr>
<th>Employee</th>
<th>Asset</th>
<th>Date</th>
</tr>
</thead>

<tbody>
<tr>
<td>John</td>
<td>Laptop</td>
<td>12 Mar</td>
</tr>
</tbody>

</table>

)

}







#########assignments.css

.assignment-table{
width:100%;
border-collapse:collapse;
}












#####################################Example better table CSS  global.css
table{
width:100%;
border-collapse:collapse;
background:white;
}

th{
background:#f0f2f5;
text-align:left;
}

th,td{
padding:12px;
border-bottom:1px solid #ddd;
}












        
              



#################################################################################################################
global.css
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f4f6f9;
}

/* SIDEBAR */
.sidebar {
  width: 220px;
  height: 100vh;
  background: #1e293b;
  color: white;
  position: fixed;
  padding: 20px;
}

.sidebar h2 {
  margin-bottom: 30px;
}

.sidebar a {
  display: block;
  color: white;
  text-decoration: none;
  margin: 12px 0;
  padding: 8px;
  border-radius: 6px;
}

.sidebar a:hover {
  background: #3b82f6;
}

/* MAIN AREA */
.main {
  margin-left: 240px;
  padding: 20px;
}

/* CARDS */
.card-container {
  display: flex;
  gap: 20px;
}

.card {
  background: white;
  padding: 20px;
  flex: 1;
  border-radius: 10px;
  box-shadow: 0px 3px 8px rgba(0,0,0,0.1);
}

/* TABLE */
table {
  width: 100%;
  border-collapse: collapse;
  background: white;
}

th, td {
  padding: 12px;
  border-bottom: 1px solid #ddd;
}

th {
  background: #f1f5f9;
}

/* LOGIN */
.login-box {
  width: 350px;
  margin: 120px auto;
  padding: 30px;
  background: white;
  box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
  border-radius: 10px;
}

.login-box input {
  width: 100%;
  padding: 10px;
  margin: 10px 0;
}

.login-box button {
  width: 100%;
  padding: 10px;
  background: #3b82f6;
  color: white;
  border: none;
  border-radius: 6px;
}





################################
sidebar.jsx
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












##############################
dashboard.jsx
import Sidebar from "../../components/Sidebar";
import Charts from "./Charts";

function Dashboard() {
  return (
    <>
      <Sidebar />

      <div className="main">

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















#################################
assetdetails.jsx
import Sidebar from "../../components/Sidebar";

function AssetDetails() {

  return (
    <>
      <Sidebar />

      <div className="main">

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
              <td>Monitor</td>
              <td>LG</td>
              <td>Available</td>
            </tr>

            <tr>
              <td>Printer</td>
              <td>HP</td>
              <td>Assigned</td>
            </tr>

          </tbody>

        </table>

      </div>
    </>
  );
}

export default AssetDetails;







#########################################
issueboard.jsx
import Sidebar from "../../components/Sidebar";

function IssueBoard() {

  return (
    <>
      <Sidebar />

      <div className="main">

        <h1>Issue Board</h1>

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
              <td>Screen broken</td>
              <td>Laptop</td>
              <td>Open</td>
            </tr>

            <tr>
              <td>Paper jam</td>
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












#######################################
assignassets.jsx
import Sidebar from "../../components/Sidebar";

function AssignAsset() {

  return (
    <>
      <Sidebar />

      <div className="main">

        <h1>Assign Asset</h1>

        <form>

          <input placeholder="Employee Name" />

          <input placeholder="Asset Name" />

          <button>Assign</button>

        </form>

      </div>
    </>
  );
}

export default AssignAsset;















###############################
register.jsx
import { useNavigate } from "react-router-dom";

function Register() {

  const navigate = useNavigate();

  function login(e) {
    e.preventDefault();
    navigate("/dashboard");
  }

  return (

    <div className="login-box">

      <h2>Login</h2>

      <form onSubmit={login}>

        <input type="email" placeholder="Email" />

        <input type="password" placeholder="Password" />

        <button>Login</button>

      </form>

    </div>
  );
}

export default Register;





















##################################




