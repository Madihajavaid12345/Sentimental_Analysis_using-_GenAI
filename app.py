import streamlit as st
import joblib  # Replace with torch if using a PyTorch model

# Load the trained model (ensure the model file is in the same directory)
model = joblib.load('path_to_your_model.pkl')

# Streamlit UI
st.title("Sentiment Analysis App using GenAI Models")

# Text input from the user
user_input = st.text_area("Enter text to analyze sentiment:", "")

# Prediction button
if st.button("Analyze"):
    if user_input:
        # Perform prediction
        prediction = model.predict([user_input])
        sentiment = "Positive" if prediction[0] == 1 else "Negative"
        st.write(f"**Predicted Sentiment:** {sentiment}")
    else:
        st.warning("Please enter some text to analyze.")

# Optional: Footer
st.write("---")
st.caption("Built with Streamlit and GenAI models.")
