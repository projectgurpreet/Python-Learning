def get_required_input(promptMessage):
  while True:
    givenInput = input(promptMessage).strip()
    if givenInput:
        return givenInput
    else: print("It is required!! Plz Put in the Value")

