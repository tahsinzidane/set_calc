print("""
      Hi dear, what's up!
      Select an option:
      1. Union (A ∪ B)
      2. Intersection (A ∩ B)
      3. Difference (A - B)
      4. Power set
""")

def ask_for_sets():
    first_part = input("Enter elements of Set A (comma-separated, e.g., 1, 2, a): ")
    second_part = input("Enter elements of Set B (comma-separated, e.g., 3, 4, b): ")
    
    # Convert input strings to sets
    set_a = set(first_part.replace(" ", "").split(","))
    set_b = set(second_part.replace(" ", "").split(","))
    return set_a, set_b

def power_set(s):
    """Function to calculate the power set of a given set"""
    n = len(s)
    elements = list(s)  
    power_set_list = []
    
    # loop through all possible combinations (2^n subsets)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i & (1 << j)) > 0:
                subset.append(elements[j])
        power_set_list.append(subset)
    
    return power_set_list


selected_option = int(input("1/2/3/4: "))

if selected_option == 1:
    set_a, set_b = ask_for_sets()
    print(f"Union (A ∪ B): {set_a.union(set_b)}")

elif selected_option == 2:
    set_a, set_b = ask_for_sets()
    print(f"Intersection (A ∩ B): {set_a.intersection(set_b)}")

elif selected_option == 3:
    set_a, set_b = ask_for_sets()
    print(f"Difference (A - B): {set_a.difference(set_b)}")

elif selected_option == 4:
    input_set = input("Enter elements of the set (comma-separated, e.g., a, b, c): ")
    # convert the input to a set
    elements = set(input_set.replace(" ", "").split(","))
    power_set_result = power_set(elements)
    print("Power Set:")
    for subset in power_set_result:
        print(subset)

else:
    print("Invalid option selected. Please choose 1, 2, 3, or 4.")
