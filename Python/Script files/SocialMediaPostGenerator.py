# Social Media Post Generator
# A program that generates a social media post with customizable message, hashtags, and mentions.

'''Description: This program generates a social media post with a user's 
chosen message, hashtags, and mentions.'''

# Get user input
message = input("Enter your message: ")
hashtags = input("Enter hashtags (separated by spaces): ")
mentions = input("Enter mentions (separated by spaces): ")

# Create the social media post
post = f"🌟 New post! 🌟\n\n{message}\n\n# {hashtags}\n@{mentions}"

# Print the social media post
print("\nHere is your social media post:\n")
print(post)
