from flask import Flask, request, render_template
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Initialize the recipe generation model
pipe = pipeline("text-generation", model="pratultandon/recipe-nlg-gpt2-train11_15")

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        ingredients = request.form["ingredients"]  
        prompt = f"Recipe with {ingredients}:"
        result = pipe(prompt, max_length=200, num_return_sequences=1)
        recipe = result[0]["generated_text"]

        
        return render_template("home.html", ingredients=ingredients, recipe=recipe)