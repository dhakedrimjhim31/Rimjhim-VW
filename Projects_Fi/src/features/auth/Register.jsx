import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Register(){

const navigate = useNavigate();

const[user,setUser]=useState({
name:"",
email:"",
password:"",
role:"Employee"
})

function handleChange(e){

setUser({...user,[e.target.name]:e.target.value})

}

function register(){

localStorage.setItem(user.email,JSON.stringify(user))

alert("Registration successful")

navigate("/")

}

return(

<div className="auth">

<h2>Register</h2>

<input
name="name"
placeholder="Name"
onChange={handleChange}
/>

<input
name="email"
placeholder="Email"
onChange={handleChange}
/>

<input
name="password"
type="password"
placeholder="Password"
onChange={handleChange}
/>

<select name="role" onChange={handleChange}>

<option>Admin</option>
<option>IT Manager</option>
<option>Employee</option>

</select>

<button onClick={register}>
Register
</button>

</div>

)

}

export default Register