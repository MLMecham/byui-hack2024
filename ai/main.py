from gemini import GeminiAI

# Test out if the class GeminiAi works or not
model_name = "gemini-1.5-pro"
fit_forge_ai = GeminiAI(model_name=model_name)

def start_chat():
    fit_forge_ai.generate_chat()

if __name__ == "__main__":
    ...
    # start_chat()
    # fit_forge_ai.single_message("Build me a lifting training for today, I'm 20 years old.")