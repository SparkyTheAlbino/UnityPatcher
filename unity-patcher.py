import binascii
import time

u_path = 'Unity.exe' # Unity path, Local only #TODO Add in default/detect path
op_path = 'Unity-Patched.exe' # Output binary #TODO Make this configurable

orig_hex = "84C0750833C04883C4205BC38B034883C4205BC3" # Hex string in original binary
rep_hex = "84C0740833C04883C4205BC38B034883C4205BC3"  # Hex string to replace with

# Load binary to memory
with open(u_path, "rb") as in_file:
    in_hex = binascii.hexlify(in_file.read()).decode('utf-8').upper() # Read file in as Hex

if x > 0:
    in_hex = in_hex.replace(orig_hex, rep_hex) # Apply Patch
    in_hex = binascii.unhexlify(in_hex.encode('utf-8')) # Convert the Hex back into a byte objects
    with open(op_path, 'wb') as out_file: # Write the bytes to the output binary
        out_file.write(in_hex)
    print("Patching complete. Please replace your uniy.exe with the patched version")
else:
    print("Binary already patched")