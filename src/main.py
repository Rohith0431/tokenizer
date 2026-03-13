from tokenizer_visualization import show_tokens
from tokenizer_comparision import compare_models

text = """
English and CAPITALIZATION
🎵 鸟
show_tokens False None elif == >= else: two tabs:"    " Three tabs: "       "
12.0*50=600
"""


# function to show the menu
def show_models() -> None:
    print("\n==============================")
    print(" Personal Expense Tracker")
    print("==============================")
    print("bert-base-cased")
    print("bert-base-uncased")
    print("Xenova/gpt-4")
    print("gpt2")
    print("google/flan-t5-small")
    print("bigcode/starcoder2-15b")
    print("microsoft/Phi-3-mini-4k-instruct")
    print("Qwen/Qwen2-VL-7B-Instruct")
    print("==============================")


def main() -> None:

    sentence = input("Enter the text to tokenize: ").strip()
    if len(sentence) == 0:
        print("As no text entered to tokenize, assigning the default text")
        sentence = text

    compareModel = input(
        "Press Enter key to continue to enter text or insert 1 to compare the models with given or default text: "
    ).strip()

    if int(compareModel) == 1:
        compare_models(sentence)
        return

    show_models()

    model = input(
        "Enter the model you want to tokenize the text from the list shown: "
    ).strip()

    if len(model) == 0:
        print(
            "As no model is entered to tokenize, assigning the default model 'bert-base-cased'"
        )
        model = "bert-base-cased"

    show_tokens(sentence, model)


if __name__ == "__main__":
    main()
