import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

function Login(){

const[email,setEmail]=useState("");
const[password,setPassword]=useState("");

const navigate = useNavigate();

function login(){

const user = JSON.parse(localStorage.getItem(email));

if(user && user.password === password){

localStorage.setItem("currentUser", JSON.stringify(user));

navigate("/dashboard");

}else{

alert("Invalid credentials");

}

}

return(

<div className="auth">

<h2>Login</h2>

<input
placeholder="Email"
onChange={(e)=>setEmail(e.target.value)}
/>

<input
type="password"
placeholder="Password"
onChange={(e)=>setPassword(e.target.value)}
/>

<button onClick={login}>
Login
</button>

<p>
Don't have account?
<Link to="/register"> Register</Link>
</p>

</div>

)

}

export default Login