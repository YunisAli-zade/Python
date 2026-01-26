def solution(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False
    for word1, word2 in zip(sentence1, sentence2):
        if word1 == word2:
            continue
        if [word1, word2] in similarPairs or [word2, word1] in similarPairs:
            continue
        return False
  	return True
    pass
