from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import torch
from utils import generate_hashtags, call_genai_caption,call_ollama
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")


def generate_caption_with_hashtags(image=None, description=None):
    captions = None
    if image:
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        base_caption = processor.decode(out[0], skip_special_tokens=True)
        prompt = f"Generate 5 creative and engaging Instagram captions based on this image caption:\n'{base_caption}'"
        captions = call_ollama(prompt)

    elif description:
        captions = call_genai_caption(description)
    if not captions:
        return ["unable to generate captions ."], None

    
    caption_list = [cap.strip("1234567890. ") for cap in captions.strip().split('\n') if cap.strip()]
    best_caption = caption_list[0] if caption_list else "No caption generated"
    

    hashtags = generate_hashtags(best_caption)
    return caption_list, hashtags


