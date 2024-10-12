from flask import Flask, render_template, request
import openai

app = Flask(__name__)

openai.api_key = "your_openai_api_key_here"

@app.route("/", methods=["GET", "POST"])
def home():
    image_url = None
    if request.method == "POST":
        prompt = request.form.get("prompt")
        image_url = generate_image(prompt)
    return render_template("index.html", image_url=image_url)

def generate_image(prompt):
    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == "__main__":
    app.run(debug=True)