import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from "../features/auth/Login";
import Dashboard from "../features/dashboard/Dashboard";
import AssetDetails from "../features/assets/AssetDetails";
import IssueBoard from "../features/issues/IssueBoard";
import AssignAsset from "../features/assignments/AssignAsset";

function Router() {
  return (
    <BrowserRouter>
      <Routes>

        <Route path="/" element={<Login />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/assets" element={<AssetDetails />} />
        <Route path="/issues" element={<IssueBoard />} />
        <Route path="/assignments" element={<AssignAsset />} />

      </Routes>
    </BrowserRouter>
  );
}

export default Router;