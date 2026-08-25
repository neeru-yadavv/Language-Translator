from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    translated_text = ""

    if request.method == 'POST':
        text = request.form.get('text')
        src_lang = request.form.get('src_lang')
        dest_lang = request.form.get('dest_lang')

        if text:
            try:
                translated_text = GoogleTranslator(
                    source=src_lang,
                    target=dest_lang
                ).translate(text)
            except Exception as e:
                translated_text = "Error: " + str(e)

    return render_template('index.html', translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)