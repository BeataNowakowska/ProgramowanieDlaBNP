import datetime

class SimpleLogger:
    def __init__(self, filename):
        """Inicjalizuje logger z podaną nazwą pliku."""
        self.filename = filename

    def log(self, message):
        """Dodaje wiadomość do pliku z logami, z czasem."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, 'a') as file:
            file.write(f"[{timestamp}] {message}\n")

# Przykład użycia
if __name__ == "__main__":
    logger = SimpleLogger("logfile.txt")
    logger.log("Logowanie rozpoczęte.")
    logger.log("To jest kolejna wiadomość.")
