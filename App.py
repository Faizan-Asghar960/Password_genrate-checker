import streamlit as st
from streamlit.components.v1 import html
import random
import string

# Function to generate password
def generate_password(length, use_upper, use_lower, use_digits, use_special):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += "!@#$%^&*()_+"

    if not characters:
        return "Please select at least one option."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to check password strength
def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char in "!@#$%^&*()_+" for char in password):
        strength += 1

    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    else:
        return "Weak"

# Streamlit App
st.title("MFK Password Generator")

# Password length slider
length = st.slider("Password Length", min_value=2, max_value=20, value=10)

# Checkboxes for options
use_upper = st.checkbox("Uppercase Letters")
use_lower = st.checkbox("Lowercase Letters", value=True)
use_digits = st.checkbox("Numbers")
use_special = st.checkbox("Special Characters")

# Generate button
if st.button("Generate Password"):
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    strength = check_password_strength(password)

    # Custom HTML, CSS, aur JavaScript
    custom_code = f"""
    <style>
    .custom-container {{
        background: rgba(0, 0, 0, 0.7);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin-top: 20px;
    }}
    .custom-button {{
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }}
    .custom-button:hover {{
        background-color: #45a049;
    }}
    </style>

    <div class="custom-container">
        <h2>MFK Generated Password:</h2>
        <p>{password}</p>
        <p>Strength: <span>{strength}</span></p>
    </div>
    """

    # Streamlit mein custom code display karein
    html(custom_code, height=200)