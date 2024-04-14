


def explode_file(input_file, output_file):
    with open(input_file, 'r') as infile:
        numbers = infile.readlines()

    # Duplicate each entry 9 times
    duplicated_numbers = [num.strip() + '\n' for num in numbers for _ in range(10)]

    with open(output_file, 'w') as outfile:
        outfile.writelines(duplicated_numbers)



# explode the files...
# input_filename = '10x50_tactile_2/case1_1x0/familiarFits.txt'
# output_filename = '10x50_tactile_2/case1_1x0/familiarFits_exploded.txt'
# explode_file(input_filename, output_filename)




explode_file('10x75_tactile_2/case1_10x75/familiarFits.txt', '10x75_tactile_2/case1_10x75/familiarFits_exploded.txt')
explode_file('10x75_tactile_2/case1_10x75/foreignFits.txt', '10x75_tactile_2/case1_10x75/foreignFits_exploded.txt')

explode_file('10x75_tactile_2/case1_1x0/familiarFits.txt', '10x75_tactile_2/case1_1x0/familiarFits_exploded.txt')
explode_file('10x75_tactile_2/case1_1x0/foreignFits.txt', '10x75_tactile_2/case1_1x0/foreignFits_exploded.txt')
