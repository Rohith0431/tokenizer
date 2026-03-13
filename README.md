# Tokenizer Project

## This project is a small CLI playground for exploring and comparing Trained LLM tokenizers.

It lets you enter any text (or use the built-in sample that includes capitalization, Unicode, whitespace, and operators), then:

- Tokenize with a selected model via transformers.AutoTokenizer.from_pretrained(...).
- Print the tokenizer’s vocabulary size, the token strings (tokenizer.tokenize(...)), and the token IDs.
- Visualize the tokenization in the terminal by decoding each token ID and printing it with alternating ANSI background colors (so you can see token boundaries at a glance).


It also includes a “compare models” mode that runs the same input through a predefined list of model tokenizers and prints, per model, the vocab size, number of tokens, and the token list—useful for seeing how tokenization differs across models like BERT/GPT/T5-style tokenizers.

Note: the first run will download tokenizer files for the chosen model(s) (internet required), and the color output depends on terminal ANSI/truecolor support.