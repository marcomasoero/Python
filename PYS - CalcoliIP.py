#List Comprehension
import math

def conversioneDecimale(ipBin):
    gruppiDecimali = []
    for i in range(0, 32, 8):
        ottetto = ipBin[i:i+8]
        gruppiDecimali.append(str(int(ottetto, 2)))
    return ".".join(gruppiDecimali)

def main():
    #Definisco l'IP
    ip = "90.90.120.1"
    print(ip)
    #Dichiaro la notazione cidr
    cidr = 24
    print(cidr)
    #Calcolo la subnet
    subnet = "1" * cidr + "0" * (32 - cidr)
    print(subnet)
    #Calcolo l'anti subnet
    wildCard = "0" * cidr + "1" * (32 - cidr)
    #Spezzo l'ip in grouppi x e li converto in gruppi binari
    ipBinGroup = [format(int(x), '08b') for x in ip.split('.')]
    print(ipBinGroup)
    #Unisco i gruppi x
    ipBin = ''.join(ipBinGroup)
    print(ipBin)
    #Calcolo ip di rete e di broadcast
    ipNet = ipBin[0:cidr] + "0" * (32 - cidr)
    ipBroad = ipBin[0:cidr] + "1" * (32 - cidr)
    print(ipNet)
    print(ipBroad)

    conversioneDecimale(ipBin)
    print(ipBin)

#formula per l'esecuzione del main
if __name__ == "__main__":
    main()