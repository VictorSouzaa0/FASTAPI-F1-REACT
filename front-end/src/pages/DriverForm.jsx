import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { createDriver, updateDriver, getDriver, getTeams } from "../services/api";

export default function DriverForm() {
  const { driver_id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", age: "", team_id: "" });
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    getTeams().then(res => setTeams(res.data));
    if (driver_id) getDriver(driver_id).then(res => setForm(res.data));
  }, [driver_id]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const action = driver_id ? updateDriver(driver_id, form) : createDriver(form);
    action.then(() => navigate("/drivers"));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{driver_id ? "Edit" : "Create"} Driver</h2>
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} /><br />
      <input name="age" type="number" placeholder="Age" value={form.age} onChange={handleChange} /><br />
      <select name="team_id" value={form.team_id} onChange={handleChange}>
        <option value="">Select Team</option>
        {teams.map(t => <option key={t.id} value={t.id}>{t.name}</option>)}
      </select><br />
      <button type="submit">Submit</button>
    </form>
  );
}