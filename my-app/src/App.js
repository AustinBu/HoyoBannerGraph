import React, { useState } from 'react';

const PlotComponent = () => {
  const [copies, setCopies] = useState("7");
  const [pulls, setPulls] = useState("0");
  const [plotUrl, setPlotUrl] = useState("");
  const [chance, setChance] = useState('0');

  const handleSubmit = () => {
    const url = `http://localhost:5000/simulate/${copies}/${pulls}`;
    setPlotUrl(url);
  };

  return (
    <div>
      <h2>Chances</h2>
      <div>
        <label>Copies: </label>
        <input type="text" value={copies} onChange={e => setCopies(e.target.value)} />
      </div>
      <div>
        <label>Pulls: </label>
        <input type="text" value={pulls} onChange={e => setPulls(e.target.value)} />
      </div>
      <div><label>Chance: {chance}</label></div>
      <button onClick={handleSubmit}>Generate Plot</button>

      {plotUrl && (
        <div style={{ marginTop: "20px" }}>
          <img src={plotUrl} alt="Custom Plot" />
        </div>
      )}
    </div>
  );
};

export default PlotComponent;
