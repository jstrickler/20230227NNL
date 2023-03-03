"""
General tools for searching text.

search(search-term, file-list, ignore_case=False)
"""
import sys

def main(args):
    """
    Program entry point.

    :return: None
    """
    search_term, *file_paths = args
    results = search(search_term, *file_paths)
    for result in results:
        print(result)

def search(search_term: str, *file_paths, ignore_case: bool=False):
    """
    Search one or more files for a search term.

    part one
    --------

    :param search_term: Search term
    :param file_paths: Iterable of file paths to search
    :param ignore_case: If True, ignore case when searching files
    :return: List of matching lines
    """
    matching_lines = []
    if ignore_case:
        search_term = search_term.lower()
    for file_path in file_paths:
        with open(file_path) as file_in:
            for raw_line in file_in:
                search_line = raw_line.lower() if ignore_case else raw_line
                if search_term in search_line:
                    line = raw_line.rstrip()
                    matching_lines.append(line)
    return matching_lines

if __name__ == '__main__':
    main(sys.argv[1:])
