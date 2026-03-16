import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "./features/auth/Login";
import Register from "./features/auth/Register";
import Dashboard from "./features/dashboard/Dashboard";
import AssetList from "./features/assets/AssetList";
import AssignAsset from "./features/assignments/AssignAsset";
import IssueReport from "./features/issues/IssueReport";
import UserManagement from "./features/users/UserManagement";

function App() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/assets" element={<AssetList />} />
        <Route path="/assignments" element={<AssignAsset />} />
        <Route path="/issues" element={<IssueReport />} />
        <Route path="/users" element={<UserManagement />} />

      </Routes>
    </BrowserRouter>
  );
}

export default App;