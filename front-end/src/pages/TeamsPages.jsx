import { useEffect, useState } from "react";
import { Link  } from "react-router-dom";
import { getTeams, deleteTeam } from "../services/api";

export default function TeamsPages() {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    getTeams().then(res => setTeams(res.data));
  }, []);

  const handleDelete = (id) => {
    deleteTeam(id).then(() => setTeams(teams.filter(t => t.id !== id)));
  };

  return (
    <div>
      <h1>Teams</h1>
      <Link to="/teams/new">Create New Team</Link>
      <ul>
        {teams.map(team => (
          <li key={team.id}>
            {team.name} ({team.location})
            <div>
              <Link to={`/teams/${team.id}/edit`}>Edit</Link> | 
              <Link to={`/teams/${team.id}/drivers`}>Drivers</Link> | 
              <button onClick={() => handleDelete(team.id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
