import re

def validation(userInput):
    regex_ph = r'\(?\+?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    matches =  re.match(regex_ph,userInput) 
     
    return matches    



if __name__ == '__main__':

    user_input =input("")
    valid =validation(user_input)

    if valid :
        
        if valid.group() == user_input:
            print(f"valid number:"+ valid.group())
        else:
            print("not valid") 
               






