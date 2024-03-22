import React from "react";

import "./Gauge.css";

interface Props {
  color: string;
  percent: number;
  text: string;
}

const Gauge: React.FC<Props> = (props) => (
  <div className="gauge">
    <div
      className="gauge__gauge"
      style={{
        background: `conic-gradient(${props.color} 0deg, ${props.color} ${
          (props.percent * 360) / 100
        }deg, transparent ${(props.percent * 360) / 100}deg)`,
        mask: "radial-gradient(circle at center, transparent 0, transparent 60%, black 30%, black 70%, transparent 51%, transparent 100%)",
      }}
    ></div>
    <div className="gauge__text">{props.text}</div>
  </div>
);

export default Gauge;
