from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

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

# Flask routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    length = int(data["length"])
    use_upper = data["use_upper"]
    use_lower = data["use_lower"]
    use_digits = data["use_digits"]
    use_special = data["use_special"]

    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    strength = check_password_strength(password)
    return jsonify({"password": password, "strength": strength})

if __name__ == "__main__":
    app.run(debug=True)