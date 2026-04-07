import time
from datetime import datetime # Naya module time aur date nikalne ke liye

def log_session(duration, subject):
    # Current time ko ek badhiya format mein set karna
    now = datetime.now().strftime("%Y-%m-%d %I:%M %p")
    
    # File ko 'a' (append) mode mein open karna taaki purana record delete na ho
    with open("study_history.txt", "a") as file:
        log_entry = f"[{now}] | {duration} Mins | {subject}\n"
        file.write(log_entry)

def countdown(minutes, message):
    print(f"\n=== {message} ===")
    total_seconds = minutes * 60

    while total_seconds > 0:
        mins_left = total_seconds // 60
        secs_left = total_seconds % 60
        
        print(f"\rTime remaining: {mins_left:02d}m {secs_left:02d}s", end="")
        time.sleep(1)
        total_seconds -= 1
        
    print("\nTime's up! \a")

def main():
    print("Welcome to your Python Pomodoro Marathon  \n")
    
    try:
        study_time = int(input("Kitne minutes ka Focus Session chahiye? "))
        break_time = int(input("Kitne minutes ka Break chahiye? "))
        total_sessions = int(input("Total kitne sessions lagane hain? "))
        
        # Naya Input: Aaj kya padhna hai?
        subject = input("Aaj konsa subject/topic padhna hai? (e.g., Physics - Newton Law of Motion): ")
    except ValueError:
        print("Please sirf numbers type karein!")
        return

    print("\nPress Enter to start your marathon...")
    input()

    for i in range(1, total_sessions + 1):
        print(f"\n\n>>> Starting Session {i} of {total_sessions} <<<")
        
        # Study session ab aapke subject ke naam ke sath aayega
        countdown(study_time, f"Focus Session: {subject}")
        
        # JAISE HI SESSION KHATAM HOGA, FILE MEIN SAVE HO JAYEGA!
        log_session(study_time, subject)
        print(f"\n[+] Session saved to study_history.txt!")
        
        if i < total_sessions:
            countdown(break_time, "Short Break: Screen se aakhein hata lo!")
        else:
            print("\n=== Boom! All sessions complete. Mission 2026 ke ek kadam aur paas! ===")
            print("\a\a\a")

if __name__ == "__main__":
    main()