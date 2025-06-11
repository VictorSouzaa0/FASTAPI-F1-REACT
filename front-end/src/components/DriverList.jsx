import React, { useEffect, useState } from "react";
import { getTeams } from "../services/api";

const TeamList = ({ onTeamSelect }) => {
  const [teams, setTeams] = useState([]);

  useEffect(() => {
    getTeams().then(res => setTeams(res.data));
  }, []);

  return (
    <div>
      <h2>Teams</h2>
      <ul>
        {teams.map(team => (
          <li key={team.id} onClick={() => onTeamSelect(team.id)}>
            {team.name} (Age: {team.age}, Location: {team.location})
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TeamList;
