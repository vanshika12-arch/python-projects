import validators

print("=== Phishing Detection Chatbot ===")
print("Enter a website link to check if it may be phishing.")
print("Type 'exit' to stop.\n")

while True:

    url = input("You: ")

    if url.lower() == "exit":
        print("Bot: Goodbye!")
        break

    # Check if URL format is valid
    if not validators.url(url):
        print("Bot: ❌ This is not a valid URL.\n")
        continue

    # Simple phishing checks
    if "@" in url:
        print("Bot: ⚠ Warning! '@' found in URL → Possible phishing.\n")

    elif "-" in url:
        print("Bot: ⚠ Suspicious domain detected ('-').\n")

    elif "login" in url or "verify" in url or "bank" in url or "secure" in url:
        print("Bot: ⚠ This link contains suspicious words → Possible phishing.\n")

    elif len(url) > 75:
        print("Bot: ⚠ URL is very long → Could be phishing.\n")

    else:
        print("Bot: ✅ This link looks safe.\n")