#project
#boy_name:?
#girl_name:?
#Output should be jyeshta loves rakshini

boy_name=input("boy_name: ")
girl_name=input("girl_name: ")

#Age difference is??????

boy_age=int(input("boy_Age: "))
girl_age=int(input("girl_Age: "))

print(boy_name +  "loves"  + girl_name)#solved this using formatting string

age_diff = abs( boy_age - girl_age )

print(boy_name+ " loves " +girl_name+".Age_difference is" + str(age_diff))

print(f"{boy_name} loves {girl_name}.age difference is {age_diff}")







