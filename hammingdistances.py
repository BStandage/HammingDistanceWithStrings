
# returns hamming distance between two strings
def hamming_distance(str1, str2):
    hd = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hd += 1

    return hd

# produces all strings within hamming distance d from str
def hamming_list(str, d):
    return



if __name__ == '__main__':
    hamming_distance('Brian', 'Briaz')