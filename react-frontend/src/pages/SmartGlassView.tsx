import React from "react";
import "./SmartGlassView.css";
import MainUiController from "../components/MainUiController";
import { IonPage } from "@ionic/react";

const SmartGlassView: React.FC = () => {
  return (
    <IonPage>
      <MainUiController />
    </IonPage>
  );
};

export default SmartGlassView;
