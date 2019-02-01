#!/usr/local/bin/python3 # Mac OS X interpreter
#!/usr/bin/python3 # Linux interpreter
# -*- coding: utf-8 -*-
#
# Script permettant l'ajout et la mise à jour des enregistrements DNS et DHCP d'une machine
# Pour isc_dhcp_server & bind9
#
 
import getopt, sys, re, IPy

# On importe IPy, si le module n'est pas présent on l'installe puis on l'importe de nouveau

def import_IPy():
    try :
        from IPy import IP
    except ModuleNotFoundError:
        from subprocess import call
        call(['sudo', 'pip3', 'install', 'IPy']) # Permet de lancer des commandes systèmes.
        print("\nIPy est installé !\n")
        return import_IPy() # On relance la fonction pour s'assurer de la bonne fin de l'installation.
    print("On retourne l'import")
    return exec("from IPy import IP")

def ip_is_correct(ip):
    try:
        IPy.ip(ip)
    except ValueError:
        return "La valeur {} n'est pas une adresse IP correcte."
    except AttributeError:
        import_IPy()
    
    return ip

def add_dns_record(file):
#Si nouvelle machine on ajoute le record dans le fichier de zone.
    record = []
    continuer = ""
    while continuer != "Q":
        name    = input("Entrer le nom de la machine : ")
        type    = input("Entrer le type d'enregistrement souhaité (A, CNAME ou MX) : ").upper()
        index = 2
        while type != "A" or type != "MX" or type != "CNAME":
            if type == "A" or type == "MX":
                ip      = ip_is_correct(input("Entrer l'adresse IP de {} : ".format(name)))
                record.insert(index, "{} {} {}\n".format(name, type, ip).split(' '))
                print(record)
                break
            elif type == "CNAME":
                cname   = input("Entrer l'alias de {} : ".format(name))
                record.insert(index, "{}\t{}\t{}\n".format(cname, type, name))
                print(record)
                break
            else:
                print("Le type demandé n'est pas disponible")
                type    = input("Entrer le type d'enregistrement souhaité (A, CNAME ou MX) : ").upper()
        continuer = input("Tapez \"Q\" pour quitter le menu des enregistrements DNS").upper()

    if record != []:
        return record

def update_dns_record():
#Si une machine existe on met à jour le record dans le fichier de zone.
    pass
    return 0
 
def add_dhcp_reservation():
# Si nouvelle machine on crée une nouvelle reservation.
    pass
    print("test")
    return 0
 
def update_dhcp_reservation():
# Si une reservation existe on met à jour les données machines.
    pass
    return 0
 
def import_csv():
    # format fichier:   nom_machine;@_mac;@_ip;type_rec_DNS
    print("Import csv file")
    sys.exit(0)
 
 
def help():
    print("Usage:\n\tadd_host.py")
    sys.exit(0)
 
# Main program
def main():
    import_IPy()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file"])
    except getopt.GetoptError as error:
        print(str(error))
        help()
        sys.exit(1)
 
    for opt, arg in opts:
        print(opt)
        if opt == "-h":
            help()
        elif opt == "-f" and arg != "":
            import_csv(arg)

# Stocke le contenu du fichier dans la variable data
    with open("add_host.txt", "r") as file_r:
        data = file_r.readlines()
    # with open("add_host2.txt", "w") as file_w:
        # for line in data2

    for line in data:
        line = line.split(" ")
        print(line)
        # for item in line:
        #     print(item)

# Utiliser file.writelines pour écrire ligne par ligne dans un fichier temporaire 
# le soumettre à validation
# Si le fichier est validé, alors on effectue un move.
    message = """
Veuillez utiliser une des options suivantes :
\t- Q : Quitter le script.
\t- DNS : Ajouter un nouvel enregistrement DNS.
\t- DHCP : Ajouter une nouvelle réservation pour un client DHCP

Option choisie : """

    loop_indic = input(message)

    while loop_indic.upper() != "Q":
        if loop_indic.upper() == "DHCP":
            loop_indic = ""
            print("On joue add_dhcp_reservation()\n{}".format(add_dhcp_reservation()))
	   # print("On joue add_dhcp_reservation(){}\n".format(add_dhcp_reservation()))
        elif loop_indic.upper() == "DNS":
            loop_indic = ""
            print("On joue add_dns_record() \n{}".format(add_dns_record(data)))
        else:
            loop_indic = input(message)

# 1. Stocker le fichier dans un tableau 
# 2. Ajouter la donnée avec la fonction insert(Index) fin de ligne \n
# 3. Réécrire dans le fichier avec le contenu du tableau.

# Si on lance ce programme __name__ == "__main__" sinon basename ...
if __name__ == "__main__":
    if float(sys.version[:3]) <= 3.0: #sys.version[:3] affiche les 3 premiers caractères de la sortie std
        print("Mauvaise version : {}".format(sys.version[:3]))
        sys.exit(1)
    main()
