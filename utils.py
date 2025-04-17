import subprocess

def call_ollama(prompt, model="mistral"):
    command = [
        "ollama", "run", model
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate(input=prompt.encode())

    return output.decode().strip()



def call_genai_caption(description):
    prompt = f"""
    Generate 5 different creative and engaging Instagram captions for this description:
    \"{description}\"
    
    Each caption should be:
    - Short and catchy
    - Suitable for an Instagram post
    - In a different tone (funny, poetic, aesthetic, adventurous, etc.)

    Output captions as a numbered list.
    """
    return call_ollama(prompt)
    

def generate_hashtags(caption):
    prompt = f"Based on these caption: '{caption}', generate up to 10 trending and relevant Instagram-style hashtags."
    return call_ollama(prompt)




