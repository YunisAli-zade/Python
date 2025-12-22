w = int(input())
def even_pieces(w:int) -> bool:
    return 'Yes' if w > 2 and w % 2 == 0 else 'No'
print(even_pieces(w))