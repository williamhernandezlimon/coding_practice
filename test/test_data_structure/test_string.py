#!/usr/bin/env python3
from src.data_structure import string
from pytest import mark

# solution 1
@mark.parametrize(
	"test_s, expected_response", [
		("baaaaa", 1),  # "baaaba"
		("baaabbaabbba", 2),
		("baabab", 0),
		("", 0)
	]
)
def test_solution1(test_s, expected_response):
	response = string.solution1(test_s)

	assert response == expected_response

# solution 2
@mark.parametrize(
	"test_s, test_c, expected_response", [
		("", [1], 0),
		("a", [], 0),
		("", [], 0),
		("abccbd", [0,1,2,3,4,5], 2),
		("aabbcc", [1,2,1,2,1,2], 3),
		("aaaa", [3,4,5,6], 12),
		("ababa", [10,5,10,5,10], 0),
	]
)
def test_solution2(test_s, test_c, expected_response):
	response = string.solution2(test_s, test_c)

	assert response == expected_response


# solution 3
@mark.parametrize(
	"test_t, test_r, expected_response", [
		(
			["test1a", "test2", "test1b", "test1c", "test3"], 
			[
				"Wrong answer", "OK", "Runtime error", "OK", 
				"Time limit exceeded"
			],
			33
		)

	]
)
def test_solution3(test_t, test_r, expected_response):
	response = string.solution3(test_t, test_r)

	assert response == expected_response
	

@mark.parametrize("test_s, expected_response", [
		("(1+(4+5+2)-3)+(6+8)", 23),
		("- (3 + (4 + 5))", -12)
	]
)
def test_calculate(test_s, expected_response):
	response = string.calculate(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("", ""),
		("a", "a"),
		("aa", "a2"),
		("aaa", "a3"),
		("aabbcc", "a2b2c2"),
		("abbcdddd", "ab2cd4"),
		("abcdefg", "abcdefg"),
		("AaBBbb", "AaB2b2"),
		("ddaaaff", "d2a3f2"),
		("daaaafffyy", "da4f3y2"),
		("mississippi", "mis2is2ip2i"),
		("aaabbccccddefg", "a3b2c4d2efg")
	]
)
def test_compress(test_s, expected_response):
	response = string.compress(test_s)

	assert response == expected_response


@mark.parametrize("test_chars, test_new_chars, expected_response", [
		(["a"],["a"],1),
		(["a","b","b","b","b","b","b","b","b","b","b","b","b"], ["a","b","1","2"], 4),
		(["a","a","b","b","c","c","c"],  ["a","2","b","2","c","3"], 6)
	]
)
def test_compress_list(test_chars, test_new_chars, expected_response):
	response = string.compress_list(test_chars)
	assert response == expected_response
	assert test_chars == test_new_chars


@mark.parametrize("test_n, expected_response", [
		(1, "1"),
		(2, "11"),
		(3, "21"),
		(4, "1211"),
		(5, "111221")
	]
)
def test_count_and_say(test_n, expected_response):
	response = string.count_and_say(test_n)

	assert response == expected_response


@mark.parametrize("test_n, expected_response", [
		(0, []),
		(1, ["()"]),
		(3, ["((()))","(()())","(())()","()(())","()()()"])
	]
)
def test_generate_parenthesis(test_n, expected_response):
	response = string.generate_parenthesis(test_n)

	assert response == expected_response


@mark.parametrize(
	"test_hostnames_range, test_hosts, expected_response", [
		("", {}, []),
		("web0001-1000.facebook.com", {}, []),
		("web0001-1000.facebook.com", {
										"web0001.facebook.com": {
											"instances": {
												"app": 1,
												"docker": 2,
												"instana": 3
											}
										},
										"web0002.facebook.com": {
											"instances": {
												"app": 2,
												"docker": 2,
												"instana": 3
											}
										},
										"web1000.facebook.com": {
											"instances": {
												"app": 4,
												"docker": 2,
												"instana": 3
											}
										}
									}, ["web0001.facebook.com", "web0002.facebook.com"])
	]
)
def test_get_bad_hosts(test_hostnames_range, test_hosts, expected_response):
	response = string.get_bad_hosts(test_hostnames_range, test_hosts)

	assert response == expected_response


@mark.parametrize(
	"test_s1, test_s2, expected_response", [
		("", "", ""),
		("", "-", "-"),
		("", "a", "a"),
		('aa', 'a', 'aa'),
		('---', '--', '---'),
		('hello-12', 'hello-1', 'hello-12'),
		('hello-world', 'hello-earth', 'hello-world')
	]
)
def test_get_larger(test_s1, test_s2, expected_response):
	response = string.get_larger(test_s1, test_s2)

	assert response == expected_response


