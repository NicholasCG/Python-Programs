words_1_19 = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words_20_90_tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

word_cnt_1_19 = [len(x) for x in words_1_19]
word_cnt_20_90_tens = [len(x) for x in words_20_90_tens]

def num_to_word_upto_999(n):
    rtn = ''
    hund = n // 100
    if hund:
        rtn += words_1_19[hund] + ' hundred'
    rest_upto_99 = n % 100
    if hund and rest_upto_99:
        rtn += ' and '
    if rest_upto_99 < 20:
        rtn += words_1_19[rest_upto_99]
    else:
        tens_from_20 = rest_upto_99 // 10
        if tens_from_20:
            rtn += words_20_90_tens[tens_from_20 - 2] + ' '
        rtn += words_1_19[rest_upto_99 % 10]
    return rtn

def num_to_word_cnt_upto_999(n):
    rtn = 0
    hund = n // 100
    if hund:
        rtn += word_cnt_1_19[hund] + 7
    rest_upto_99 = n % 100
    if hund and rest_upto_99:
        rtn += 3
    if rest_upto_99 < 20:
        rtn += word_cnt_1_19[rest_upto_99]
    else:
        tens_from_20 = rest_upto_99 // 10
        if tens_from_20:
            rtn += word_cnt_20_90_tens[tens_from_20 - 2]
        rtn += word_cnt_1_19[rest_upto_99 % 10]
    return rtn

cnt_sum = 11    # one thousand
for i in range(1, 1000):
    cnt_sum += num_to_word_cnt_upto_999(i)

print(cnt_sum)