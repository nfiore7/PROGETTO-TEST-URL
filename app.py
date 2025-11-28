from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    risultato = ''
    if request.method == 'POST':
        testo = request.form.get('testo', '')
        if 'http://' in testo:
            risultato = '🚨 PERICOLOSO: trovato http://'
        else:
            risultato = '✅SICURO: nessun http://'
    return f'''
    <h1>TEST URL</h1>
    <form method="post">
        Testo: <input name="testo" size="40"><br><br>
        <button>TEST</button>
    </form>
    <h2>{risultato}</h2>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)