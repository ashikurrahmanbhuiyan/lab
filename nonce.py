import hashlib

def solve_puzzle(String, leading_zeroes):
    nonce = 0
    while True:
        nonce_str = str(nonce)
        data = String + nonce_str
        hash = hashlib.sha256(data.encode()).hexdigest()
        if hash[:leading_zeroes] == '0' * leading_zeroes:
            return nonce, hash
        nonce += 1

input_string = input("Enter the string: ")
input_zeroes = int(input("Enter the number of leading zeroes: "))

nonce_value, hash_result = solve_puzzle(input_string, input_zeroes)

print("Input String: ", input_string)
print("Nonce: ", nonce_value)
print("Hash: ", hash_result)