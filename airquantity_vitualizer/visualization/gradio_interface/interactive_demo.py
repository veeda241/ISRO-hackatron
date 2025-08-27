import gradio as gr
import joblib
from pathlib import Path

# 📦 Load the trained model from modeling folder
model_path = Path(__file__).resolve().parent.parent.parent / "modeling" / "AQI_model.pkl"
model = joblib.load(model_path)

# 🔮 Define prediction function
def predict_aqi(pm25, pm10, no2, so2):
    try:
        inputs = [[float(pm25), float(pm10), float(no2), float(so2)]]
        prediction = model.predict(inputs)[0]
        return round(prediction, 2)
    except Exception as e:
        return f"Error: {e}"

# 🚀 Build Gradio interface
app = gr.Interface(
    fn=predict_aqi,
    inputs=[
        gr.Number(label="PM2.5 (μg/m³)"),
        gr.Number(label="PM10 (μg/m³)"),
        gr.Number(label="NO₂ (ppb)"),
        gr.Number(label="SO₂ (ppb)")
    ],
    outputs=gr.Number(label="Predicted AQI"),
    title="🌿 Air Quality AI Agent",
    description="Enter pollutant levels to predict AQI using trained model",
    allow_flagging="never"
)

# 🎬 Launch
if __name__ == "__main__":
    app.launch()
