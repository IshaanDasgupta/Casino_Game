#include <bits/stdc++.h>
using namespace std;

map<string, string> getPassword;
map<string, int> getCoins;
bool gameOn = true;
string currentEmail;

void gameStart()
{
    bool stillPlaying = true;
    if (stillPlaying)
    {
        cout << "Guess the color of the casino chip (Red or Black)\n";
        int randomNum = rand();
        randomNum %= 2;
        string userString;
        cin >> userString;
        int userInput = 0;
        if (userString == "Red")
        {
            userInput = 1;
        }

        cout << "Enter the ammount you want to bet\n";
        int ammount;
        cin >> ammount;

        if (getCoins[currentEmail] == 0)
        {
            cout << "You dont have enough balance to bet\n";
        }
        else
        {
            if (ammount >= getCoins[currentEmail])
            {
                ammount = getCoins[currentEmail];
                cout << "Betting all coins\n";
            }

            if (randomNum == userInput)
            {
                cout << "You gussed correctly\n";
                cout << "You won " << ammount << " coins\n";
                getCoins[currentEmail] += ammount;
                cout << "Your current coins are : " << getCoins[currentEmail] << "\n";
            }
            else
            {
                cout << "Your Guess was wrong\n";
                cout << "You lost " << ammount << " coins\n";
                getCoins[currentEmail] -= ammount;
            }
        }
        cout << "------------------------------------------\n";
        cout << "1 to play again\n";
        cout << "2 to add balance\n";
        cout << "3 to signout and quit\n";
        cout << "------------------------------------------\n";

        int operation;
        cin >> operation;
        if (operation == 2)
        {
            addCoins(currentEmail);
        }
        if (operation == 3)
        {
            currentEmail = "";
            operationSelector();
        }

        if (stillPlaying)
        {
            gameStart();
        }
    }
    return;
}

void printHighScore()
{
    vector<int> coins;
    for (auto i : getCoins)
    {
        coins.push_back(i.second);
    }

    sort(coins.begin(), coins.end());
    int first = 0, second = 0, third = 0;

    for (int i = coins.size() - 1; i >= max(0, (int)coins.size() - 3); i--)
    {
        if (i == coins.size() - 1)
        {
            first = coins[i];
        }
        if (i == coins.size() - 2)
        {
            second = coins[i];
        }
        if (i == coins.size() - 3)
        {
            third = coins[i];
        }
    }

    cout << "1st place is at " << first << "\n";
    cout << "2nd place is at " << second << "\n";
    cout << "3rd place is at " << third << "\n";
    return;
}

void registerUser()
{
    bool registered = false;
    while (!registered)
    {
        cout << "Enter email address or input X to exit\n";
        string enteredEmail;
        cin >> enteredEmail;
        if (enteredEmail == "X")
        {
            return;
        }
        while (!emailValidator(enteredEmail))
        {
            cout << "The previously entred email is invalid please enter a correct email or input X to exit\n";
            string enteredEmail;
            cin >> enteredEmail;
            if (enteredEmail == "X")
            {
                return;
            }
        }
        cout << "Enter password\n";
        string enteredPassword;
        cin >> enteredPassword;
        if (getPassword[enteredEmail] == "")
        {
            cout << "Registration Success\n";
            getPassword[enteredEmail] = enteredPassword;
            getCoins[enteredEmail] = 0;
            registered = true;
            currentEmail = enteredEmail;
            break;
        }
        cout << "This email is alredy under use\n";
        cout << "Please enter another username\n";
    }
    gameStart();
    return;
}

void signInUser()
{
    bool loginedIn = false;
    while (!loginedIn)
    {
        cout << "Enter email address or input X to exit\n";
        string enteredEmail;
        cin >> enteredEmail;
        if (enteredEmail == "X")
        {
            return;
        }
        while (!emailValidator(enteredEmail))
        {
            cout << "The previously entred email is invalid please enter a correct email or input X to exit\n";
            string enteredEmail;
            cin >> enteredEmail;
            if (enteredEmail == "X")
            {
                return;
            }
        }

        cout << "Enter password\n";
        string enteredPassword;
        cin >> enteredPassword;

        if (getPassword[enteredEmail] == enteredPassword)
        {
            cout << "Login Success\n";
            currentEmail = enteredEmail;
            loginedIn = true;
            break;
        }
        cout << "The entred email and password does not match\n";
    }

    gameStart();
    return;
}

void operationSelector()
{
    cout << "------------------------------------------\n";
    cout << "1 to Register\n";
    cout << "2 to Sign in\n";
    cout << "3 to view Leaderboard\n";
    cout << "4 to view Rules\n";
    cout << "5 to get your ranking\n";
    cout << "------------------------------------------\n";

    int operation;
    cin >> operation;
    switch (operation)
    {
    case 1:
        registerUser();
        return;

    case 2:
        signInUser();
        return;

    case 3:
        printHighScore();
        return;

    case 4:
        getRules();
        return;

    case 5:
        cout << "Your current rank is : " << getYourRanking(currentEmail) << " with total coins : " << getCoins[currentEmail];
        return;
    }

    if (gameOn)
    {
        operationSelector();
    }
}

int main()
{
    if (gameOn)
    {
        operationSelector();
    }
    return 0;
}