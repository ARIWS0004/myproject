def Hitung(angka):
    if not angka :
        return None
    return min(angka)

def nilai_minimal():
    assert Hitung([80,70,60]) == 60


nilai_minimal()