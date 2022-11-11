from datetime import date

f_date = list()
s_date = list()

f = input("Enter fiest Date: ")
s = input("Enter seccond Date: ")



f_date = f.split(",")
s_date = s.split(",")

f = date(int(f_date[0]),int(f_date[1]),int(f_date[2]))
s = date(int(s_date[0]),int(s_date[1]),int(s_date[2]))

answer  = f - s

print("Days between date's is => ",answer.days)