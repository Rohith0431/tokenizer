# Warning control
import warnings
from transformers import AutoTokenizer


warnings.filterwarnings("ignore")

models = [
    "bert-base-cased",
    "bert-base-uncased",
    "Xenova/gpt-4",
    "gpt2",
    "google/flan-t5-small",
    "bigcode/starcoder2-15b",
    "microsoft/Phi-3-mini-4k-instruct",
    "Qwen/Qwen2-VL-7B-Instruct",
]


def compare_models(sentence: str):

    for model in models:
        tokenizer = AutoTokenizer.from_pretrained(model)
        print(f"\n\nModel name: {model}")
        print(f"Length of vocabulary: {len(tokenizer)}")
        print(f"Token length: {len(tokenizer.tokenize(sentence))}")
        print(f"Tokens: {tokenizer.tokenize(sentence)}")
