def read_file(fliename):
    lines = []
    try:
        with open(fliename, 'r', encoding='utf-8-sig') as file:
            for line in file:
                lines.append(line.strip())

    except Exception as error_message:
        print(error_message)
    return lines

def convert(lines):
    new = []
    person = None
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        if person:
            new.append(person + ': ' + line)
    return new

def out_file(filename,lines):
    result = False
    if not filename:
        print('請輸入檔案路徑')
        return result
    elif not lines:
        print('請輸入要儲存的chat')
        return result

    try:
        with open(filename,'w',encoding='utf-8') as file:
            for line in lines:
                file.write(line + '\n')
            result = True
    except Exception as error_message:
        print(error_message)
    return result

def main():
    input_fliename = 'input.txt'
    output_filename = 'output.txt'
    lines = read_file(input_fliename)
    lines = convert(lines)
    if out_file(output_filename,lines):
        print('檔案輸出成功!!!')
    else:
        print('檔案輸出失敗!!!')

if __name__ == '__main__':
    main()