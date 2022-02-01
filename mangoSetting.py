

class MangoInfo:
    with open("mango_info.txt") as f:
        lines = f.readlines()
    data = []
    for line in lines:
        data.append(line.split(' '))

    userName = data[0][1].strip('\n')
    password = data[1][1].strip('\n')
    db_name = data[2][1].strip('\n')
    tempLink = data[3][1].strip('\n')

    def generate_link(self):
        new_link = self.switch_str_between_chars(self.tempLink, self.userName, '//', ":")
        temp_str = new_link.split('//')
        temp_str[1] = self.switch_str_between_chars(temp_str[1], self.password, ":", "@")
        new_link = '//'.join(temp_str)
        temp_str = new_link.split("@")
        temp_str[1] = self.switch_str_between_chars(temp_str[1], self.db_name, "/", "?")
        return "@".join(temp_str)

    def switch_str_between_chars(self, ogStr, insStr, start_char, end_char):
        temp = ogStr.split(start_char)
        temp2 = temp[1].split(end_char)
        temp2[0] = insStr
        temp[1] = end_char.join(temp2)
        return start_char.join(temp)


