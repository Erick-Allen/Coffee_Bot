#Chat Bot
def coffee_bot():
  print ("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print("Alright, that's a {} {}!".format(size, drink_type))

  extra_selection = extra_options()
  temperature = hot_or_cold()

  name = input("Can I get your name please? \n")

  print("Thanks {name}! Your {temp} {size} {drink} will be ready shortly."
  .format(name=name, temp=temperature, size=size, drink=drink_type))

  second_option = second_drink()

  if second_option == "a":
    size2 = get_size()
    drink_type2 = get_drink_type()
    extra_selection2 = extra_options()
    temperature2 = hot_or_cold()
    print("Alright, for your second drink we have here a {temp2} {size2} {drink2}."
    .format(temp2=temperature2, size2=size2, drink2=drink_type2))
  else:
    pass
  
  survey = survey_question()
  
  if survey == "Great":
    print("Thank you so much for the feedback {}, and come back soon!".format(name))
  elif survey == "ehh":
    print("Awww man how could we make it better?")
    get_feedback()
    print("Thank you for the feedback {}, we hope to see you again!".format(name))
  
#Gets size of drink
def get_size():
  res = input("What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ")

  if res == "a":
    return "small"
  elif res == "b":
    return "medium"
  elif res == "c":
    return "large"
  else:
    print_message()
    return get_size()

#Error message
def print_message():
  print ("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

#Gets what type of drink
def get_drink_type():
  res = input("What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")

  if res == "a":
    return "brewed coffee"
  elif res == "b":
    return "mocha"
  elif res == "c":
    return order_latte()
  else:
    print_message()
    return get_drink_type()

#Type of latte
def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n")

  if res == "a":
    return "latte"
  elif res == "b":
    return "non-fat latte"
  elif res == "c":
    return "soy latte"
  else:
    print_message()
    return order_latte()

# Cup options
def extra_options():
  res = input("What kind of cup would you like to use? \n[a] paper cup \n[b] plastic cup \n[c] reusuable cup \n")
  
  if res == "a":
    return "paper cup"
  elif res == "b":
    return "plastic cup"
  elif res == "c":
    return "reusuable cup"
  else:
    print_message()
    return extra_options()

#Temperature options
def hot_or_cold():
  res = input("Would you like your drink hot or cold? \n[a] Hot \n[b] Cold \n")

  if res == "a":
    return "Hot"
  elif res == "b":
    return "Cold"
  else:
    print_message()
    return hot_or_cold()

#Get a second drink
def second_drink():
  res = input("Is there anything else that I can get for you \n[a] Yes \n[b] No \n")
  if res == "a":
    return "a"
  elif res == "b":
    return "b"
    
  else:
    print_message()
    return second_drink()

#Questions about experience
def survey_question():
  res = input("Did you enjoy your expierence with Erick's coffee chat bot? \n[a] Yes!!! \n[b] Ehh \n")

  if res == "a":
    return "Great"
  elif res == "b":
    return "ehh"
  else:
    print_message()
    return survey_question()

#User input for feedback
def get_feedback():
  res = input("")

# Call coffee_bot()!
coffee_bot()