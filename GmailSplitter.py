# Get the user's Gmail and split it into username and domain parts
email = input("Enter your Gmail: ")

# Find the index of '@' to separate username and domain
index = email.index("@")

# Extract the username and domain from the email
username = email[:index]
domain = email[index+1:]

# Print the extracted username and domain
print(f"Your username is {username}\nAnd your domain is {domain}")