@mark.parametrize("test_strs, expected_response", [
		([""], [[""]]),
		(["a"], [["a"]]),
		(
			["eat","tea","tan","ate","nat","bat"], 
			[["bat"],["nat","tan"],["ate","eat","tea"]]
		)
	]
)
def test_group_anagrams(test_strs, expected_response):
	response = string.group_anagrams(test_strs)

	# convert elements to sets
	assert len(response) == len(expected_response)
	for i in range(len(response)):
		response[i] = set(response[i])
		expected_response[i] = set(expected_response[i])

	for r in response:
		assert r in expected_response


@mark.parametrize(
	"test_serialNumber, expected_response", [
		([], 0),
		(["1"], 0),
		(["AVG190420T"], 20),
		(["RTF20001000Z"], 1000),
		(["QWER201850G"], 0),
		(["AFA199620E"], 0),
		(["ERT1947200T"], 200),
		(["RTY20202004"], 0),
		(["DRV1984500Y"], 500),
		(["A201550B"], 0),
		(["ABB19991000Z"], 0),
		(["XYZ200019Z"], 0),
		(["SCD203010T"], 0),
		(["A201550B", "ABB19991000Z", "XYZ200019Z", "ERF200220", 
			"SCD203010T"], 0),
		(["QDB2012R20B", "RED190250E", "RFV201111T", "TYU20121000E", 
			"AAA198710B", "AbC200010E"], 1050),

	]
)
def test_countCounterfeit(test_serialNumber, expected_response):
	response = string.countCounterfeit(test_serialNumber)

	assert response == expected_response


@mark.parametrize(
	"test_digits, expected_response", [
		("2", ["a", "b", "c"]),
		# ("12131", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
		# ("213", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
		("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
		("234", [
			"adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh",
			"bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg",
			"ceh","cei","cfg","cfh","cfi"
			]
		)

	]
)
def test_letter_combination(test_digits, expected_response):
	response = string.letter_combination(test_digits)

	assert response == expected_response


@mark.parametrize(
	"test_str_list, expected_response", [
		([""], ""),
		(["caa", "", "a", "acb"], ""),
		(["flower", "flow"], "flow"),
		(["flower", "flow", "flight"], "fl"),
		(["dog","racecar","car"], "")
	]
)
def test_longest_common_prefix(test_str_list, expected_response):
	response = string.longest_common_prefix(test_str_list)
	response_inefficient = string.longest_common_prefix_inefficient(test_str_list)

	assert response == expected_response
	assert response_inefficient == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("", ""),
		("a", "a"),
		("aba", "aba"),
		("abba", "abba"),
		("cbbd", "bb"),
		("abcdefg", "g")
	]
)
def test_longest_palindrome(test_s, expected_response):
	response = string.longest_palindrome(test_s)

	assert response == expected_response


@mark.parametrize("test_text, expected_response", [
		("", 0),
		("nlaebolko", 1),
		("loonbalxballpoon", 2)
	]
)
def test_max_number_of_balloons(test_text, expected_response):
	response = string.max_number_of_balloons(test_text)

	assert response == expected_response


@mark.parametrize(
	"test_str, test_substr_len, expected_response", [
		("abciiidef", 3, 3),
		("aeiou", 2, 2),
		("leetcode", 3, 2),
		("rhythms", 4, 0),
		("tryhard", 4, 1),
		("", 4, 0),
		("aeiou", 0, 0),
		("wzx", 7, 0)
	]
)
def test_max_vowels(test_str, test_substr_len, expected_response):
	response = string.max_vowels(test_str, test_substr_len)

	assert response == expected_response


