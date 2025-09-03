import datetime
import json
import os

# File jisme attendance data save hoga
FILE_NAME = "attendance.json"

# Agar file exist nahi karti to nayi file bana lo
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump({}, f)

# Load data
def load_data():
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Student add karna
def add_student(name):
    data = load_data()
    if name not in data:
        data[name] = {"attendance": []}
        save_data(data)
        print(f"✅ Student '{name}' added successfully!")
    else:
        print("⚠️ Student already exists!")

# Attendance mark karna
def mark_attendance(name, status):
    data = load_data()
    if name in data:
        today = str(datetime.date.today())
        data[name]["attendance"].append({"date": today, "status": status})
        save_data(data)
        print(f"📌 Attendance marked for {name} on {today} as {status}")
    else:
        print("⚠️ Student not found!")

# Attendance report
def show_report(name):
    data = load_data()
    if name in data:
        records = data[name]["attendance"]
        total = len(records)
        present = sum(1 for r in records if r["status"] == "P")
        percentage = (present / total) * 100 if total > 0 else 0
        print(f"\n📊 Report for {name}:")
        print(f"Total Days: {total}")
        print(f"Present: {present}")
        print(f"Attendance %: {percentage:.2f}%\n")
    else:
        print("⚠️ Student not found!")

# Main menu
def main():
    while True:
        print("\n=== Attendance Manager ===")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Show Report")
        print("4. Exit")

        choice = input("👉 Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(name)

        elif choice == "2":
            name = input("Enter student name: ")
            status = input("Enter status (P/A): ").upper()
            if status in ["P", "A"]:
                mark_attendance(name, status)
            else:
                print("⚠️ Invalid status! Use P for Present, A for Absent.")

        elif choice == "3":
            name = input("Enter student name: ")
            show_report(name)

        elif choice == "4":
            print("👋 Exiting Attendance Manager...")
            break

        else:
            print("⚠️ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
