#firstly starting with the input function to input user values and use strip function so to split it up
email_id=input("enter your email id").strip()

# next process the user have to enroll or input the username
username=email_id[:email_id.index('@')]

# here we have the domain
domain=email_id[email_id.index('@')+1:]

# so now we have the username and domain and slice it up at the "@"

print(f"your username is {username} and your domain is {domain}")

#so this is how the process run