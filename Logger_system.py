import datetime

print("====== Logger System ======")

LOG_FILE = "app_logs.txt"


class Logger:

    @staticmethod
    def write_log(message):
        try:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(LOG_FILE, "a") as file:
                file.write(f"[{timestamp}] {message}\n")

            print("Log written successfully.")

        except Exception as e:
            print("Error writing log:", e)


if __name__ == "__main__":

    Logger.write_log("Application started.")
    Logger.write_log("User logged in.")
    Logger.write_log("Error: Invalid password attempt.")