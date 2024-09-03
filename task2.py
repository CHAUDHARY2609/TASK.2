import random
import string
def generate_password(length):
if length < 4:
raise ValueError("Password length must be at least 4 characters long.")
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
special = string.punctuation
password = [
random.choice(lower),
random.choice(upper),
random.choice(digits),
random.choice(special)
]
all_characters = lower + upper + digits + special
password += [random.choice(all_characters) for _ in range(length - 4)]
random.shuffle(password)
return ''.join(password)
def main():
print("Password Generator")
while True:
try:
length = int(input("Enter the desired length of the password: "))
if length < 4:
print("Password length must be at least 4 characters long.")
continue
password = generate_password(length)
print(f"Generated Password: {password}")
break
except ValueError:
print("Invalid input. Please enter a numerical value.")
if __name__ == "__main__":
main()
