from algorithm import max_area_bruteforce, max_area_two_pointers

height = [1,1]
print("Brute Force Result:", max_area_bruteforce(height))
print("Two Pointers Result:", max_area_two_pointers(height))

height = [2,3,4,5,18,17,6]
print("Brute Force Result:", max_area_bruteforce(height))
print("Two Pointers Result:", max_area_two_pointers(height))

height = [1,2,1]
print("Brute Force Result:", max_area_bruteforce(height))
print("Two Pointers Result:", max_area_two_pointers(height))

height = [1,8,6,2,5]
print("Brute Force Result:", max_area_bruteforce(height))
print("Two Pointers Result:", max_area_two_pointers(height))