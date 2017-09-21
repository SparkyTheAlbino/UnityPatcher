import binascii
import time

changes = 0

u_path = 'Unity.exe'
op_path = 'Unity-Patched.exe'

orig_hex = "84C0750833C04883C4205BC38B034883C4205BC3"
rep_hex = "84C0740833C04883C4205BC38B034883C4205BC3"

# Load binary to memory
with open(u_path, "rb") as in_file:
    in_bytes = binascii.hexlify(in_file.read()).decode('utf-8').upper()

# Search for hex
x = in_bytes.count(orig_hex)
print(x)

if x > 0:
    # Write Patch
    in_bytes = in_bytes.replace(orig_hex, rep_hex)
    x = in_bytes.count(orig_hex)
    print(x)

    # Write back to file
    in_bytes = binascii.unhexlify(in_bytes.encode('utf-8'))
    with open(op_path, 'wb') as out_file:
        out_file.write(in_bytes)

    print("Patching complete. Please replace your uniy.exe with the patched version")
    time.sleep(3)
else:
    print("Binary already patched")
    time.sleep(3)