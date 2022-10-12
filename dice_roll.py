//Simulation program to estimate the winning chance of the Craps game.
/*Author: Ricky Vidals
  CIS 3100 BMWA Spring 2019
  Assignment 3*/
#include <iostream>
#include <ctime>
#include <cstdlib>
using namespace std;

int main()
{
	const int MIN_VALUE = 1, MAX_VALUE = 6, GAMES = 10000;
	int die1, die2, first_dice_rolled;
	double winning_chance, wins, losses;

	unsigned seed = time(0);
	srand(seed);

	wins = 0.0;
	losses = 0.0;

	for (int play = 1; play <= GAMES; play++)
	{
		die1 = (rand() % (MAX_VALUE - MIN_VALUE + 1)) + MIN_VALUE;
		die2 = (rand() % (MAX_VALUE - MIN_VALUE + 1)) + MIN_VALUE;
		first_dice_rolled = die1 + die2;

		if ((first_dice_rolled == 2) || (first_dice_rolled == 3)) 
			losses++;
		else if (first_dice_rolled == 12)
			losses++;
		else if ((first_dice_rolled == 7) || (first_dice_rolled == 11))
			wins++;
		else
		{
			bool start = true;
			int established_point = first_dice_rolled;
			int dice_rolled;
			while (start)
			{
				die1 = (rand() % (MAX_VALUE - MIN_VALUE + 1)) + MIN_VALUE;
				die2 = (rand() % (MAX_VALUE - MIN_VALUE + 1)) + MIN_VALUE;
				dice_rolled = die1 + die2;

				if (dice_rolled == established_point)
				{
					wins++;
					start = false;
				}
				else if (dice_rolled == 7)
				{
					losses++;
					start = false;
				}
			}
		}    

	}
	winning_chance = (wins / GAMES) * 100;
	cout << "Played " << GAMES << " games.\n";
	cout << "Your winning chance for those games was " << winning_chance << "%\n";
	return 0;
}