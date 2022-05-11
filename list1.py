otal_dictionary = {}

while True:
    question = input("Enter your question : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("Enter your reply : ")
    total_dictionary[i] = answer
print(total_dictionary)