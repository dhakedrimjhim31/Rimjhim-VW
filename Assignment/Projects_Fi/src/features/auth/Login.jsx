import { useNavigate } from "react-router-dom";

function Login() {

  const navigate = useNavigate();

  function handleLogin(e) {

    e.preventDefault();

    navigate("/dashboard");

  }

  return (

    <div className="login-container">

      <div className="login-box">

        <h2>Login</h2>

        <form onSubmit={handleLogin}>

          <input type="email" placeholder="Email" required />

          <input type="password" placeholder="Password" required />

          <button>Login</button>

        </form>

      </div>

    </div>

  );

}

export default Login;