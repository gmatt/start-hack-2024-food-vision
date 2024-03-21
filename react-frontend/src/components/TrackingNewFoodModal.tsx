import { IonButton, IonIcon, IonToolbar } from "@ionic/react";
import { NutritionInfo } from "../schemas/nutritionInfo";

import "./TrackingNewFoodModal.css";

import * as IonIcons from "ionicons/icons";
import Gauge from "./Gauge";
import {
  refCalories,
  refCarb,
  refFat,
  refProtein,
} from "../data/referenceValues";

interface Props {
  nutritions: NutritionInfo;
  onSumbit: () => void;
}

const TrackingNewFoodModal: React.FC<Props> = ({ nutritions, onSumbit }) => {
  return (
    <div className="tracking-new-food-modal">
      <img
        className="tracking-new-food-modal__image"
        src={`/public/a_last_milestone.jpg?v=${Date.now()}`}
        alt=""
      />
      <center>
        <h1>
          <IonIcon icon={IonIcons.pricetagOutline} />
          &nbsp;{nutritions.name}
        </h1>
        <h3>
          <IonIcon icon={IonIcons.scaleOutline} />
          &nbsp;{nutritions.quantity}
        </h3>
      </center>
      <div className="tracking-new-food-modal__gauges">
        <Gauge
          color="green"
          percent={(nutritions.calories / refCalories) * 200}
          text={`Calories\n${nutritions.calories}kcal`}
        />
        <Gauge
          color="blue"
          percent={(nutritions.protein / refProtein) * 200}
          text={`Protein\n${nutritions.protein}g`}
        />
        <Gauge
          color="red"
          percent={(nutritions.carb / refCarb) * 200}
          text={`Carbonhydrates\n${nutritions.carb}g`}
        />
        <Gauge
          color="orange"
          percent={(nutritions.fat / refFat) * 200}
          text={`Fats\n${nutritions.fat}g`}
        />
      </div>
      <IonToolbar>
        <IonButton color="danger" shape="round" slot="start">
          <IonIcon icon={IonIcons.closeOutline} />
          &nbsp;Modify
        </IonButton>
        <IonButton
          color="success"
          shape="round"
          slot="end"
          onClick={() => onSumbit()}
        >
          <IonIcon icon={IonIcons.checkmarkOutline} />
          &nbsp;Dismiss
        </IonButton>
      </IonToolbar>
    </div>
  );
};

export default TrackingNewFoodModal;
