# List of feedback emails
feedback_mail = [
    "akasnsha.gupta@sify.com", "deepak.sharam@sify.com", "karan.bhatia@sify.com", 
    "sarah.baswa@sify.com", "raveesh.bhatt@sify.com", "sheeta;@hotmail.com",
    "jatin.sai@saidata.com", "kindly.maggy@colt.net", "prashun.das@sify.com"
]

# Lists to store categorized emails
sify_list = []
non_sify_list = []

# Categorizing emails
for email in feedback_mail:
    if email.endswith("@sify.com"):  # Removed unnecessary parentheses
        sify_list.append(email)
    else:
        non_sify_list.append(email)

# Display results
print("List of mail IDs from Sify:")
print(sify_list)
print("\nList of mail IDs not from Sify:")
print(non_sify_list)
