import React from "react";
import "./MainUiController.css";

interface Props {}

class State {
  predictionHistory: boolean[] = [false, true, false, false, true];
}

type BackendState = State;

class MainUiController extends React.Component<Props, State> {
  state = new State();

  componentDidMount() {
    // this.tick();
  }

  tick = async () => {
    const data: BackendState = await (await fetch("getState")).json();
    this.setState({ predictionHistory: data.predictionHistory });
    setTimeout(this.tick, 500);
  };

  render() {
    return (
      <div className="main-ui-controller">
        {this.state.predictionHistory.map((box) => (
          <div
            className={`main-ui-controller__history-box main-ui-controller__history-box--${
              box ? "detected" : "not-detected"
            }`}
          />
        ))}
      </div>
    );
  }
}

export default MainUiController;
