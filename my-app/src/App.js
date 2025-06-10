import React, { useState } from 'react';

const PlotComponent = () => {
  const [copies, setCopies] = useState("7");
  const [plotUrl, setPlotUrl] = useState("");

  const handleSubmit = () => {
    const url = `http://localhost:5000/simulate/${copies}`;
    setPlotUrl(url);
  };

  return (
    <div>
      <h2>Chances</h2>
      <div>
        <label>Copies: </label>
        <input type="text" value={copies} onChange={e => setCopies(e.target.value)} />
      </div>
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
