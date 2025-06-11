import { BrowserRouter, Routes, Route } from "react-router-dom";
import TeamsPage from "../pages/TeamsPages";
import TeamForm from "../pages/TeamForm";
import DriversPage from "../pages/DriversPage";
import DriverForm from "../pages/DriverForm";
import TeamDriversPage from "../pages/TeamDriversPages";

export function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<TeamsPage />} />
        <Route path="/teams" element={<TeamsPage />} />
        <Route path="/teams/new" element={<TeamForm />} />
        <Route path="/teams/:team_id/edit" element={<TeamForm />} />
        <Route path="/teams/:team_id/drivers" element={<TeamDriversPage />} />
        <Route path="/drivers" element={<DriversPage />} />
        <Route path="/drivers/new" element={<DriverForm />} />
        <Route path="/drivers/:driver_id/edit" element={<DriverForm />} />
      </Routes>
    </BrowserRouter>
  );
}