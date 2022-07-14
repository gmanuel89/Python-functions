## Get CSV header
def get_csv_header(input_csv_file: list[list] | list[dict]) -> list[str]:
    if isinstance(input_csv_file[0], list):
        return input_csv_file[0]
    elif isinstance(input_csv_file[0], dict):
        return list(input_csv_file[0].keys())
    else:
        pass
