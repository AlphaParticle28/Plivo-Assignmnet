import json
import random

# Sample data pools
first_names = ["rohan", "priya", "amit", "sneha", "rahul", "anjali", "vikram", "pooja", "arjun", "divya", 
               "karan", "neha", "aditya", "riya", "sanjay", "kavya", "manish", "shreya", "deepak", "meera",
               "raj", "nisha", "varun", "tanya", "akash", "simran", "nitin", "swati", "harsh", "preeti",
               "gaurav", "ananya", "mohit", "ishita", "naveen", "kritika", "sandeep", "madhuri", "kunal", "sakshi"]

last_names = ["mehta", "sharma", "patel", "kumar", "singh", "gupta", "verma", "reddy", "iyer", "khan",
              "das", "nair", "rao", "joshi", "chopra", "malhotra", "agarwal", "desai", "shah", "pillai",
              "bose", "kapoor", "chauhan", "pandey", "mishra", "trivedi", "saxena", "bhatt", "menon", "shetty"]

email_domains = ["gmail dot com", "yahoo dot com", "hotmail dot com", "outlook dot com", "rediffmail dot com",
                 "protonmail dot com", "icloud dot com", "aol dot com", "zoho dot com", "mail dot com"]

cities = ["delhi", "mumbai", "bangalore", "chennai", "kolkata", "hyderabad", "pune", "ahmedabad", "jaipur", "lucknow",
          "kanpur", "nagpur", "indore", "bhopal", "patna", "chandigarh", "ludhiana", "agra", "vadodara", "kochi"]

streets = ["m g road", "nehru street", "gandhi nagar", "park avenue", "ring road", "station road", "main street",
           "lake view road", "residency road", "commercial street", "church street", "brigade road", "silk board"]

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

# Template functions
def generate_credit_card():
    """Generate a credit card number in spelled-out format"""
    card = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    # Format as groups of 4
    parts = [card[i:i+4] for i in range(0, 16, 4)]
    return ' '.join(parts)

def generate_phone():
    """Generate a phone number"""
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

def generate_date():
    """Generate a date"""
    day = random.randint(1, 28)
    month = random.choice(months)
    year = random.randint(1990, 2025)
    return f"{day} {month} {year}"

# Dataset generation templates
templates = []

