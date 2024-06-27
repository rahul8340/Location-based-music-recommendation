
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, request, jsonify, render_template
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable

# Spotify API credentials
CLIENT_ID = 'cffdc2d0d51845029c109ad3156a78fa'
CLIENT_SECRET = '12a14eecccf244d381420cf9b776f57f'

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

# Flask app
app = Flask(__name__)

# State to keyword mapping for Indian states
state_to_keyword = {
    'Maharashtra': 'Marathi music',
    'Punjab': 'Punjabi music',
    'Tamil Nadu': 'Tamil music',
    'Kerala': 'Malayalam music',
    'Karnataka': 'Kannada music',
    'West Bengal': 'Bengali music',
    'Uttar Pradesh': 'Hindi music',
    'Gujarat': 'Gujarati music',
    'Rajasthan': 'Rajasthani music',
    'Assam': 'Assamese music',
    'Bihar': 'Bhojpuri music',
    'Goa': 'Konkani music',
    'Haryana': 'Haryanvi music',
    'Himachal Pradesh': 'Pahari music',
    'Jammu and Kashmir': 'Kashmiri music',
    'Jharkhand': 'Nagpuri music',
    'Madhya Pradesh': 'Bundelkhandi music',
    'Manipur': 'Manipuri music',
    'Meghalaya': 'Garo music',
    'Mizoram': 'Mizo music',
    'Nagaland': 'Naga music',
    'Odisha': 'Odia music',
    'Sikkim': 'Nepali music',
    'Telangana': 'Telugu music',
    'Tripura': 'Kokborok music',
    'Uttarakhand': 'Garhwali music',
    'Andhra Pradesh': 'Telugu music',
    'Chhattisgarh': 'Chhattisgarhi music',
    'Arunachal Pradesh': 'Nyishi music',
    'Andaman and Nicobar Islands': 'Bengali music',
    'Chandigarh': 'Punjabi music',
    'Dadra and Nagar Haveli': 'Gujarati music',
    'Daman and Diu': 'Gujarati music',
    'Lakshadweep': 'Malayalam music',
    'Puducherry': 'Tamil music',
    'Delhi': 'Hindi music'
}

def get_location_coordinates(location):
    geolocator = Nominatim(user_agent="location-based-music")
    try:
        location = geolocator.geocode(location, timeout=10)
        return location.latitude, location.longitude
    except GeocoderUnavailable:
        return None, None

def get_music_recommendations(keyword, limit=10):
    results = sp.search(q=keyword, type='track', limit=limit)
    
    recommendations = []
    for track in results['tracks']['items']:
        track_info = {
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'spotify_link': track['external_urls']['spotify']
        }
        recommendations.append(track_info)
        
    return recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    location = request.form.get('location')
    latitude, longitude = get_location_coordinates(location)
    
    if latitude is None or longitude is None:
        return jsonify({'error': 'Could not determine location. Please try again.'})

    # Simplified state determination based on location input (assuming location is a city, state)
    state = location.split(',')[-2].strip()
    keyword = state_to_keyword.get(state, 'Bollywood music')

    recommendations = get_music_recommendations(keyword)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
