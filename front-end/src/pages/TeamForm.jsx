import { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getTeam, createTeam, updateTeam } from "../services/api";

export default function TeamForm() {
  const { team_id } = useParams();
  const navigate = useNavigate();
  const [form, setForm] = useState({ name: "", age: "", location: "" });

  useEffect(() => {
    if (team_id) {
      getTeam(team_id).then(res => setForm(res.data));
    }
  }, [team_id]);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const action = team_id ? updateTeam(team_id, form) : createTeam(form);
    action.then(() => navigate("/teams"));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>{team_id ? "Edit" : "Create"} Team</h2>
      <input name="name" placeholder="Name" value={form.name} onChange={handleChange} /><br />
      <input name="age" type="number" placeholder="Age" value={form.age} onChange={handleChange} /><br />
      <input name="location" placeholder="Location" value={form.location} onChange={handleChange} /><br />
      <button type="submit">Submit</button>
    </form>
  );
}