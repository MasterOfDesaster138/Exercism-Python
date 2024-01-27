def encode(data):
    if not data:
        return ""

    encoded = ""
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded += (str(count) if count > 1 else "") + data[i - 1]
            count = 1

    encoded += (str(count) if count > 1 else "") + data[-1]
    return encoded


def decode(encoded_data):
    if not encoded_data:
        return ""

    decoded = ""
    i = 0

    while i < len(encoded_data):
        count_str = ""
        while i < len(encoded_data) and encoded_data[i].isdigit():
            count_str += encoded_data[i]
            i += 1

        count = int(count_str) if count_str else 1
        char = encoded_data[i]
        decoded += count * char
        i += 1

    return decoded
