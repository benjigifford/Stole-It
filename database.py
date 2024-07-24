import sqlite3

def create_database():
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (id INTEGER PRIMARY KEY, transcript TEXT)''')
    conn.commit()
    conn.close()

def store_transcript(transcript):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (transcript) VALUES (?)", (transcript,))
    conn.commit()
    conn.close()

def search_transcripts(keyword):
    conn = sqlite3.connect('conversations.db')
    c = conn.cursor()
    c.execute("SELECT * FROM conversations WHERE transcript LIKE ?", ('%' + keyword + '%',))
    results = c.fetchall()
    conn.close()
    return results

if __name__ == '__main__':
    create_database()
