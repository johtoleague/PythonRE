def xor_encrypt(hex_input, key):
    
    input_bytes = bytearray.fromhex(hex_input)

    
   
    key = bytearray.fromhex(key)
        
    print(key)

    key_length = len(key)

    
    for i in range(len(input_bytes)):
        input_bytes[i] ^= key[i % key_length]

   
    encrypted = input_bytes.hex()

    return encrypted


hex_input = "9f95989ec4c09d9f9a9f9ccaa9ad49fcf9ac8d4cdc9cdccd49b989acd4cacad0cecec9cac99fcfc89a"
#key = "4321"
key = "A4AE9C6F" 
# "A4AE9C6F" "6F9CAEA4"
print("Key: ", key)
encrypted = xor_encrypt(hex_input, key)
print("Encrypted: ", encrypted)