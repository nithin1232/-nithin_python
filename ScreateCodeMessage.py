# write a python program to translate a message into secret language use the rules below to translate normal english into secret language
# coding :
# if the word contains at least 3 characters remove the first letter and append it at  the end
# now append 3 random character at the end starting and the end
# else :
# simply reverse the string
# decoding :
# if the world contains less than 3 characters reverse it
# else:
# remove 3 random characters from start  and end now remove the last letter and append it to the beginning
import random
import string

# data = input("Enter the elements : ")
#
# coding = True
# if(coding):
#     for word in words :
#         if len(data) >= 3:
#             r1 = "hjv"
#             r2 = "sad"
#             newdata = r1 + data[1:] + data[0] + r2
#             print(newdata)


st = input("enter  the elements:")
words = st.split(" ")
coding = False
if(coding):
    nwords = []
    for word in words :
        if (len(word)>=3):
            r1 =''.join(random.choices(string.ascii_lowercase, k=3))
            r2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            stnew = r1 +word[1:] +word[0] +r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
else:
    nwords = []
    for word in words :
        if (len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print(" ".join(nwords))
