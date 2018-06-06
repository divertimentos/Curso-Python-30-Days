import datetime
default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are excited about using it. Just as a
reminder the purchase total was ${total}.
Wave a great one!

Team CFE
"""


def make_messages(names, amounts):

    messages = []
    if len(names) == len(amounts):
        i = 0
        for name in names:
            new_msg = unf_message.format(
                name=name,
                date="some date",
                total=amounts[i]
            )
            i += 1
            print(new_msg)


make_messages(default_names, default_amounts)
