from pet import Pet

def main():
    # Create a new pet
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    print(f"\nWelcome to Pet Simulator! You have adopted {pet_name}.")
    
    # Main interaction loop
    while True:
        print("\n--- What would you like to do? ---")
        print("1. Feed your pet")
        print("2. Let your pet sleep")
        print("3. Play with your pet")
        print("4. Check pet status")
        print("5. Train your pet")
        print("6. Show pet's tricks")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            my_pet.get_status()
        elif choice == '5':
            trick = input("What trick would you like to teach? ")
            my_pet.train(trick)
        elif choice == '6':
            my_pet.show_tricks()
        elif choice == '7':
            print(f"Goodbye! Take care of {pet_name}!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()