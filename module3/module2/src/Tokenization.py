import warnings
warnings.filterwarnings('ignore')

from transformers import AutoTokenizer

sentence = "Hello World!!"
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
tokens = tokenizer(sentence)
token_ids = tokenizer(sentence).input_ids
print("Tokens: ", tokens)
print("Token IDs: ", token_ids) 

for i in token_ids:
    print(tokenizer.decode(i))