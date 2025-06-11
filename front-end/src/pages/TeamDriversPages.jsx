import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import { getDriversByTeam } from "../services/api";

export default function TeamDriversPage() {
  const { team_id } = useParams();
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    getDriversByTeam(team_id).then(res => setDrivers(res.data));
  }, [team_id]);

  return (
    <div>
      <h2>Drivers for Team {team_id}</h2>
      <ul>
        {drivers.map(d => <li key={d.id}>{d.name} (age {d.age})</li>)}
      </ul>
    </div>
  );
}
