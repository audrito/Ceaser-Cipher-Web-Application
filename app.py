from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_amount = shift % 26  # Ensure the shift value wraps around if it's greater than 26
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message
@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    if request.method == "POST":
        # Retrieve data from the POST request
        data = request.json  # Assuming the data is sent in JSON format

        # Extract the message and shift from the data
        message = data.get("message", "")
        shift = int(data.get("shift", 0))

        # Perform your encryption logic (e.g., Caesar cipher)
        encrypted_message = caesar_cipher(message, shift)

        # Return the encrypted message in JSON format
        return jsonify({"encrypted_message": encrypted_message})

    # Handle other HTTP methods or return an error if needed
    return jsonify({"error": "Invalid request"})
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        message = request.form["message"]
        shift = int(request.form["shift"])

        if 1 <= shift <= 25:
            encrypted_message = caesar_cipher(message, shift)
            return jsonify({"encrypted_message": encrypted_message})

        return jsonify({"error": "Shift value must be between 1 and 25"})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)