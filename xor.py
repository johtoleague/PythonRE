def sub_0(passed_in):
    hex_key = 0x6F9CAEA4
    hex_key_bytes = hex_key.to_bytes(4, 'little')  # Convert to bytes assuming little-endian

    # Convert passed_in into bytes and slice off the last half
    passed_in_bytes = passed_in.to_bytes(16, 'little')[:8]  

    # Determine the length of passed_in_bytes
    length = int.from_bytes(passed_in_bytes[:8], 'little')

    # Initialize the_pass_in_value as a bytearray for mutable operations
    the_pass_in_value = bytearray(passed_in_bytes)

    # Perform XOR operation
    for i in range(length):
        for j in range(4):
            the_pass_in_value[i] ^= hex_key_bytes[j]

    # Convert back to int and return
    result = int.from_bytes(the_pass_in_value, 'little')
    return result



hex_input = 0x9f95989ec4c09d9f9a9f9ccaa9ad49fcf9ac8d4cdc9cdccd49b989acd4cacad0cecec9cac99fcfc89a
#key = "4321"

encrypted = sub_0(hex_input)
print("Encrypted: ", encrypted)