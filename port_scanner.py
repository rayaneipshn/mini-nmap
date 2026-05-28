import socket
import threading
import queue
import time

# Fonction de scan d'un port unique
def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5) 
        resultat = s.connect_ex((ip, port))
        s.close()
        return resultat == 0
    except:
        return False

# Fonction exécutée par chaque Thread
def worker(ip, port_queue, open_ports):
    while not port_queue.empty():
        try:
            port = port_queue.get_nowait()
            if scan_port(ip, port):
                print(f" [+] Port {port} ouvert")
                open_ports.append(port)
            port_queue.task_done()
        except queue.Empty:
            break

# Fonction principale
def main():
    target_ip = input("Entrez l'adresse IP à scanner : ")
    premier_port = int(input("Port de début (ex: 1) : "))
    dernier_port = int(input("Port de fin (ex: 1024) : "))
    
    print(f"\n--- Analyse de {target_ip} en cours ---\n")
    start_time = time.time()

    # Création de la file d'attente (Queue)
    port_liste = queue.Queue()
    for p in range(premier_port, dernier_port + 1):
        port_liste.put(p)

    # Liste pour stocker les résultats
    ports_true = []
    threads = []

    # Création et lancement des threads
    for _ in range(100):
        t = threading.Thread(target=worker, args=(target_ip, port_liste, ports_true))
        t.start()
        threads.append(t)

    # Attente de la fin de tous les threads
    for t in threads:
        t.join()

    # Affichage du résumé
    end_time = time.time()
    print(f"\n--- Scan terminé en {round(end_time - start_time, 2)} secondes ---")
    print(f"Ports ouverts : {sorted(ports_true)}")

if __name__ == "__main__":
    main()
