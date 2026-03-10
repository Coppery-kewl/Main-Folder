# Receipt maker 1.1
version='1.1'

print(f"""Hello, welcome to receipt maker {version}
      to make your receipt, answer these questions.
      leave blank and/or just click ENTER if any of the information is not issued""")
name=input("What is the name of the consumer/customer? Ans: ")
id=input("Give order/receipt number/id. Ans: ")
item=input("Give item or service name. Ans: ")
date=input("Give the date. Ans: ")
company=input("Give the company/issuer name. (Can be your name, shop name, etc) Ans: ")
price=input("Give the price payed or to be payed. (Can be free) Ans: ")
thanknote=input("Write a thanks note like 'Thank you for shopping at our establishment, have a great day :-)', etc. Ans: ")

print(fr"""-----------------------------RECEIPT-----------------------------
      -------------------
      !`````:::::::`````! Issued by: {company}
      !````//```````````! No. {id}
      !```//````````````! Name: {name}
      !``||`````````````! Service/Order: {item}
      !```\\````````````! Price: {price}
      !````\\```````````! Date: {date}
      !`````:::::::`````! {thanknote}
      -------------------""")
