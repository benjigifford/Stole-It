from flask import Flask, request, render_template
import audio_capture
import transcription
import database

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/search" method="post">
            <input type="text" name="keyword">
            <input type="submit" value="Search">
        </form>
    '''

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form['keyword']
    results = database.search_transcripts(keyword)
    return render_template('search_results.html', results=results)

if __name__ == '__main__':
    database.create_database()
    app.run(host='0.0.0.0', port=5000)
