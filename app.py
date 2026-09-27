from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

posts = [
    {"id": 1, "titulo": "Mi primer post en Flask", "contenido": "Desarrollando aplicaciones web con Python y Flask."}
]

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/nuevo', methods=('GET', 'POST'))
def nuevo():
    if request.method == 'POST':
        titulo = request.form['titulo']
        contenido = request.form['contenido']
        posts.append({"id": len(posts) + 1, "titulo": titulo, "contenido": contenido})
        return redirect(url_for('index'))
    return render_template('nuevo.html')

if __name__ == '__main__':
    app.run(debug=True)