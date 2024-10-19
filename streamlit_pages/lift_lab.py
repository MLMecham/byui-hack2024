import streamlit as st
from ai.gemini import GeminiAI
import random

def ask_api(message):
    """ Creates the AI chat and receives a response from the message.
        args():
        message (string): The message to ask the AI.

        returns:
            response (string): The response from the AI.
    """
    model_name = "gemini-1.5-pro"
    fit_forge_ai = GeminiAI(model_name=model_name)
    return fit_forge_ai.single_message(message)

def lift_lab_page(client):
    db = client["FitForge"]
    collection = db["users"]
    generated = False

    exercises = st.session_state.profile['exercises']
    # st.write(exercises)

    def sendAPI():
        ...

    st.image("streamlit_pages\images\LiftLab2.png")

    # st.title("Lift Lab")
    st.markdown(
    """
    <h1 style="text-align: center;">Let's Make Gains</h1>
    """, 
    unsafe_allow_html=True
)
    st.write("---")

    # Explanation text
    st.write(
        "Welcome to the Lift Lab! Here, you can track your weightlifting exercises, "
        "manage your workout routines, and keep a record of your progress. "
        "Add your preferred exercises to the list, and the chatbot will remember them for future reference. "
        "Feel free to remove any exercises that you no longer need."
    )

    # List to hold the items (exercises)
    # TODO make this list initialize from the database excersizes the user likes
    # if 'exercises' not in st.session_state:
    #     st.session_state.exercises = []

    # Input box to add new exercises
    new_exercise = st.text_input("Add a new exercise:")

    # Button to add the exercise to the list
    if st.button("Add Exercise"):
        if new_exercise:
            if new_exercise not in st.session_state.profile['exercises']:
                st.session_state.profile['exercises'].append(new_exercise)
                st.success(f"Added '{new_exercise}' to your list!")
                collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"exercises": st.session_state.profile['exercises']
                  }}
                )
            else:
                st.error("Please do not duplicate exercises.")
        else:
            st.error("Please enter a valid exercise. No duplicates allowed.")

    # Display the current list of exercises
    if st.session_state.profile['exercises']:
        st.subheader("Current Exercises:")
        exercise_to_remove = st.selectbox("Select an exercise to remove:", st.session_state.profile['exercises'])

        if st.button("Remove Exercise"):
            st.session_state.profile['exercises'].remove(exercise_to_remove)
            st.success(f"Removed '{exercise_to_remove}' from your list!")
            collection.update_one(
                {"username": st.session_state.profile["username"]}, 
                {"$set": {"exercises": st.session_state.profile['exercises']
                  }}
                )
        # Display the list of exercises
        # st.write(st.session_state.exercises)
    else:
        st.write("No exercises added yet.")

    st.write("---")

    st.subheader("Current Fitness Plan")
    document = collection.find_one({"username": st.session_state.profile["username"]})
    st.write(document["fitness_plan"])

    st.write("---")
    st.subheader("Power Move Challenge")
    st.write("🔥 **Are you feeling unstoppable today?** 🔥")
    st.write("Do you want to push your limits and take on a serious challenge? 💪 **Hit the **Power Move** button and unlock a workout that'll test your strength and endurance.** Let's make today the day you crush your goals and set new records!")
    
    # List of intense Power Move challenges
    challenges = [
        "Complete 100 push-ups, 100 sit-ups, and 100 air squats—no rest between exercises!",
        "Hold a plank for 5 minutes. Stay strong!",
        "Perform 50 burpees, followed by a 1-minute wall sit!",
        "Do 100 jumping jacks, 100 mountain climbers, and 100 air squats back-to-back!",
        "Complete 10 sprints of 30 seconds each, with only 10 seconds rest in between!",
        "Perform 5 rounds of 20 push-ups, 20 squats, and 20 lunges!",
        "Run 2 miles as fast as you can!",
        "Hold a wall sit for 3 minutes straight!",
        "Perform 200 air squats. Take minimal rest!",
        "Do 100 push-ups, 100 sit-ups, 100 squats, and 100 lunges—no breaks!",
        "Complete a 10-minute AMRAP (As Many Rounds As Possible) of 10 push-ups, 10 sit-ups, and 10 squats!",
        "Hold a side plank for 3 minutes per side!",
        "Perform 100 jumping jacks and 100 mountain climbers without stopping!",
        "Sprint 50 meters, then do 20 push-ups. Repeat 5 times!",
        "Do 3 rounds of 25 burpees and 25 jump squats!",
        "Hold a squat position for 5 minutes!",
        "Perform 5 sets of 10 push-ups, 10 sit-ups, and 10 air squats—without resting between sets!",
        "Do a 4-minute Tabata (20 seconds of work, 10 seconds of rest) of squats and burpees!",
        "Complete 150 squats as fast as possible!",
        "Hold a 5-minute plank, with a 10-second rest after every 1 minute!",
        "Run for 30 minutes without stopping!",
        "Perform 100 push-ups, 50 sit-ups, and 25 burpees in one go!",
        "Hold a handstand for as long as you can (against a wall if needed)!",
        "Do 200 mountain climbers without stopping!",
        "Perform 3 rounds of 50 jumping jacks and 50 squats!",
        "Run up and down the stairs for 10 minutes non-stop!",
        "Hold a plank for 2 minutes, then immediately do 50 push-ups!",
        "Perform 3 rounds of 20 burpees and 30 air squats!",
        "Do 1-minute high-knees, then 1-minute jumping jacks—repeat for 5 rounds!",
        "Complete 100 step-ups (50 each leg) onto a bench or step!",
        "Hold a wall sit for as long as you can!",
        "Perform 10 minutes of non-stop bodyweight squats!",
        "Do 5 rounds of 10 push-ups, 10 burpees, and 10 lunges!",
        "Complete 100 push-ups and 100 squats in one go!",
        "Run a mile as fast as you can!",
        "Do 10 rounds of 30 seconds of burpees, followed by 30 seconds of rest!",
        "Hold a plank for 4 minutes straight!",
        "Perform 200 lunges as fast as possible!",
        "Do a 5-minute non-stop ab circuit: 1 minute each of crunches, leg raises, bicycle crunches, heel touches, and sit-ups!",
        "Complete 100 squat jumps without stopping!",
        "Run in place for 3 minutes, then do 25 burpees!",
        "Perform 5 rounds of 20 mountain climbers, 20 squats, and 20 push-ups!",
        "Hold a bridge position for 5 minutes!",
        "Do 150 jumping jacks as fast as possible!",
        "Perform 50 sit-ups, followed by 50 push-ups, and finish with 50 air squats!",
        "Do 3 rounds of 20 burpees and 20 lunges (10 per leg)!",
        "Run stairs for 15 minutes, as fast as possible!",
        "Hold a squat for 4 minutes straight, then do 50 squats!",
        "Complete 5 rounds of 10 burpees, 10 push-ups, and 10 jump squats!",
        "Hold a plank for 6 minutes, taking only 10-second breaks between each minute!"
    ]

    # Button to trigger a random Power Move
    if st.button("Power Move"):
        st.success("Bring on the pain!")
        # Randomly choose a challenge
        challenge = random.choice(challenges)
        st.write(f"**Today's Power Move:** {challenge}")
            
    if st.button("Generate Meal Plan!"):
        generated = True

    if generated == True:
        st.write("Generating...")
        age = st.session_state.profile["age"]
        height = st.session_state.profile["height"]
        weight = st.session_state.profile["weight"]
        gender = st.session_state.profile["gender"]
        body_goal = st.session_state.profile["body_goal"]
        one_rm_goal = st.session_state.profile["1mg"]
        six_rm_goal = st.session_state.profile["6mg"]
        twelve_rm_goal = st.session_state.profile["12mg"]
        exercises = st.session_state.profile["exercises"]

        # Properly format the string for the API call
        query = f"""
            Create an in-depth, personalized fitness plan based on the following parameters:
            Age: {age}, Height: {height}, Weight: {weight}, Gender: {gender}, 
            Body Goal: {body_goal} (Specify whether the goal is to lose weight, build muscle, improve endurance, tone the body, etc.),
            1-Rep Max Goal (1mg): {one_rm_goal} (Target weight the user wants to lift for one repetition in key exercises such as bench press, squat, or deadlift),
            6-Rep Max Goal (6mg): {six_rm_goal} (Target weight for a set of six repetitions),
            12-Rep Max Goal (12mg): {twelve_rm_goal} (Target weight for a set of twelve repetitions),
            Preferred Exercises: {exercises} (List any exercises or routines the user prefers to include, or highlight specific exercises like running, cycling, yoga, bench press, squats, etc.)
            
            The fitness plan should be designed to help the user reach their body goal and rep max targets over time, incorporating a balance of strength training and cardiovascular exercises.
            For each exercise, provide detailed workout sets, reps, rest periods, and progression tips. 
            Align the workout plan with the user’s fitness goals, tailoring specific muscle group exercises for strength, endurance, or hypertrophy.
            If information is incorrect or is missing do your best to just give them a workout plan based on their needs with the information provided. Do not discuss recovery strategies and supplementation, we will provide that information elsewhere.Only talk about important considerations that talk about the exercise aspect (Warm-up, Listen to your body, and Progressive overload.).Be as specific as possible for when it comes to cardio, static stretches and exercises. Add a time frame of about how long this workout will take for the level of difficulty they choose. Make sure every component gives an explicit stretch and exercise. They should not have to come up with their own stretches or exercisses.
        """

        # Call your ask_api function with the properly formatted query
        response = ask_api(query)
        st.write(response)
        collection.update_one(
            {"username": st.session_state.profile["username"]}, 
            {"$set": {"fitness_plan": response}}
        )