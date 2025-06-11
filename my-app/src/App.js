import React, { useState } from 'react';

const PlotComponent = () => {
  const [copies, setCopies] = useState("7");
  const [pulls, setPulls] = useState("0");
  const [plotUrl, setPlotUrl] = useState("");
  const [chance, setChance] = useState('0');
  const [hide, setHide] = useState(false);

  const handleSubmit = () => {
    const url = `http://localhost:5000/simulate/${copies}/${pulls}`;
    setPlotUrl(url);
    fetch('http://localhost:5000/simulate/getchance')
      .then(response => response.json())
      .then(data => setChance(data.chance));
  };

  return (
    <div>
      <h2>Chances</h2>
      <div>
        { hide ? <button onClick={() => setHide(false)}>Show</button>
        : <button onClick={() => setHide(true)}>Hide</button> }
      </div>
      <div>
        {
          !hide &&
          <><label>{"Copies: "}</label><input type="text" value={copies} onChange={e => setCopies(e.target.value)} /></>
        }
      </div>
      <div>
        {!hide && <><label>Pulls: </label>
        <input type="text" value={pulls} onChange={e => setPulls(e.target.value)} /></>}
      </div>
      <div><label>Chance: {chance}</label></div>
      <button onClick={() => handleSubmit()}>Generate Plot</button>

      {plotUrl && (
        <div style={{ marginTop: "20px" }}>
          <img src={plotUrl} alt="Custom Plot" />
        </div>
      )}
    </div>
  );
};

export default PlotComponent;
