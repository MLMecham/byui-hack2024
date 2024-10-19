# Fit Forge: Forged Body | Fit Future

Welcome to **Fit Forge**, a personalized fitness and meal planning web app designed to help users achieve their body transformation goals! Built with powerful AI-driven insights, Fit Forge tailors workout and meal plans to each user's unique profile, including age, weight, height, body type goals, and more. Whether you're looking to build muscle, improve endurance, or lose weight, Fit Forge has you covered.

## Features
### Current Features:
- **AI-Generated Workout Plans**: Based on user parameters like age, height, weight, body type, and fitness goals, the app generates tailored fitness plans, incorporating specific exercises and progression tips.
- **AI-Generated Meal Plans**: Fit Forge provides custom meal plans that align with the user's workout goals and dietary preferences, including calorie counts, macronutrients, and even a shopping list!
- **Personal Trainer Chatbot**: Users can interact with an AI chatbot to refine and adjust their workout and meal plans.
- **"Power Move" Daily Challenge**: Gamify your workout with randomized daily fitness challenges, including endurance holds, high-intensity intervals, and bodyweight exercises.

### Future Features:
- **Progress Tracking**: Monitor your fitness progress over time with graphical representations of your improvements.
- **Daily Challenges (POWER MOVE)**: Fresh daily challenges to push your limits.
- **Lift Lab**: Access personalized workout routines and track progress.
- **Motivational Quotes** (Upcoming): Receive daily encouragement to keep your momentum going.
- **Additional Analytics with Gemini API**: Leverage advanced analysis for fitness and meal prep plans using the Gemini API for a more data-driven approach to your fitness journey.

## Tech Stack
- **Front-End**: Python (Streamlit)
- **Database**: MongoDB
- **API**: Gemini API for enhanced fitness analytics
- **Deployment**: GoDaddy
- **Other Tools**: 
  - Pymongo for database management
  - Integration of AI models to generate personalized plans
  - Multi-page navigation via Streamlit

## Getting Started
To deploy or run Fit Forge locally, follow these steps:

1. Clone the repository to your local environment:
   ```bash
   git clone https://github.com/your-repo/Fit-Forge.git
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your environment variables for MongoDB:

Create a .streamlit folder in your root directory.
Inside .streamlit, create a mongokey.txt file and add your MongoDB connection key.
Run the app:

bash
Copy code
streamlit run app.py
Deployment
Fit Forge is deployed via GoDaddy. To deploy, follow these steps:

Purchase a domain and hosting plan on GoDaddy.
Set up a Python-compatible environment on your GoDaddy server.
Deploy your app by following GoDaddy's documentation on deploying Python applications.
Future Development Goals
Implement motivational quotes for user engagement.
Introduce user progress tracking and analytics.
Enhance the Lift Lab feature for tracking specific workout goals.
Incorporate Gemini API for deeper fitness and nutritional insights.