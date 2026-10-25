# Disaster Management System

disaster_tips = {
    "earthquake": [
        "Drop, Cover, and Hold On.",
        "Stay away from windows and heavy objects.",
        "When shaking stops, move carefully to a safe place."
    ],
    "flood": [
        "Move to higher ground.",
        "Avoid walking or driving through floodwater.",
        "Follow official evacuation instructions."
    ],
    "cyclone": [
        "Stay indoors and away from windows.",
        "Keep emergency supplies ready.",
        "Follow official weather alerts and evacuation instructions."
    ],
    "fire": [
        "Raise the alarm and leave the building.",
        "Stay low if there is smoke.",
        "Call your local emergency services from a safe location."
    ]
}


def show_disaster_information():
    print("\n--- DISASTER MANAGEMENT SYSTEM ---")
    print("1. Earthquake")
    print("2. Flood")
    print("3. Cyclone")
    print("4. Fire")
    print("5. Exit")


def display_safety_tips(disaster):
    print(f"\nSafety tips for {disaster.title()}:")

    for index, tip in enumerate(disaster_tips[disaster], start=1):
        print(f"{index}. {tip}")


def main():
    options = {
        "1": "earthquake",
        "2": "flood",
        "3": "cyclone",
        "4": "fire"
    }

    while True:
        show_disaster_information()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "5":
            print("Stay safe! Thank you for using the system.")
            break

        disaster = options.get(choice)

        if disaster:
            display_safety_tips(disaster)
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
