import hashlib

#text = 'Hello, world!'
#hash_object = hashlib.sha256(text.encode())
#hash_digest = hash_object.hexdigest()
#print (f"SHA Hash of",text, "is ",hash_digest,)

def hash_file(file_path):
    h=hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True:
            chunk= file.read(1024)
            if chunk== b"":
                break
            h.update(chunk)
    return h.hexdigest()

def verify_integrity(file1, file2):
    hash1= hash_file(file1)
    hash2= hash_file(file2)
    print("\nChecking integrity between", file1, "and", file2)
    if hash1 == hash2:
        return "File is intact. No modification have been made"
  
    return "File has been modified. Probably unsafe."


if __name__== "__main__":
    print ("SHA Hash of file is:", hash_file(r"CYBER_TOOLKIT\sample_files\sample.txt"))
    print (verify_integrity(r"C:\Users\Name\Python\filename\sample_files\file1.png", r"C:\Users\Name\Python\filename\sample_files\file3.png"))
    print (verify_integrity(r"C:\Users\Name\Python\filename\sample_files\file1.png" , r"C:\Users\Name\Python\filename\sample_files\file2.png"))
