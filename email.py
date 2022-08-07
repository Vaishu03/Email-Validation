email = input("Enter your email:")# w@w.in or w@w.com

a,b,c = 0,0,0
if len(email)>=6:
  if email[0].isalpha():
    if ('@' in email) and (email.count('@')==1):
      if (email[-4] == '.') ^ (email[-3] == '.'):
        for i in email:
          if i == i.isspace():
            a = 1
          elif i.isalpha():
            if i == i.upper():
              b = 1
          elif i.isdigit():
            continue
          elif i == "_" or i == "." or i == "@":
            continue
          else:
            c = 1

        if a == 1 or b == 1 or c == 1:
          print("Invalid email ID")
        else:
          print("Valid email ID")
      else:
        print("Invalid email ID")
    else:
      print("Invalid email ID")
  else:
    print("Invalid email ID")
else:
  print("Invalid email ID")