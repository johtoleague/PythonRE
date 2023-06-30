import struct

def sub_0(passed_in):
    assert len(passed_in) == 16, "Input must be a 16-byte string"

    # Convert passed_in to an array of bytes
    pass_in = bytearray(passed_in)

    # Define our 4-byte XOR key as an array of bytes
    hex_address = bytearray(struct.pack("I", 0x6F9CAEA4)) # 'I' is for unsigned int

    # Extract the least significant 8 bytes (as a little-endian 'q') and use it as an offset
    offset = struct.unpack_from('<q', passed_in)[0]

    # Calculate the start and end points of the range of bytes to be processed
    start = 8
    end = start + offset

    # Loop over each byte in the range
    for i in range(start, end):
        # XOR the byte with each byte in hex_address, and update the byte in pass_in
        for j in range(4): # 4 bytes in hex_address
            pass_in[i] ^= hex_address[j]

    # Return the byte array
    return pass_in

# Here is your input:
input_hex = "9f95989ec4c09d9f9a9f9ccaca9ad49fcf9ac8d4cdc9cdccd49b989acad4caca0cecec9caca9fcfc89a"
input_bytes = bytes.fromhex(input_hex)  
 # Remove spaces and convert to bytes

# We apply the function to each 16-byte block of the input:
blocks = [input_bytes[i:i+16] for i in range(0, len(input_bytes), 16)]
output_bytes = b''.join(sub_0(block) for block in blocks)

# Print the result as a hex string:
print(output_bytes.hex())
