from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Friend data with their traits and emojis
friends_data = {
    "sasi": {
        "traits": ["notorious2", "rob stark", "fork in the weatherspoon", "chaiwala magnetic attraction"],
        "emoji": "😎"
    },
    "satish": {
        "traits": ["Smart", "Hardworking", "Analytical", "problem creater"],
        "emoji": "🧠"
    },
    "rkn": {
        "traits": ["sacrosanct", "techdope", "stoic", "ramsay bolton"],
        "emoji": "⚡"
    },
    "kalanwesh": {
        "traits": ["notorious1", "quickie learner", "maida flour", "CO2 in O2"],
        "emoji": "🚀"
    },
    "prakash": {
        "traits": ["Helpful", "saviour", "psycho", "ted bundy"],
        "emoji": "🤝"
    },
    "maniratnam": {
        "traits": ["Ambitious", "pain in the arse", "insulin driven", "deMotivating"],
        "emoji": "👑"
    }
}

@app.route('/')
def index():
    """Render the dashboard page"""
    return render_template('index.html', friends=list(friends_data.keys()))

@app.route('/api/traits/<friend_name>')
def get_traits(friend_name):
    """API endpoint to get traits for a specific friend"""
    friend_name = friend_name.lower()
    if friend_name in friends_data:
        return jsonify({
            'name': friend_name,
            'traits': friends_data[friend_name]['traits'],
            'emoji': friends_data[friend_name]['emoji'],
            'success': True
        })
    else:
        return jsonify({
            'success': False,
            'error': 'Friend not found'
        }), 404

if __name__ == "__main__":
    print("🌟 Starting Friends Traits Dashboard Server...")
    print("🌐 Open your browser and go to: http://127.0.0.1:80")
    print("💡 All friends are arranged in a circle!")
    app.run(debug=True, host='127.0.0.1', port=80)
