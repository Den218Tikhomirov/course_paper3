from utils import get_operations_file, get_filtr_list, get_sort_list, get_format_list


def main():
    print("Крсовая №3")
    data = get_operations_file()
    data = get_filtr_list(data)
    data = get_sort_list(data)
    data = get_format_list(data)
    for Operations in data:
        print(Operations)


if __name__ == "__main__":
    main()
