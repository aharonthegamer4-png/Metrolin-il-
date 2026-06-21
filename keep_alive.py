from flask import Flask
from threading import Thread
import logging

# הגדרת אפליקציית Flask
app = Flask('')

# ביטול לוגים מיותרים בטרמינל כדי לשמור על סדר
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
    """נקודת הקצה שרנדר יבדוק כדי לוודא שהבוט חי"""
    return "Bot is alive and running 24/7!"

def run():
    # השרת ירוץ על פורט 8080 שמתאים ל-Render
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    """פונקציה שמפעילה את השרת בתהליכון נפרד"""
    t = Thread(target=run)
    t.daemon = True
    t.start()
