import os
from PIL import Image
from landingai.predict import Predictor
from gtts import gTTS

def main():
    # 1. Credentials
    endpoint_id = "a8b6ecf4-cce9-413b-bdb2-6981441c0271"
    api_key = "land_sk_8BfgUKHWu3HJe5ypgwGTPja2OufWRirt9raRLKSCDFhCoFvs5U"

    # Directory where this script is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(current_dir, "test.jpg")
    output_audio_path = os.path.join(current_dir, "voice_output.mp3")

    print(f"Loading image from: {image_path}")
    image = Image.open(image_path)

    # 2. Prediction
    print("Sending prediction request to LandingAI...")
    predictor = Predictor(endpoint_id, api_key=api_key)
    predictions = predictor.predict(image)

    print("LandingAI Raw Output:", predictions)

    # 3. Result message
    if len(predictions) > 0:
        label = predictions[0].label_name
        confidence = round(predictions[0].score * 100, 1)
        voice_msg = f"You are looking {label} with {confidence} percent confidence."
    else:
        voice_msg = "No emotion detected."

    print("Result Message:", voice_msg)

    # 4. Voice output generation
    print("Generating voice output via gTTS...")
    tts = gTTS(text=voice_msg, lang='en')
    tts.save(output_audio_path)
    print(f"Saved voice output to: {output_audio_path}")

if __name__ == "__main__":
    main()

