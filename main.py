import init_db
from skater import Skater

def main():
     
    # add in check to make sure blank database has been created, throw exception if not


     menu_choice = None
     while menu_choice != 5:
            # main menu to control program
            print()
            print("---------------")
            print("MAIN MENU")
            print("---------------")
            print("1: Skater Management")
            print("2: Game Management")
            print("3: GTSC Scoring")
            print("4: System Management")
            print("5: Close Program")

            menu_choice = input()

            if menu_choice == "1":
               skater_menu()            
            elif menu_choice == "2":
                print("opening game menu")
                game_menu()
            elif menu_choice == "3":
                print("opening gtsc menu")
                gtsc_menu()
            elif menu_choice == "4":
                print("opening system menu")
                system_management()            
            elif menu_choice == "5":
                print("closing program")
                break
            else:
                print("choice not recognised, please try again")

def skater_menu():
    skater_menu_choice = None    
    while skater_menu_choice != 0:
        print()
        print("---------------")
        print("SKATER MANAGEMENT")
        print("---------------")
        print("0: Return to main menu")
        print("1: Add new skater (name/number only)")
        skater_menu_choice = input()

        if skater_menu_choice == "0":
            return
        elif skater_menu_choice == "1":
            Skater()

def game_menu():
    game_menu_choice = None    
    while game_menu_choice != 0:
        print()
        print("---------------")
        print("GAME MANAGEMENT")
        print("---------------")
        print("0: Return to main menu")

        game_menu_choice = input()

        if game_menu_choice == "0":
            return
        
def gtsc_menu():
    gtsc_menu_choice = None    
    while gtsc_menu_choice != 0:
        print()
        print("---------------")
        print("GTSC SCORING AND REPORTS")
        print("---------------")
        print("0: Return to main menu")

        gtsc_menu_choice = input()

        if gtsc_menu_choice == "0":
            return
        
def system_management():
    sys_choice = None    
    while sys_choice != 0:
         print()
         print("---------------")
         print("SYSTEM MANAGEMENT")
         print("---------------")
         print("0: Return to main menu")
         print("1: Initialise Database")
         print("2: Run System Tests")
         sys_choice = input()    

         if sys_choice == "0":
            break
         elif sys_choice == "1":
           init_db.setup_tables()
         elif sys_choice == "2":
            print("running system tests")
         else:
            print("Choice not recognised")


if __name__ == '__main__':
    main()