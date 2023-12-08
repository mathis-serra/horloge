import time

def afficher_heure(heure, alarme=None):
    if heure[0] < 0 or heure[0] > 23 or heure[1] < 0 or heure[1] > 59 or heure[2] < 0 or heure[2] > 59:
        print("Heure incorrecte")
        return
    # Print time
    while True:
        current_time = f"{heure[0]:02}h{heure[1]:02}m{heure[2]:02}s"
        print(current_time)
        # Check if alarme is reached
        if alarme is not None and heure == alarme:
            print("Alarme activée!")
            break
        # Wait 1 second
        time.sleep(1)

        # Increment time
        heure = (heure[0], heure[1], heure[2] + 1)
        if heure[2] == 60:
            heure = (heure[0], heure[1] + 1, 0)
            if heure[1] == 60:
                heure = (heure[0] + 1, 0, 0)
                if heure[0] == 24:
                    heure = (0, 0, 0)

# Get user input for time and alarm
heure = int(input("Entrez l'heure : "))
minute = int(input("Entrez les minutes : "))
seconde = int(input("Entrez les secondes : "))

alarme_heure = int(input("Entrez l'heure de l'alarme (ou appuyez sur Entrée pour ignorer) : "))
alarme_minute = int(input("Entrez les minutes de l'alarme (ou appuyez sur Entrée pour ignorer) : "))
alarme_seconde = int(input("Entrez les secondes de l'alarme (ou appuyez sur Entrée pour ignorer) : "))

alarme_time = (alarme_heure, alarme_minute, alarme_seconde) if alarme_heure != "" else None

# Call the function with the typed time and alarm
afficher_heure((heure, minute, seconde), alarme_time)

