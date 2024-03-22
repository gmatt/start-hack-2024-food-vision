import { IonPage } from "@ionic/react";
import React from "react";
import "./CameraPage.css";
import MainUiController from "../components/MainUiController";

class CameraPage extends React.Component<{}, {}> {
  private stream?: MediaStream;
  private videoElement?: HTMLVideoElement;

  async componentDidMount() {
    await this.captureStream();
  }

  private async captureStream() {
    const stream = await navigator.mediaDevices.getUserMedia({
      video: { facingMode: "environment" },
    });
    this.stream = stream;
    if (!this.videoElement) {
      return;
    }
    this.videoElement.srcObject = stream;
    await this.videoElement.play();
  }

  componentWillUnmount() {
    if (this.stream) {
      this.videoElement?.pause();
      for (const track of this.stream.getTracks()) {
        track.stop();
        this.stream.removeTrack(track);
      }
      this.stream = null!;
    }
  }

  render() {
    return (
      <IonPage className="camera-page">
        <video
          className="camera-page__video"
          muted
          autoPlay
          playsInline
          ref={(e) => (this.videoElement = e!)}
        />
        <MainUiController />
      </IonPage>
    );
  }
}

export default CameraPage;
