from urielplus import urielplus as uriel
import csv

u = uriel.URIELPlus()
u.set_cache(True)
u.integrate_databases()
u.softimpute_imputation()

MT560_LANGS = [['sinh1246', 'stan1293'], ['stan1293', 'cebu1242'], ['stan1293', 'amha1245'], ['faro1244', 'stan1293'], ['stan1293', 'nucl1235'], ['stan1293', 'kirg1245'], ['stan1293', 'haus1257'], ['amha1245', 'stan1293'], ['stan1293', 'sind1272'], ['taga1270', 'stan1293'], ['stan1293', 'nucl1417'], ['stan1293', 'cent1989'], ['lomb1257', 'stan1293'], ['stan1293', 'ewee1241'], ['stan1293', 'sinh1246'], ['stan1293', 'tami1289'], ['egyp1253', 'stan1293'], ['stan1293', 'plat1254'], ['stan1293', 'luxe1241'], ['stan1293', 'mara1378'], ['kaza1248', 'stan1293'], ['stan1293', 'xhos1239'], ['zulu1248', 'stan1293'], ['mara1378', 'stan1293'], ['stan1293', 'kaza1248'], ['stan1293', 'panj1256'], ['nucl1235', 'stan1293'], ['xhos1239', 'stan1293'], ['nucl1305', 'stan1293'], ['stan1293', 'egyp1253'], ['nucl1310', 'stan1293'], ['java1254', 'stan1293'], ['stan1293', 'nucl1310'], ['tami1289', 'stan1293'], ['tata1255', 'stan1293'], ['stan1293', 'nucl1302'], ['stan1293', 
'yoru1245'], ['stan1293', 'tata1255'], ['stan1293', 'taga1270'], ['stan1293', 'indo1316'], ['afri1274', 'stan1293'], ['indo1316', 'stan1293'], ['soma1255', 'stan1293'], ['yoru1245', 'stan1293'], ['stan1293', 'guja1252'], ['nucl1347', 'stan1293'], ['stan1293', 'wels1247'], ['bela1254', 'stan1293'], ['stan1293', 'occi1239'], ['wels1247', 'stan1293'], ['stan1293', 'nucl1305'], ['swat1243', 'stan1293'], ['stan1293', 'lomb1257'], ['guja1252', 'stan1293'], ['stan1293', 'afri1274'], ['stan1293', 'swat1243'], ['stan1293', 'zulu1248'], ['stan1293', 'bash1264'], ['ewee1241', 'stan1293'], ['cent1989', 'stan1293'], ['bash1264', 'stan1293'], ['stan1293', 'java1254'], ['stan1293', 'soma1255'], ['stan1293', 'sout2832'], ['plat1254', 'stan1293'], ['nucl1302', 'stan1293'], ['haus1257', 'stan1293'], ['stan1293', 'chha1249'], ['panj1256', 'stan1293'], ['stan1293', 'faro1244'], ['stan1293', 'turk1304'], ['cebu1242', 'stan1293'], ['stan1293', 'bela1254'], ['stan1293', 'kiny1244'], ['occi1239', 'stan1293'], ['sind1272', 'stan1293'], ['stan1293', 'maor1246'], ['kiny1244', 'stan1293'], ['shon1251', 'stan1293'], ['maor1246', 'stan1293'], ['turk1304', 'stan1293'], ['chha1249', 'stan1293'], ['sout2832', 'stan1293'], ['luxe1241', 'stan1293'], ['nucl1417', 'stan1293'], ['stan1293', 'shon1251'], ['kirg1245', 'stan1293'], ['stan1293', 'nucl1347']]

NUSA_LANGS = [['beta1252', 'bima1247'], ['beta1252', 'indo1316'], ['beta1252', 'java1254'], ['beta1252', 'nucl1460'], ['beta1252', 'maka1311'], ['beta1252', 'mina1268'], ['beta1252', 'sund1252'], ['bima1247', 'beta1252'], ['bima1247', 'indo1316'], ['bima1247', 'java1254'], ['bima1247', 'nucl1460'], ['bima1247', 'maka1311'], ['bima1247', 'mina1268'], ['bima1247', 'sund1252'], ['indo1316', 'beta1252'], ['indo1316', 'bima1247'], ['indo1316', 'java1254'], ['indo1316', 'nucl1460'], ['indo1316', 'maka1311'], ['indo1316', 'mina1268'], ['indo1316', 'sund1252'], ['java1254', 'beta1252'], ['java1254', 'bima1247'], ['java1254', 'indo1316'], ['java1254', 'nucl1460'], ['java1254', 'maka1311'], ['java1254', 'mina1268'], ['java1254', 'sund1252'], ['nucl1460', 'beta1252'], ['nucl1460', 'bima1247'], ['nucl1460', 'indo1316'], ['nucl1460', 'java1254'], ['nucl1460', 'maka1311'], ['nucl1460', 'mina1268'], ['nucl1460', 'sund1252'], ['maka1311', 'beta1252'], ['maka1311', 'bima1247'], ['maka1311', 'indo1316'], ['maka1311', 'java1254'], ['maka1311', 'nucl1460'], ['maka1311', 'mina1268'], ['maka1311', 'sund1252'], ['mina1268', 'beta1252'], ['mina1268', 'bima1247'], ['mina1268', 'indo1316'], ['mina1268', 'java1254'], ['mina1268', 'nucl1460'], ['mina1268', 'maka1311'], ['mina1268', 'sund1252'], ['sund1252', 'beta1252'], ['sund1252', 'bima1247'], ['sund1252', 'indo1316'], ['sund1252', 'java1254'], ['sund1252', 'nucl1460'], ['sund1252', 'maka1311'], ['sund1252', 'mina1268']]

DISTANCES = ["genetic", "geographic", "syntactic", "inventory", "phonological", "featural", "morphological"]

with open("mt560_distances.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    header = ["source_lang", "target_lang"] + DISTANCES

    writer.writerow(header)

    for lang_pair in MT560_LANGS:
        distance_values = u.new_distance(DISTANCES, lang_pair)

        # Convert distance_values to a string of comma-separated values
        distance_str = ",".join(f"{value:.4f}" for value in distance_values)

        print(distance_str)

        writer.writerow([lang_pair[0], lang_pair[1]] + distance_values)


with open("nusa_distances.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    header = ["source_lang", "target_lang"] + DISTANCES

    writer.writerow(header)

    for lang_pair in NUSA_LANGS:
        distance_values = u.new_distance(DISTANCES, lang_pair)

        # Convert distance_values to a string of comma-separated values
        distance_str = ",".join(f"{value:.4f}" for value in distance_values)

        print(distance_str)

        writer.writerow([lang_pair[0], lang_pair[1]] + distance_values)
