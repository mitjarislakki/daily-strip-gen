import torch
from PIL import Image
from torchvision import transforms
from transformers import BertTokenizer, BertForImageCaptioning

# Load pre-trained image captioning model
model = BertForImageCaptioning.from_pretrained("bert-base-uncased")
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Define image preprocessing pipeline
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

# Load and preprocess the image
image_path = 'frameSet/2-1.jpg'
image = Image.open(image_path)
image = transform(image).unsqueeze(0)

# Generate image caption
with torch.no_grad():
    outputs = model.generate(
        input_images=image,
        max_length=50,  # Maximum length of the generated caption
    )

# Decode the generated caption
caption = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(caption)