@mark.parametrize("test_s, test_cost, expected_response", [
		("abaac", [1,2,3,4,5], 3),
		("aaaaa", [1,2,3,4,5], 10),
		("abc", [1,2,3], 0),
		("aabaa", [1,2,3,4,1], 2),
		("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1], 26),
		("aaabbbabbbb", [3,5,10,7,5,3,5,5,4,8,1], 26)
	]
)
def test_min_cost(test_s, test_cost, expected_response):
	response = string.min_cost(test_s, test_cost)

	assert response == expected_response


@mark.parametrize("test_s, expected_response", [
		("bcabc", "abc"),
		("cbacdcbc", "acdb"),
		("abacb", "abc")
	]
)
def test_remove_duplicates_letters(test_s, expected_response):
	response = string.remove_duplicates_letters(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_number, expected_response", [
		(123, 321),
		(-123, -321),
		(1534236469, 0),
		(1, 1),
		(0, 0)
	]
)
def test_reverse_integer(test_number, expected_response):
	response = string.reverse_integer(test_number)

	assert response == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("", ""),
		("hello", "hello"),
		("hello world how are you", "you are how world hello"),
	]
)
def test_reverse_words(test_s, expected_response):
	response = string.reverse_words(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_roman_number, expected_response", [
		("I", 1),
		("V", 5),
		("X", 10),
		("L", 50),
		("C", 100),
		("D", 500),
		("M", 1000),
		("III", 3),
		("IV", 4),
		("III", 3),
		("IV", 4),
		("LVIII", 58),
		("MCMXCIV", 1994)
	]
)
def test_roman_to_integer(test_roman_number, expected_response):
	response = string.roman_to_integer(test_roman_number)

	assert response == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("A man, a plan, a canal: Panama", True),
		("race a car", False),
		(".,", True),
		(".a", True),
		("0P", False)
	]
)
def test_is_palindrom(test_s, expected_response):
	response = string.is_palindrome(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_number, expected_response", [
		(-1, False),
		(-11, False),
		(1211, False),
		(948, False),
		(0, True),
		(1, True),
		(11, True),
		(121, True),
		(1221, True)
	]
)
def test_is_palindrom_integer(test_number, expected_response):
	response = string.is_palindrome_integer(test_number)

	assert response == expected_response


@mark.parametrize("test_instructions, expected_response", [
		("GGLLGG", True),
		("GG", False),
		("GL", True),
		("GLGLGGLGL", False),
		("LLGRL", True)
	]
)
def test_is_robot_bounded(test_instructions, expected_response):
	response = string.is_robot_bounded(test_instructions)

	assert response == expected_response


@mark.parametrize(
	"test_string, expected_response", [
		("", True),
		("()", True),
		("()[]{}", True),
		("([{}])", True),
		("(]", False),
		("([)]", False),
		("()]", False),
		("]]", False),
		("((", False)
	]
)
def test_is_valid_paranthesis(test_string, expected_response):
	response = string.is_valid_parenthesis(test_string)

	assert response == expected_response


@mark.parametrize("test_l, expected_response", [
		([], {}),
		(['cheapair'], {
			'cheapair': {'c', 'h', 'e', 'a', 'p', 'a', 'i', 'r'}
			}
		),
		(['cheapair', 'cheapoair', 'peloton', 'pelican'], {
				'cheapair': {'pa'}, 
				'cheapoair': {'oa', 'po'}, 
				'peloton': {'t'}, 
				'pelican': {'li', 'li', 'ic', 'an', 'ca'}
			}
		)
	]
)
def test_get_substr(test_l, expected_response):
	response = string.get_substr(test_l)

	if not test_l:
		assert response == expected_response

	for s in response:
		assert response[s] in expected_response[s]


@mark.parametrize(
	"test_input, expected_response", [
		("", 0),
		("abcabcbb", 3),
		("abc", 3),
		("a", 1),
		("aaaaa", 1),
		("tmmzuxt", 5)
	]
)
def test_length_of_longest_substring(test_input, expected_response):
	response = string.length_of_longest_substring(test_input)

	assert response == expected_response


@mark.parametrize("test_s, expected_response", [
		("A", 1),
		("AB", 28),
		("ZY", 701),
	]
)
def test_title_to_number(test_s, expected_response):
	response = string.title_to_number(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_s, expected_response", [
		("", ""),
		("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
		(
			"The quick brown fox jumped over the lazy dog", 
			"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
		)
	]
)
def test_to_goat_latin(test_s, expected_response):
	response = string.to_goat_latin(test_s)

	assert response == expected_response


@mark.parametrize(
	"test_nums, expected_response", [
		([2,2,1], 1),
		([4,1,2,1,2], 4),
	]
)
def test_single_number(test_nums, expected_response):
	response = string.single_number(test_nums)

	assert response == expected_response


@mark.parametrize(
	"test_haystack, test_needle, expected_response", [
		("", "", 0),
		("", "a", -1),
		("mississippi", "issip", 4),
		("a", "", 0),
		("hello", "ll", 2),
		("hello", "aaaa", -1),
	]
)
def test_str_str(test_haystack, test_needle, expected_response):
	response = string.str_str(test_haystack, test_needle)

	assert response == expected_response


@mark.parametrize("test_s, test_word_dict, expected_response", [
		("leetcode", ["leet", "code"], True),
		("applepenapple", ["apple", "pen"], True),
		("catsandog", ["cats","dog","sand","and","cat"], False)
	]
)
def test_word_break(test_s, test_word_dict, expected_response):
	response = string.word_break(test_s, test_word_dict)

	assert response == expected_response

	response = string.word_break_dp(test_s, test_word_dict)
	assert response == expected_response