#!/usr/local/bin/python3 # Mac OS X interpreter
#!/usr/bin/python3 # Linux interpreter
# -*- coding: utf-8 -*-
#
# Script permettant l'ajout et la mise à jour des enregistrements DNS et DHCP d'une machine
# Pour isc_dhcp_server & bind9
#
 
import getopt, sys, re, IPy

# On importe IPy, si le module n'est pas présent on l'installe puis on l'importe de nouveau

def import_IPy():
    try :
        from IPy import IP
    except ModuleNotFoundError:
        from subprocess import call
        call(['sudo', 'pip3', 'install', 'IPy']) # Permet de lancer des commandes systèmes.
        print("\nIPy est installé !\n")
        return import_IPy() # On relance la fonction pour s'assurer de la bonne fin de l'installation.
    print("On retourne l'import")
    return exec("from IPy import IP")

def ip_is_correct(ip):
    try:
        IPy.ip(ip)
    except ValueError:
        return "La valeur {} n'est pas une adresse IP correcte."
    except AttributeError:
        import_IPy()
    
    return ip

def add_dns_record(file):
#Si nouvelle machine on ajoute le record dans le fichier de zone.
    record = []
    continuer = ""
    while continuer != "Q":
        name    = input("Entrer le nom de la machine : ")
        type    = input("Entrer le type d'enregistrement souhaité (A, CNAME ou MX) : ").upper()
        index = 2
        while type != "A" or type != "MX" or type != "CNAME":
            if type == "A" or type == "MX":
                ip      = ip_is_correct(input("Entrer l'adresse IP de {} : ".format(name)))
                record.insert(index, "{} {} {}\n".format(name, type, ip).split(' '))
                print(record)
                break
            elif type == "CNAME":
                cname   = input("Entrer l'alias de {} : ".format(name))
                record.insert(index, "{}\t{}\t{}\n".format(cname, type, name))
                print(record)
                break
            else:
                print("Le type demandé n'est pas disponible")
                type    = input("Entrer le type d'enregistrement souhaité (A, CNAME ou MX) : ").upper()
        continuer = input("Tapez \"Q\" pour quitter le menu des enregistrements DNS").upper()

    if record != []:
        return record

def update_dns_record():
#Si une machine existe on met à jour le record dans le fichier de zone.
    pass
    return 0
 
def add_dhcp_reservation():
# Si nouvelle machine on crée une nouvelle reservation.
    pass
    print("test")
    return 0
 
def update_dhcp_reservation():
# Si une reservation existe on met à jour les données machines.
    pass
    return 0
 
def import_csv():
    # format fichier:   nom_machine;@_mac;@_ip;type_rec_DNS
    print("Import csv file")
    sys.exit(0)
 
 
def help():
    print("Usage:\n\tadd_host.py")
    sys.exit(0)
 
# Main program
def main():
    import_IPy()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hf:", ["help", "file"])
    except getopt.GetoptError as error:
        print(str(error))
        help()
        sys.exit(1)
 
    for opt, arg in opts:
        print(opt)
        if opt == "-h":
            help()
        elif opt == "-f" and arg != "":
            import_csv(arg)

# Stocke le contenu du fichier dans la variable data
    with open("add_host.txt", "r") as file_r:
        data = file_r.readlines()
    # with open("add_host2.txt", "w") as file_w:
        # for line in data2

    for line in data:
        line = line.split(" ")
        print(line)
        # for item in line:
        #     print(item)

# Utiliser file.writelines pour écrire ligne par ligne dans un fichier temporaire 
# le soumettre à validation
# Si le fichier est validé, alors on effectue un move.
    message = """
Veuillez utiliser une des options suivantes :
\t- Q : Quitter le script.
\t- DNS : Ajouter un nouvel enregistrement DNS.
\t- DHCP : Ajouter une nouvelle réservation pour un client DHCP

Option choisie : """

    loop_indic = input(message)

    while loop_indic.upper() != "Q":
        if loop_indic.upper() == "DHCP":
            loop_indic = ""
            print("On joue add_dhcp_reservation()\n{}".format(add_dhcp_reservation()))
	   # print("On joue add_dhcp_reservation(){}\n".format(add_dhcp_reservation()))
        elif loop_indic.upper() == "DNS":
            loop_indic = ""
            print("On joue add_dns_record() \n{}".format(add_dns_record(data)))
        else:
            loop_indic = input(message)

# 1. Stocker le fichier dans un tableau 
# 2. Ajouter la donnée avec la fonction insert(Index) fin de ligne \n
# 3. Réécrire dans le fichier avec le contenu du tableau.

# Si on lance ce programme __name__ == "__main__" sinon basename ...
if __name__ == "__main__":
    if float(sys.version[:3]) <= 3.0: #sys.version[:3] affiche les 3 premiers caractères de la sortie std
        print("Mauvaise version : {}".format(sys.version[:3]))
        sys.exit(1)
    main()
