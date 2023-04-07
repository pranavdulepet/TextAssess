from transformers import AutoTokenizer, AutoModel
from sklearn.metrics.pairwise import cosine_similarity
from termcolor import colored
import numpy as np
import torch

# Load Sentence-BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "sentence-transformers/bert-base-nli-mean-tokens")
model = AutoModel.from_pretrained(
    "sentence-transformers/bert-base-nli-mean-tokens")


def highlight_errors(prompt_tokens, response_tokens):

    # Find the index of the first token in the response that does not match the prompt
    error_index = len(prompt_tokens)
    for i in range(len(prompt_tokens)):
        if i >= len(response_tokens) or prompt_tokens[i] != response_tokens[i]:
            error_index = i
            break

    # Highlight incorrect parts of the response
    highlighted_response = ''
    for i, token in enumerate(response_tokens):
        if i < error_index:
            highlighted_response += token + ' '
        else:
            highlighted_response += colored(token + ' ', 'red')

    return highlighted_response


def identify_improvements(prompt, response, similarity_threshold=0.7):
    # Tokenize the prompt and response
    prompt_tokens = tokenizer(
        prompt, return_tensors='pt', padding=True, truncation=True)['input_ids']
    response_tokens = tokenizer(
        response, return_tensors='pt', padding=True, truncation=True)['input_ids']

    prompt_embeddings = model(prompt_tokens)[0].mean(dim=1)
    response_embeddings = model(response_tokens)[0].mean(dim=1)

    similarity = cosine_similarity(prompt_embeddings.detach(
    ).numpy(), response_embeddings.detach().numpy())[0][0]

    # Identify the parts of the response that do not match the prompt
    prompt_tokens = tokenizer.tokenize(prompt)
    response_tokens = tokenizer.tokenize(response)
    error_index = len(prompt_tokens)
    for i in range(len(prompt_tokens)):
        if i >= len(response_tokens) or prompt_tokens[i] != response_tokens[i]:
            error_index = i
            break
    error_part = " ".join(response_tokens[error_index:])

    highlighted_response = highlight_errors(prompt_tokens, response_tokens)

    return similarity, error_part, highlighted_response


prompt = "Who is Barack Obama?"
response = '''
Barack Obama was the 44th president.
'''

similarity, error, highlight_response = identify_improvements(
    prompt, response)

if similarity >= 0.7:
    print("\nThe response is similar to the prompt.")
else:
    print("\nThe response is not similar to the prompt.")
    print(f"\nError: {error}")
    print("\nHighlighted response: ", highlight_response)
