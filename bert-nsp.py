from transformers import BertTokenizer, BertForNextSentencePrediction
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertForNextSentencePrediction.from_pretrained("bert-base-uncased")

prompt = "In Italy, pizza served in formal settings, such as at a restaurant, is presented unsliced."
next_sentence1 = "Guests can slice the pizza, add seasoning, and then enjoy a pleasant meal."
# next_sentence1 = "The sky is blue."
next_sentence2 = "Additionally, pasta with some light olive oil and salt can also be served as an side dish."
encoding1 = tokenizer(prompt, next_sentence1, return_tensors="pt")
encoding2 = tokenizer(prompt, next_sentence2, return_tensors="pt")

outputs1 = model(**encoding1, labels=torch.LongTensor([1]))
outputs2 = model(**encoding2, labels=torch.LongTensor([1]))
logits1 = outputs1.logits
logits2 = outputs2.logits

if logits1[0][0] > logits2[0][0]:
  print(prompt + " " + next_sentence1)
else:
  print(prompt + " " + next_sentence2)


#   Note: if logits [0, 0] < [0, 1], then sentence was random