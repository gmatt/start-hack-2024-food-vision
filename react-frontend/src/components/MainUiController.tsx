import React from "react";
import "./MainUiController.css";
import { NutritionInfo } from "../schemas/nutritionInfo";
import { sleep } from "../util";
import TrackingNewFoodModal from "./TrackingNewFoodModal";

interface Props {}

class State {
  predictionHistory: boolean[] = [false, true, false, false, true];
  lastNutritionPrediction?: NutritionInfo = {
    name: "Cheeseburger",
    quantity: "150g",
    calories: 300.0,
    fat: 12.0,
    protein: 15.0,
    carb: 33.0,
  };
  isModalOpen: boolean = true;
}

type BackendState = State;

class MainUiController extends React.Component<Props, State> {
  state = new State();

  componentDidMount() {
    // this.tick();
  }

  private showModal = async () => {
    this.setState({ ...this.state, isModalOpen: true });
    await sleep(150_000);
    this.setState({
      ...this.state,
      isModalOpen: false,
      lastNutritionPrediction: undefined,
    });
  };

  tick = async () => {
    const data: BackendState = await (await fetch("/api/getState")).json();
    this.setState({
      predictionHistory: data.predictionHistory,
      lastNutritionPrediction: data.lastNutritionPrediction,
      isModalOpen: this.state.isModalOpen,
    });
    if (this.state.lastNutritionPrediction != null) {
      await this.showModal();
    }
    setTimeout(this.tick, 1000);
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
        {this.state.isModalOpen && (
          <TrackingNewFoodModal
            nutritions={this.state.lastNutritionPrediction!}
            onSumbit={() =>
              this.setState({ ...this.state, isModalOpen: false })
            }
          />
        )}
      </div>
    );
  }
}

export default MainUiController;
