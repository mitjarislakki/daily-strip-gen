from transformers import BertTokenizer, BertModel #pip install transformers --user
import torch #pip install torch --user
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Load FinBERT tokenizer
tokenizer = BertTokenizer.from_pretrained('TurkuNLP/bert-base-finnish-cased-v1')

def preprocess_text(text):
    # Tokenize the text
    tokenized_text = tokenizer.encode(text, add_special_tokens=False)
    # Convert token IDs to strings
    processed_text = tokenizer.decode(tokenized_text)
    return processed_text

# Example input sentence
input_sentence = "mikäköhän YLLÄTYS\nNÄISSÄ ON."
processed_input = preprocess_text(input_sentence)

# Example list of predefined sentences
#tähän sit tiedoston luku:
csv_file = 'computerVision.csv'
df = pd.read_csv(csv_file)
predefined_sentences =  df['texts'].tolist()

result_dict = dict(zip(df['texts'], df['img']))

# Preprocess each sentence in the predefined list
processed_predefined_sentences = [preprocess_text(sentence) for sentence in predefined_sentences]

# Load pre-trained FinBERT model
model = BertModel.from_pretrained('TurkuNLP/bert-base-finnish-cased-v1')

# Encode input and predefined sentences
with torch.no_grad():
    input_ids = tokenizer(processed_input, return_tensors='pt')['input_ids']
    predefined_ids = tokenizer(processed_predefined_sentences, return_tensors='pt', padding=True, truncation=True)['input_ids']
    input_embeddings = model(input_ids)[0].mean(dim=1)  # Mean pooling over token embeddings for input sentence
    predefined_embeddings = model(predefined_ids)[0].mean(dim=1)  # Mean pooling over token embeddings for predefined sentences

# Calculate cosine similarity
similarity_scores = cosine_similarity(input_embeddings, predefined_embeddings)

# Find the index of the most similar predefined sentence
best_match_index = similarity_scores.argmax()

# Get the best matching predefined sentence
best_match_sentence = predefined_sentences[best_match_index]

print("Input Sentence:", input_sentence)
print("Best Match:", best_match_sentence)
