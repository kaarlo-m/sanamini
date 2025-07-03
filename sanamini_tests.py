import sanamini

test_sub=check_word("aall")[0]
assert test_sub[1] == "aalloittainen"

assert test_sub[len(test_sub-1)] == "aallotus"