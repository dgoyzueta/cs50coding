def print_items(final_dict):
    for key in final_dict:
        print(final_dict[key], key)

def main():

    final_list = {}

    while True:
        try:
            item = input().strip().upper()
            if item != "":
                final_list[item] = final_list[item] + 1
        except KeyError:
            final_list[item] = 1
        except EOFError:
            print("\n")
            if final_list != {}:
                print_items(dict(sorted(final_list.items())))
            break

main()
