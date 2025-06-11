import { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { getDrivers, deleteDriver } from "../services/api";

export default function DriversPage() {
  const [drivers, setDrivers] = useState([]);

  useEffect(() => {
    getDrivers().then(res => setDrivers(res.data));
  }, []);

  const handleDelete = (id) => {
    deleteDriver(id).then(() => setDrivers(drivers.filter(d => d.id !== id)));
  };

  return (
    <div>
      <h1>Drivers</h1>
      <Link to="/drivers/new">Create New Driver</Link>
      <ul>
        {drivers.map(driver => (
          <li key={driver.id}>
            {driver.name} (age {driver.age})
            <div>
              <Link to={`/drivers/${driver.id}/edit`}>Edit</Link> | 
              <button onClick={() => handleDelete(driver.id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}
