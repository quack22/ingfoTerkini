import requests
from bs4 import BeautifulSoup


def ekstraksiData():
    """
    Tanggal : 14 Maret 2024
    Waktu : 01:56:14 WIB
    Magnitudo : 6.2
    Kedalaman : 10 km
    Lokasi : LS=-0.21 BT=125.64
    Pusat Gempa : Pusat Gempa berada di 128 km Tenggara TUTUYAN-BOLTIM-SULUT
    :return:
    """
    # adding extra headers to fix 403 error status (sc: stackoverflow)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'
    }
    # using try and except to anticipate any-errors.
    try:
        content = requests.get('https://bmkg.go.id', headers=headers)
    except Exception:
        return None

    # checking status code
    # 200 OK
    # 400 Client Error
    # 500 Server Error
    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split(', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None
        kedalaman = None

        for res in result:
            print(i, res)
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text
            i += 1

        hasil = dict()
        hasil['tanggal'] = tanggal #'15 Maret 2024'
        hasil['waktu'] = waktu #'01:56:14 WIB'
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = kedalaman
        hasil['koordinat'] = {'ls': ls, 'bt':  bt}
        hasil['lokasi'] = lokasi
        hasil['dirasakan'] = dirasakan
        return hasil
    else:
        return None

def tampilkanData(result):
    if result is None:
        print('Tidak bisa menemukan data')
        return
    print('Gempa Terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Koordinat: LS= {result['koordinat']['ls']}, BT= {result['koordinat']['bt']}")
    print(f"{result['dirasakan']}")

# if __name__ == '__main__':
#     print('Hai')