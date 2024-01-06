"""
    Commands:
    00001: "wink",
    00010: "double blink",
    00100: "close your eyes",
    01000: "jump",
    10000: "Reverse the order of the operations in the secret handshake"
"""


def commands(binary_str):
    commands = ["wink", "double blink", "close your eyes", "jump", "Reverse the order of the operations in the secret handshake"]
    binary_numbers = list(binary_str)
    actions = []
    
    if len(binary_numbers) == 5:
        for i in range(5):
            number = binary_numbers.pop()
            action = commands.pop(0)
            if number == '1':
                if "Reverse the order of the operations in the secret handshake" == action:
                    actions.reverse()
                else:
                    actions.append(action)
    return actions

