def abbreviate_word(w):
    # Adding last, fake character to add the last char to result in the loop
    w +=  '_'
    last_char = w[0]
    counter = 0
    result = ''
    
    # for i in range(len(w)):
    #     c = w[i]
    for c in w:
        if c == last_char:
            # counter = counter + 1
            counter += 1            
        else:
            # Add to result
            result += last_char
            if counter == 2:
                result += last_char
            elif counter > 2:
                result += str(counter)

            # Reset variables
            last_char = c
            counter = 1
    
    return result

if __name__ == '__main__':
    c = int(input())

    for i in range(c):
        word = input()
        print(abbreviate_word(word))