def template_email():
    first = random.choice(first_names)
    last = random.choice(last_names)
    domain = random.choice(email_domains)
    
    patterns = [
        f"reach me at {first} dot {last} at {domain}",
        f"you can email me at {first} underscore {last} at {domain}",
        f"my email is {first} {last} at {domain}",
        f"contact {first} dot {last} at {domain}",
        f"send message to {first} {last} at {domain}",
        f"email address is {first} underscore {last} at {domain}",
        f"write to me at {first} dot {last} at {domain}",
        f"my id is {first} {last} at {domain}",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    # Find email start (first occurrence of first name)
    email_start = text.find(first)
    email_end = text.find(domain) + len(domain)
    entities.append({"start": email_start, "end": email_end, "label": "EMAIL"})
    
    return text, entities

# Template 2: Phone only
def template_phone():
    phone = generate_phone()
    first = random.choice(first_names)
    
    patterns = [
        f"call me on {phone}",
        f"my phone number is {phone}",
        f"you can reach me at {phone}",
        f"mobile number {phone}",
        f"contact number is {phone}",
        f"phone is {phone}",
        f"dial {phone} to reach me",
        f"{first} phone number {phone}",
        f"my mobile is {phone}",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    # Find phone
    phone_start = text.find(phone)
    phone_end = phone_start + len(phone)
    entities.append({"start": phone_start, "end": phone_end, "label": "PHONE"})
    
    # Find name if present
    if first in text and text.find(first) < phone_start:
        name_start = text.find(first)
        name_end = name_start + len(first)
        entities.append({"start": name_start, "end": name_end, "label": "PERSON_NAME"})
    
    return text, entities

# Template 3: Person name only
def template_person_name():
    first = random.choice(first_names)
    last = random.choice(last_names)
    
    patterns = [
        f"my name is {first} {last}",
        f"i am {first} {last}",
        f"this is {first} {last}",
        f"call me {first} {last}",
        f"{first} {last} speaking",
        f"you can call me {first} {last}",
        f"i go by {first} {last}",
        f"the name is {first} {last}",
        f"myself {first} {last}",
        f"{first} {last} here",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    # Find name
    name_start = text.find(first)
    name_end = text.find(last) + len(last)
    entities.append({"start": name_start, "end": name_end, "label": "PERSON_NAME"})
    
    return text, entities

# Template 4: Credit card
def template_credit_card():
    card = generate_credit_card()
    first = random.choice(first_names)
    last = random.choice(last_names)
    
    patterns = [
        f"my credit card number is {card}",
        f"card details are {card} name {first} {last}",
        f"the card number is {card}",
        f"please charge {card}",
        f"use card {card} for payment",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    card_start = text.find(card)
    card_end = card_start + len(card)
    entities.append({"start": card_start, "end": card_end, "label": "CREDIT_CARD"})
    
    if first in text:
        name_start = text.find(first)
        name_end = text.find(last) + len(last)
        entities.append({"start": name_start, "end": name_end, "label": "PERSON_NAME"})
    
    return text, entities

# Template 5: Address
def template_address():
    street = random.choice(streets)
    city = random.choice(cities)
    pincode = ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    patterns = [
        f"i live at {street} {city} {pincode}",
        f"my address is {street} in {city} pincode {pincode}",
        f"ship to {street} {city} pin {pincode}",
        f"address is {street} near {city} {pincode}",
        f"deliver at {street} {city} postal code {pincode}",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    addr_start = text.find(street)
    addr_end = text.find(pincode) + len(pincode)
    entities.append({"start": addr_start, "end": addr_end, "label": "ADDRESS"})
    
    return text, entities

# Template 6: Date of birth
def template_dob():
    date = generate_date()
    first = random.choice(first_names)
    
    patterns = [
        f"my date of birth is {date}",
        f"i was born on {date}",
        f"{first} birthday is {date}",
        f"dob is {date}",
        f"born {date}",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    if first in text:
        name_start = text.find(first)
        name_end = name_start + len(first)
        entities.append({"start": name_start, "end": name_end, "label": "PERSON_NAME"})
    
    date_start = text.find(date.split()[0])
    date_end = text.find(date.split()[-1]) + len(date.split()[-1])
    entities.append({"start": date_start, "end": date_end, "label": "DATE_OF_BIRTH"})
    
    return text, entities


# Template 7: Multiple entities
def template_complex():
    first = random.choice(first_names)
    last = random.choice(last_names)
    phone = generate_phone()
    email_domain = random.choice(email_domains)
    city = random.choice(cities)
    date = generate_date()
    street = random.choice(streets)
    card = generate_credit_card()
    
    patterns = [
        # Name + Phone + City
        f"i am {first} {last} from {city} call me at {phone}",
        f"contact person is {first} {last} mobile {phone} city {city}",
        f"{first} {last} visiting {city} contact {phone}",
        f"this is {first} {last} you can reach me on {phone} i am in {city}",
        f"hi my name is {first} {last} phone number {phone} location {city}",
        
        # Name + Email + Phone
        f"{first} {last} email {first} at {email_domain} phone {phone}",
        f"reach {first} {last} at {first} dot {last} at {email_domain} or call {phone}",
        f"i am {first} {last} my email is {first} underscore {last} at {email_domain} mobile {phone}",
        f"contact details for {first} {last} email {first} {last} at {email_domain} phone {phone}",
        
        # Name + Date + City
        f"my name is {first} {last} i will be in {city} on {date}",
        f"{first} {last} traveling to {city} on {date}",
        f"hi i am {first} {last} arriving {city} {date}",
        f"{first} {last} scheduled visit to {city} date {date}",
        
        # Name + Phone + Email
        f"you can contact {first} {last} phone {phone} email {first} at {email_domain}",
        f"{first} {last} here call {phone} or write to {first} dot {last} at {email_domain}",
        f"for {first} {last} dial {phone} or email {first} underscore {last} at {email_domain}",
        
        # Name + Address + Phone
        f"{first} {last} lives at {street} {city} phone {phone}",
        f"deliver to {first} {last} address {street} {city} contact {phone}",
        f"ship to {first} {last} at {street} in {city} call {phone}",
        
        # Name + Card + Phone
        f"cardholder {first} {last} number {card} phone {phone}",
        f"credit card {card} belongs to {first} {last} contact {phone}",
        
        # Complex combinations
        f"passenger details {first} {last} phone {phone} email {first} at {email_domain} traveling to {city}",
        f"booking for {first} {last} contact {phone} destination {city} date {date}",
        f"customer {first} {last} mobile {phone} address {street} {city}",
        f"registration details name {first} {last} email {first} dot {last} at {email_domain} phone {phone} city {city}",
        f"profile for {first} {last} located in {city} phone {phone} email {first} underscore {last} at {email_domain}",
        f"{first} {last} from {city} phone number {phone} visiting on {date}",
        f"delivery to {first} {last} address {street} {city} mobile {phone} date {date}",
    ]
    
    text = random.choice(patterns)
    entities = []
    
    # Find person name
    name_start = text.find(first)
    name_end = text.find(last) + len(last)
    entities.append({"start": name_start, "end": name_end, "label": "PERSON_NAME"})
    
    # Find phone
    if phone in text:
        phone_start = text.find(phone)
        phone_end = phone_start + len(phone)
        entities.append({"start": phone_start, "end": phone_end, "label": "PHONE"})
    
    # Find email
    if email_domain in text:
        # Find the email start (after the name mention)
        email_start = text.find(first, name_end)
        if email_start == -1:  # If not found after name, search from beginning but skip name
            words = text.split()
            for i, word in enumerate(words):
                if first in word and i > 0 and words[i-1] in ['email', 'at', 'write', 'to']:
                    email_start = text.find(word, name_end)
                    break
        email_end = text.find(email_domain) + len(email_domain)
        if email_start != -1:
            entities.append({"start": email_start, "end": email_end, "label": "EMAIL"})
    
    # Find date
    if date.split()[0] in text:
        date_start = text.find(date.split()[0])
        date_end = text.find(date.split()[-1]) + len(date.split()[-1])
        entities.append({"start": date_start, "end": date_end, "label": "DATE"})
    
    # Find address (street + city combination)
    if street in text and city in text:
        addr_start = text.find(street)
        addr_end = text.find(city) + len(city)
        entities.append({"start": addr_start, "end": addr_end, "label": "ADDRESS"})
    elif city in text and street not in text:
        # Just city mentioned without street
        city_start = text.find(city)
        city_end = city_start + len(city)
        entities.append({"start": city_start, "end": city_end, "label": "LOCATION"})
    
    # Find credit card
    if card in text:
        card_start = text.find(card)
        card_end = card_start + len(card)
        entities.append({"start": card_start, "end": card_end, "label": "CREDIT_CARD"})
    
    return text, entities

# Generate dataset
dataset = []
template_functions = [
    template_phone,
    template_person_name,
    template_email,
    template_credit_card,
    template_address,
    template_dob,
    template_complex
]

iters = 100

for i in range(iters):
    template_func = random.choice(template_functions)
    try:
        text, entities = template_func()
        
        # Sort entities by start position
        entities = sorted(entities, key=lambda x: x["start"])
        
        entry = {
            "id": f"utt_{i+1:04d}",
            "text": text,
            "entities": entities
        }
        dataset.append(entry)
    except Exception as e:
        print(f"Error generating entry {i}: {e}")
        continue

# Write to JSONL file
output_file = r"C:\Users\deban\Desktop\7th Sem\Interview Prep\pii_ner_assignment 2\pii_ner_assignment\data\train.jsonl"
with open(output_file, 'w', encoding='utf-8') as f:
    for entry in dataset:
        f.write(json.dumps(entry) + '\n')


print(f"Generated {len(dataset)}")
print(f"Dataset saved to {output_file}")