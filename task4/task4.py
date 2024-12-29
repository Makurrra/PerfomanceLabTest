import sys


def read_numbers_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            numbers = [int(line.strip()) for line in file.readlines()]
        return numbers
    except FileNotFoundError:
        print(f"Файл {file_path} не найден!")
        return None


def find_median(nums):
    nums.sort()
    n = len(nums)
    if n % 2 == 1:
        return nums[n // 2]
    else:
        return nums[n // 2 - 1]


def main():
    if len(sys.argv) != 2:
        print("Пример использования: python task4.py <nums_file>")
        return

    nums_file = sys.argv[1]

    # Загрузка данных из файла
    nums = read_numbers_from_file(nums_file)

    # Проверка на успешность загрузки
    if nums is None:
        return

    median = find_median(nums)
    total_steps = sum(abs(num - median) for num in nums)
    print(total_steps)

if __name__ == "__main__":
    main()
