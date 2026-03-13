# Warning control
import warnings
from transformers import AutoTokenizer


warnings.filterwarnings("ignore")


colors = [
    "72;209;204",
    "65;105;225",
    "139;0;139",
    "176;196;222",
    "255;235;205",
    "255;20;147",
]


def show_tokens(sentence: str, name_of_tokenizer: str):
    tokenizer = AutoTokenizer.from_pretrained(name_of_tokenizer)
    token_ids = tokenizer(sentence).input_ids

    print(f"Length of vocabulary: {len(tokenizer)}")
    print(tokenizer.tokenize(sentence))
    print(token_ids)

    for idx, t in enumerate(token_ids):
        print(
            f"\x1b[0;30;48;2;{colors[idx % len(colors)]}m"
            + tokenizer.decode(t)
            + "\x1b[0m",
            end=" ",
        )
