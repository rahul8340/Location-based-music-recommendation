# Location-based-music-recommendation

 ## Overview
The Location-Based Music Recommendation System is a web application that provides music recommendations based on the user's geographical location. This project is tailored to recommend region-specific music for different Indian states, with a primary focus on Bihar, Punjab, and Maharashtra.

 ## Features
- **Geolocation Integration**: Utilizes the Geopy library to determine the user's location.
- **Spotify API Integration**: Leverages Spotipy to fetch music recommendations from Spotify.
- **State-Specific Recommendations**: Offers customized music suggestions for Bihar (Bhojpuri music), Punjab (Punjabi music), and Maharashtra.
- **User-Friendly Interface**: Built with Flask and Bootstrap to ensure an intuitive and responsive user experience.

 ## Technologies Used
- **Python**: Core programming language for backend development.
- **Flask**: Lightweight web framework for creating the backend.
- **Spotipy**: Python library for Spotify Web API.
- **Geopy**: Library for geocoding and fetching location data.
- **Bootstrap**: Framework for building a responsive and attractive frontend.
- **HTML/CSS**: Markup and styling for the web pages.
- **JavaScript**: For dynamic interactions and client-side logic.

 # Installation and Setup
   # Prerequisites
Python 3.7 or higher
Spotify Developer Account

## Steps
1. **Clone the repository:**
   ```bash
    git clone https://github.com/yourusername/location-based-music-recommendation.git
cd location-based-music-recommendation
    ```
2. **Create and activate a virtual environment:**

  ```bash
    python -m venv myenv
source myenv/bin/activate   # On Windows use `myenv\Scripts\activate`
  ```
 
3. **Install the required packages:**

```bash
pip install -r requirements.txt
```
4. **Set up Spotify API credentials:**

- Create a new app on the Spotify Developer Dashboard.
- Get your Client ID and Client Secret.
- Create a .env file in the project root and add your credentials:
  

- CLIENT_ID=your_client_id
- CLIENT_SECRET=your_client_secret

5. **Run the application:**

  flask run
6. **Access the application:**
Open your web browser and navigate to http://127.0.0.1:5000.

## Usage
- **Enter your location**: Provide your location in the input field on the homepage.
- **Receive music recommendations**: Get a list of music tracks tailored to your state.
- **Enjoy your personalized music**: Listen to the recommended tracks.

## Code Structure
- **app.py**: Main application file with Flask routes and logic.
- **templates/**: Contains HTML templates for the frontend.
- **index.html**: Homepage template.
- **static/**: Contains static files like CSS and JavaScript.
- **styles.css**: Custom styles for the application.
- **.env**: File to store environment variables (not included in the repository).

## Acknowledgements
- **Spotify API**: For providing access to a vast library of music.
- **Geopy**: For geolocation services.
- **Flask**: For making web development easy and fun.
- **Bootstrap**: For a responsive and visually appealing design.
