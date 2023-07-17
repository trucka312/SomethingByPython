def count_vietnamese_letters(input_string):
    vietnamese_letters = ['a', 'ă', 'â', 'e', 'ê', 'i', 'o', 'ô', 'ơ', 'u', 'ư', 'y', 'đ']
    count = 0
    for char in input_string:
        if char in vietnamese_letters:
            count += 1
    return count

# Example usage:
input_string = input("Nhập chuỗi chữ cái Latin: ")
result = count_vietnamese_letters(input_string)
print("Số lượng chữ cái Tiếng Việt có thể tạo thành trong chuỗi là:", result)