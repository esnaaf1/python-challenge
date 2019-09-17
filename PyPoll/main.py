#main.pay in PyPoll
candidates = {'name': [] ,'votes': []}

answer= "y"
votes = 0
while answer =="y":
    candidate = input("Enter the Candidate Name:  ")

    print(f" from the keyboard{ candidate}")

    list1 = candidates['name']
    if candidate in list1:
        found = True
        list2 = candidates['votes']
        candidate_num = list1.index(candidate)
        list2[candidate_num] = list2[candidate_num]+ 1 
        print(f" {found}")
        print(f"votes {votes}")
        candidates.update({'votes': list2})
        print(f" dic. {candidates}")
    else:
        found = False
        votes = 1
        print(f" {found}")
        candidates['name'].append(candidate)
        candidates['votes'].append(votes)
        print(f" dic. {candidates}")
    answer = input("Do you want to add another Candidate? y(es) or n(o)? ")
print(f" candidates { candidates}")