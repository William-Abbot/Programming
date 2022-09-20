import functions.isValid as valid


digit_list = [5,0,1,0,0,0,0,9,6,0,0,0,0,9,0,0,5,0,0,0,0,0,0,5,2,0,7,4,9,0,1,0,0,0,7,0,0,0,0,0,0,7,0,0,0,1,3,0,0,0,0,0,2,0,3,0,4,0,5,9,0,0,0,0,2,8,0,7,1,0,4,0,7,6,5,8,2,0,0,0,0]

location = 'E5'

candidate_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result_list = [True]*9

for i in range(len(candidate_list)):
    result_list[i] = valid.isValid(digit_list, location, candidate_list[i])

print(result_list)
print('')
