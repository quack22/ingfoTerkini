"""
Aplikasi Pelacakan Gempa Terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGE
"""
import gempaTerkini

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = gempaTerkini.ekstraksiData()
    gempaTerkini.tampilkanData(result)