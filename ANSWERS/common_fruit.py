# fruit1 = set()
# with open("../DATA/fruit1.txt") as fruit1_in:
#     for raw_line in fruit1_in:   #  fruit1_in.readline()
#         fruit = raw_line.rstrip().lower()
#         fruit1.add(fruit)
#
# fruit2 = set()
# with open("../DATA/fruit2.txt") as fruit2_in:
#     for raw_line in fruit2_in:
#         fruit = raw_line.rstrip().lower()
#         fruit2.add(fruit)

def main():
    fruit1 = read_items_into_set("../DATA/fruit1.txt")
    fruit2 = read_items_into_set("../DATA/fruit2.txt")

    common_fruits = fruit1 & fruit2

    print(common_fruits)


def read_items_into_set(file_path):
    item_set = set()
    with open(file_path) as file_in:
        for raw_line in file_in:
            item = raw_line.rstrip().lower()
            item_set.add(item)
    return item_set


# fruit_in = open('../DATA/fruit1.txt')
# # ... do something
# fruit_in.close()  # not needed when using 'with' block

main()