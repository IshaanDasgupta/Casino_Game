import random

getPassword = {};
getCoins = {};
gameOn = True;
currentEmail = "";


def addCoins(email):
        
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;

    print("Enter the ammount you wish to add");
    ammount = int(input());
    getCoins[currentEmail] += ammount;

def emailValidator(email):
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    if (email.lower() != email):
        return False;

    atPresent = False;
    for i in email:
    
        if (i == '@'):
            atPresent = True;
    

    if (atPresent == False):
        return False;

    if (len(email) < 5):
        return False;

    n = len(email);
    good = False;
    if (email[n - 3] == '.' and email[n - 2] == 'i' and email[n - 1] == 'n'):
        good = True;

    if (email[n - 4] == '.' and email[n - 3] == 'c' and email[n - 2] == 'o' and email[n - 1] == 'm'):
        good = True;

    return good;


def getRules():
    print("------------------------------------------");
    print("RULES");
    print("This is a game in which you are supposed to guess the color of the casion chip and bet a certain ammount.");
    print("To play this game you must login with a already registered email ID or register a new email ID");
    print("This game also have a leaderboard in which you can see the coins of top players");
    print("------------------------------------------");
    return;

def getYourRanking(email):
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    yourScore = getCoins[email];
    ranking = 1;

    keys = getCoins.keys();

    for key in keys:
        if (yourScore < getCoins[key]):
            ranking += 1;

    return ranking;

def gameStart():
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    stillPlaying = True;
    if (stillPlaying):
        print("Guess the color of the casino chip (Red or Black)");
        colourList = ["Red", "Black"]
        randomColor = random.choice(colourList);
        userString = input();

        print("Enter the ammount you want to bet");
        ammount = int(input());

        if (getCoins[currentEmail] == 0):
            print("You dont have enough balance to bet");
        else:
            if (ammount >= getCoins[currentEmail]):
                ammount = getCoins[currentEmail];
                print("Betting all coins");

            if (userString == randomColor):
                print("You gussed correctly");
                print("You won " , ammount , " coins");
                getCoins[currentEmail] += ammount;
                print("Your current coins are : " , getCoins[currentEmail]);
            else:
                print("Your Guess was wrong");
                print("You lost " , ammount , " coins");
                getCoins[currentEmail] -= ammount;

        print("------------------------------------------");
        print("1 to play again");
        print("2 to add balance");
        print("3 to signout and quit");
        print("4 to get your ranking");
        print("------------------------------------------");

        operation = int(input());
        if (operation == 2):
            addCoins(currentEmail);
        if (operation == 3):
            currentEmail = "";
            operationSelector();

        if operation == 4:
            if (len(currentEmail) == 0):
                print("Please sign in to get your leaderboard ranking");
            else:
                print("Youre current rank is : " , getYourRanking(currentEmail) , " with total coins : " , getCoins[currentEmail]);
            
            gameStart();
        

        if (stillPlaying):
            gameStart();

    return;

def printHighScore():
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    coins = [];

    keys = getCoins.keys();

    for key in keys:
        coins.append(getCoins[key]);
    
    coins.sort();
    first = 0;
    second = 0;
    third = 0;


    i = len(coins) - 1;
    while i>=0:
        if (i == len(coins) - 1):
            first = coins[i];

        if (i == len(coins) - 2):
            second = coins[i];
        
        if (i == len(coins) - 3):
            third = coins[i];
            break;

        i -= 1;
        

    print("1st place is at " , first );
    print("2nd place is at " , second );
    print("3rd place is at " , third );
    return;

def registerUser():
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    registered = False;
    while (registered == False):
        print("Enter email address or input X to exit");
        enteredEmail = input();
        if (enteredEmail == "X"):
            return;
        while (emailValidator(enteredEmail) == False):
            print("The previously entred email is invalid please enter a correct email or input X to exit");
            enteredEmail = input();
            if (enteredEmail == "X"):
                return;
            
        print("Enter password");
        enteredPassword = input();
        if (getPassword.get(enteredEmail) == None):
            print("Registration Success");
            getPassword[enteredEmail] = enteredPassword;
            getCoins[enteredEmail] = 0;
            currentEmail = enteredEmail;
            break;
    
        print("This email is alredy under use");
        print("Please enter another username");
    
    gameStart();
    return;

def signInUser():
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    loginedIn = False;
    while (loginedIn == False):
        print("Enter email address or input X to exit");
        enteredEmail = input();
        if (enteredEmail == "X"):
            return;
        
        while (emailValidator(enteredEmail) == False):
            print("The previously entred email is invalid please enter a correct email or input X to exit");
            enteredEmail = input();
            if (enteredEmail == "X"):
                return;
            

        print("Enter password");
        enteredPassword = input();

        if (getPassword[enteredEmail] == enteredPassword):
            print("Login Success");
            currentEmail = enteredEmail;
            loginedIn = True;
            break;
        
        print("The entred email and password does not match");
    
    gameStart();
    return;

def operationSelector():
    global currentEmail;
    global getPassword;
    global getCoins;
    global gameOn;
    print("------------------------------------------");
    print("1 to Register");
    print("2 to Sign in");
    print("3 to view Leaderboard");
    print("4 to view Rules");
    print("5 to get your ranking");
    print("------------------------------------------");

    operation = int(input());
 
    if operation == 1:
        registerUser();

    if operation == 2:
        signInUser();

    if operation == 3:
        printHighScore();

    if operation == 4:
        getRules();

    if (gameOn):
        operationSelector();

if (gameOn):
    operationSelector();
