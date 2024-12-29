import json
import sys


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def write_json(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def main():
    if len(sys.argv) < 4:
        print("Необходимо передать три файла как аргументы!")
        print("Пример использования:")
        print("python task3.py values.json tests.json report.json")
        return


    values_file = sys.argv[1]
    tests_file = sys.argv[2]
    report_file = sys.argv[3]

    values_data = read_json(values_file)
    tests_data = read_json(tests_file)
    values_dict = {item['id']: item['value'] for item in values_data}

    for test in tests_data.values():
        test_id = test['id']
        if test_id in values_dict:
            test['value'] = values_dict[test_id]

    write_json(report_file, tests_data)
    print(f"Отчет успешно записан в {report_file}")

if __name__ == "__main__":
    main()
