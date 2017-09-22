/*
Owner:tushar2899
SnakeNladder1.0
*/

#include<iostream>//header file
using namespace std;//standard library
#include<cstdlib>//Header file for random function

class field{// class field consisting operations related to each individual cell on the game board
	public://access specifier
		int cell_no;//variable cell number consisting number hold by each individual cell on board
		field* next;//pointer variable consisting next cells address
		field* prev;// pointer variable consisting prev. cells address
		field(){//constructor
			cell_no=0;
			next=NULL;
			prev=NULL;
			
		}
	
};
class snake_n_ladder{// class snake_n_ladder consiting data variables and member functions asscociated with game
	public://access specifier
		field* player1;//pointer variable consisting player1 position node address 
		field* player2;//pointer variable consisting player2 position node address
		field* start;//pointer pointing cell 1
	
		int score, dice_no, new_score, intrim_score;//declaring variable score, dice_no,new_score, intrim_score for game operations
		snake_n_ladder(){//constructor for snake_n_ladder class
			player1=NULL;
			player2=NULL;
			start=NULL;
			score=1;
			dice_no=6;
			new_score=0;
			intrim_score=0;
		}
		
		void build(){//function start_game for creating game board
			for(int i=1;i<=100;i++){//initializing for loop for developing field till 100
				field* new_Field= new field;//creating new field
				field *temp;// pointer variable temp
				if(start==NULL){//case if field 1 has not been created
					start=new_Field;
					start->next=NULL;
					start->prev=NULL;
					start->cell_no=i;
				}
				else{//incase field 1 exists
					temp=start;//assigning temp as head node
					while(temp->next!=NULL){//iterating temp to reach the last field created
						temp=temp->next;
					}
					temp->next=new_Field;
					new_Field->prev=temp;
					new_Field->cell_no=i;//assigning cell number
				}
			}
		}
		void display_board(){//function display_board for displaying board, threats and ladders
			for(int i=100;i>=91;i--){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=81;i<=90;i++){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=80;i>=71;i--){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=61;i<=70;i++){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=60;i>=51;i--){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=41;i<=50;i++){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=40;i>=31;i--){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=21;i<=30;i++){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=20;i>=11;i--){
				cout<<" "<<i;
			}
			cout<<endl;
			for(int i=1;i<=10;i++){
				cout<<"  "<<i;
			}
			cout<<endl<<"--------------------------------------------";
			cout<<endl<<endl<<"Gamers Attention plz....!!!!!!!";
			cout<<endl<<endl<<"Snakes position:";
			cout<<endl<<endl<<"Snake.1: 27 - 7";
			cout<<endl<<"Snake.2: 39 - 3";
			cout<<endl<<"Snake.3: 35 - 5";
			cout<<endl<<"Snake.4: 50 - 34";
			cout<<endl<<"Snake.5: 59 - 46";
			cout<<endl<<"Snake.6: 66 - 24";
			cout<<endl<<"Snake.7: 73 - 12";
			cout<<endl<<"Snake.8: 97 - 86";
			cout<<endl<<"--------------------------------------------";
			cout<<endl<<"Ladders position:";
			cout<<endl<<endl<<"Ladder.1:  2 - 23";
			cout<<endl<<"Ladder.2:  7 - 29";
			cout<<endl<<"Ladder.3: 22 - 41";
			cout<<endl<<"Ladder.4: 28 - 77";
			cout<<endl<<"Ladder.5: 54 - 69";
			cout<<endl<<"Ladder.6: 70 - 90";
			cout<<endl<<"Ladder.7: 80 - 83";
			cout<<endl;
		}
	
		
		int dice(){// function dice for generating random integer b/w 1 to 6
			return(rand()%6+1);
		}
		int check_post(int scores){//function check_post for checking threats and ladders at position scores
			switch(scores){
				case 2:{//ladder 1
					return 23;
					break;
				}
				case 7:{//ladder 2
					return 29;
					break;
				}
				case 22:{//ladder 3
					return 41;
					break;
				}
				case 28:{//ladder 4
					return 77;
					break;
				}
				case 54:{//ladder 5
					return 69;
					break;
				}
				case 70:{//ladder 6
					return 90;
					break;
				}
				case 80:{//ladder 7
					return 83;
					break;
				}
				case 27:{//snake 1
					return 7;
					break;
				}
				case 39:{//snake 2
					return 3;
					break;
				}
				case 35:{//snake 3
					return 5;
					break;
				}
				case 50:{//snake 4
					return 34;
					break;
				}
				case 59:{//snake 5
					return 46;
					break;
				}
				case 66:{//snake 6
					return 24;
					break;
				}
				case 73:{//snake 7
					return 12;
					break;
				}
				case 97:{//snake 8
					return 86;
					break;
				}
				default:{//if snake nor ladder not found position remains same
					return scores;
					break;
				}
			}
			
			
			
		}
		int dice1(){//function dice1 for tossing who will start first
			return(rand()%2+1);
		}
		void play2(string player1_0, string player2_0){// function play2 for playing of 2 players
			//initializing both the players at start that is position 1
			player1=start;
			player2=start;
			
			int toss=dice1();//tossing
			cout<<endl<<"Let's begin time for the toss";
			cout<<endl<<"!!!!!!!!************ALL THE BEST***************!!!!!!!!";
			if(toss==1){//displaying toss result
				cout<<endl<<player1_0<<" Won the toss";
			}
			else{
				cout<<endl<<player2_0<<" Won the toss";
			}
			int throws;// for storing user response to continue operations
			do{
				int choice_code=toss;//assigning choice_code as toss
				if(choice_code%2==1){//if choice code is odd it's player1 chance
					while(1==1){//for taking response till user enters 1
					cout<<endl<<player1_0<<" Your chance PRESS 1 to throw the dice:";
					cin>>throws;
					if(throws==1){
						break;
					}
					else{
						cout<<endl<<"Invalid Entry";
					}
				}
					dice_no=dice();//storing dice output
					cout<<endl<<"Dice says:\t"<<dice_no;
					score=player1->cell_no;//storing players position in score
					intrim_score=score+dice_no;//adding dice output to score
					if(intrim_score<=100){ //if the position on the board
						cout<<endl<<"Time to move "<<dice_no<<" steps ahead";
						new_score=check_post(intrim_score);//updating to bonuses
						if(intrim_score==new_score){//if positon does not changes
							cout<<endl<<player1_0<<" No Threat detected your position is:"<<new_score;
						}
						else if(intrim_score<new_score){//if position has incremented due to ladder
							cout<<endl<<"WOW!! ladder detected :"<<(new_score-intrim_score)<<" steps earned";
							cout<<endl<<player1_0<<" Your position is :"<<new_score;
						}
						else{//if decremented due to snake
							cout<<endl<<"OOPS!! threat detected snake trap... snake trap..";
							cout<<endl<<"Go back "<<intrim_score-new_score<<" steps..";
							cout<<endl<<player1_0<<" Your position is "<<new_score;
						}
						
						if(score<=new_score){//updaing position on boardif increased or the same
							while(player1->cell_no!=new_score){
								player1=player1->next;
							}
						}
						else{//updating position on the board if position decended
							while(player1->cell_no!=new_score){
								player1=player1->prev;
							}
						}
						if(player1->cell_no==100){//incase player reached 100
							cout<<endl<<"Congratulations "<<player1_0<<" YOU WON!!!!";
							cout<<endl<<"***************************************************************";
							break;
						}
				}
				else{//if score goes more than 100
					cout<<endl<<"Wait"<<player1_0<<" your score can't be more 100";
					cout<<endl<<player1_0<<" Your position remains:"<<player1->cell_no;
				}
				cout<<endl<<"-------------------------------------------------------------------";
			}
			if(choice_code%2==0){//it's player2 chance if choice_code is even
				while(1==1){//for taking response till user enters 1
				cout<<endl<<player2_0<<" Your chance PRESS 1 to throw the dice:";
				cin>>throws;
				if(throws==1){
					break;
				}
				else{
					cout<<endl<<"Invalid Entry";
				}
			}
				dice_no=dice();//storing dice output
				cout<<endl<<"Dice says:\t"<<dice_no;
				score=player2->cell_no;//storing players position in score
				intrim_score=score+dice_no;//adding dice output to score
				cout<<endl<<"Time to move "<<dice_no<<" steps ahead";
				if(intrim_score<=100){//if the position on the board
					new_score=check_post(intrim_score);//updating to bonuses
					if(intrim_score==new_score){//if positon does not changes
						cout<<endl<<player2_0<<" No Threat detected your position is:"<<new_score;
					}
					else if(intrim_score<new_score){//if position has incremented due to ladder
						cout<<endl<<"WOW!! ladder detected :"<<(new_score-intrim_score)<<" steps earned";
						cout<<endl<<player2_0<<" Your position is "<<new_score;
					}
					else{//if decremented due to snake
						cout<<endl<<"OOPS!! threat detected snake trap... snake trap..";
						cout<<endl<<"Go back "<<intrim_score-new_score<<" steps..";
						cout<<endl<<player2_0<<" Your position is "<<new_score;
					}
					if(score<=new_score){//updaing position on boardif post. increased or the same
						while(player2->cell_no!=new_score){
							player2=player2->next;
						}
					}
					else{//updating position on the board if position decended
						while(player2->cell_no!=new_score){
							player2=player2->prev;
						}
					}
					if(player2->cell_no==100){
						cout<<endl<<"Congratulations "<<player2_0<<" YOU WON!!!!";
						cout<<endl<<"***************************************************************";
						break;
					}
				}
				else{//if score goes more than 100
					cout<<endl<<"Wait"<<player2_0<<" your score can't be more 100";
					cout<<endl<<player2_0<<" Your position remains:"<<player2->cell_no ;
				}
				cout<<endl<<"-------------------------------------------------------------------";
			} 
			toss++;
		}while(player1->cell_no!=100 && player2->cell_no!=100);
	}
	void play1(string player1_0, string player2_0="Computer"){// function play1 for playing of 1 player with computer
			//initializing both the players at start that is position 1
			player1=start;
			player2=start;
			
			int toss=dice1();//tossing
			cout<<endl<<"Let's begin time for the toss";
			cout<<endl<<"!!!!!!!!************ALL THE BEST***************!!!!!!!!";
			if(toss==1){//displaying toss result
				cout<<endl<<player1_0<<" Won the toss";
			}
			else{
				cout<<endl<<player2_0<<" Won the toss";
			}
			int throws;// for storing user response to continue operations
			do{
				int choice_code=toss;//assigning choice_code as toss
				if(choice_code%2==1){//it's player1 chance if choice_code is odd
					while(1==1){//for taking response till user enters 1
					cout<<endl<<player1_0<<" Your chance PRESS 1 to throw the dice:";
					cin>>throws;
					if(throws==1){
						break;
					}
					else{
						cout<<endl<<"Invalid Entry";
					}
				}
					dice_no=dice();//storing dice output
					cout<<endl<<"Dice says:\t"<<dice_no;
					score=player1->cell_no;//storing players position in score
					intrim_score=score+dice_no;//adding dice output to score
					if(intrim_score<=100){//if the position on the board
						cout<<endl<<"Time to move "<<dice_no<<" steps ahead";
						new_score=check_post(intrim_score);//updating to bonuses
						if(intrim_score==new_score){//if positon does not changes
							cout<<endl<<"No Threat detected your position is:"<<new_score;
						}
						else if(intrim_score<new_score){//if position has incremented due to ladder
							cout<<endl<<"WOW!! ladder detected :"<<(new_score-intrim_score)<<" steps earned";
							cout<<endl<<"Your position is :"<<new_score;
						}
						else{//if decremented due to snake
							cout<<endl<<"OOPS!! threat detected snake trap... snake trap..";
							cout<<endl<<"Go back "<<intrim_score-new_score<<" steps..";
							cout<<endl<<"Your position is "<<new_score;
						}
						
						if(score<=new_score){//updaing position on boardif increased or the same
							while(player1->cell_no!=new_score){
								player1=player1->next;
							}
						}
						else{//updating position on the board if position decended
							while(player1->cell_no!=new_score){
								player1=player1->prev;
							}
						}
						if(player1->cell_no==100){//incase player reached 100
							cout<<endl<<"Congratulations "<<player1_0<<" YOU WON!!!!";
							cout<<endl<<"***************************************************************";
							break;
						}
				}
				else{//if score goes more than 100
					cout<<endl<<"Wait"<<player1_0<<" your score can't be more 100";
					cout<<endl<<" Your position remains:"<<player1->cell_no;
				}
				cout<<endl<<"-------------------------------------------------------------------";
			}
			if(choice_code%2==0){//it's player2 chance if choice_code is even
				cout<<endl<<"Wait it's Computer's turn:";
				dice_no=dice();//storing dice output
				cout<<endl<<"Dice says:\t"<<dice_no;
				score=player2->cell_no;//storing players position in score
				intrim_score=score+dice_no;//adding dice output to score
				cout<<endl<<"Time to move "<<dice_no<<" steps ahead";
				if(intrim_score<=100){//if the position on the board
					new_score=check_post(intrim_score);//updating to bonuses
					if(intrim_score==new_score){//if positon does not changes
						cout<<endl<<"No Threat detected Computer's position is:"<<new_score;
					}
					else if(intrim_score<new_score){//if position has incremented due to ladder
						cout<<endl<<"WOW!! ladder detected :"<<(new_score-intrim_score)<<" steps earned";
						cout<<endl<<"Computer's position is "<<new_score;
					}
					else{//if decremented due to snake
						cout<<endl<<"OOPS!! threat detected snake trap... snake trap..";
						cout<<endl<<"Go back "<<intrim_score-new_score<<" steps..";
						cout<<endl<<"Computer's position is "<<new_score;
					}
					if(score<=new_score){//updaing position on boardif increased or the same
						while(player2->cell_no!=new_score){
							player2=player2->next;
						}
					}
					else{//updating position on the board if position decended
						while(player2->cell_no!=new_score){
							player2=player2->prev;
						}
					}
					if(player2->cell_no==100){//incase computer reached 100
						cout<<endl<<"Sorry "<<player1_0<<" You lost Computer WON!!!!";
						cout<<endl<<"***************************************************************";
						break;
					}
					}
				}
				else{//if score goes more than 100
					cout<<endl<<"Wait Computer's score can't be more 100";
					cout<<endl<<" Computer's position remains:"<<player2->cell_no ;
				}
				cout<<endl<<"-------------------------------------------------------------------";
			
			toss++;
		}while(player1->cell_no!=100 && player2->cell_no!=100);
	}

		
	
};
int main(){//main function
	int choice;//variable of type integer for storing choice
	int counter=0;//variable of type integer for storing game mode choices
	string play1_0;//player1's name
	string play2_0;//player2's name
	snake_n_ladder game_on;// creating object of snake_n_ladder class
	cout<<endl<<"****SNAKE AND LADDER POWERED BY. wwww.tusharGamingCo.ac.in****";
	cout<<endl<<"           welcome:) to the World of Gaming";
	do{//displaying menu
	
		cout<<endl<<endl<<"Snake and Ladder 3.2.0"<<endl<<"*******MENU*******";
		cout<<endl<<"1.Create Game_board";
		cout<<endl<<"2.Display Game_Board";
		cout<<endl<<"3.Start New Game";
		cout<<endl<<"4.Exit";
		cout<<endl<<"Enter your choice code:";
		cin>>choice;
		switch(choice){//switch statement for menu selection
			case 1:{//for building board
				if(counter==0){//if board has not been created
					game_on.build();//calling function start game
					cout<<endl<<"Board Successfully Created";
					counter=1;
				}
				else{// if already created
					cout<<endl<<"Board already created";
				}
			
				break;
			}
			case 2:{//for displaying game board
				if(counter==1){//only if board has been created earlier
					game_on.display_board();
				}
				else{//if board not created dispaly error message
					cout<<endl<<"Erorr1.0::Board not Built!!!";
				}
			
				break;
			}
			case 3:{// for starting the game
				int mode=0;//variable of type integer for storing mode code
				if(counter==1){//only if board is created
					
					
					do{//for continuous menu
						cout<<endl<<"**CHOOSE mode: **";
						cout<<endl<<"1.Player1 v/s Player2";
						cout<<endl<<"2.Player1 v/s Computer";
						cout<<endl<<"Enter choice code:";
						cin>>mode;
						if(mode==1){//if user selected player1 v/s player2
						
							cout<<endl<<"Player1 enter your Name: ";
							cin>>play1_0;
							cout<<"Player2 enter your Name: ";
							cin>>play2_0;
							game_on.play2(play1_0, play2_0);//calling function play2
							break;//terminating do-while loop
						}
						else if(mode==2){//if user wish to play v/s computer
							cout<<endl<<"Player1 enter your Name:  ";
							cin>>play1_0;
							game_on.play1(play1_0);//calling function play1
							break;
						}
						else{//incase user entered no, other than 1 or 2
							cout<<"inValid choice code";
							cout<<"----------------------------------------------------------";
						}
					}while(true);
						
					}
				
				else{//error messeage i board not created
					cout<<endl<<"Erorr1.0::Board not Built!!!";
				}
				cout<<endl<<"---------------------------------------------------------";
				break;
			}
			case 4:{//exit statements
				cout<<endl<<"....................SEE YOU SOON.........................";
				cout<<endl<<"     This game was powered by www.tusharGamingCo.ac.in  ";
				cout<<endl<<"sponsered by: MIT Academy of Engineering in association with IBM";
				break;
			}
			default:{//if user entered code other than 1,2,3 or 4
				cout<<endl<<"invalid choice code";
				break;
			}
			
		}
		cout<<endl<<"-------------------------------------------------------------";
}while(choice!=4);
	
	
	return 0;//return value for main function
}

/*Sample Output

****SNAKE AND LADDER POWERED BY. wwww.tusharGamingCo.ac.in****
           welcome:) to the World of Gaming

Snake and Ladder 3.2.0
*******MENU*******
1.Create Game_board
2.Display Game_Board
3.Start New Game
4.Exit
Enter your choice code:1

Board Successfully Created
-------------------------------------------------------------

Snake and Ladder 3.2.0
*******MENU*******
1.Create Game_board
2.Display Game_Board
3.Start New Game
4.Exit
Enter your choice code:2
 100 99 98 97 96 95 94 93 92 91
 81 82 83 84 85 86 87 88 89 90
 80 79 78 77 76 75 74 73 72 71
 61 62 63 64 65 66 67 68 69 70
 60 59 58 57 56 55 54 53 52 51
 41 42 43 44 45 46 47 48 49 50
 40 39 38 37 36 35 34 33 32 31
 21 22 23 24 25 26 27 28 29 30
 20 19 18 17 16 15 14 13 12 11
  1  2  3  4  5  6  7  8  9  10
--------------------------------------------

Gamers Attention plz....!!!!!!!

Snakes position:

Snake.1: 27 - 7
Snake.2: 39 - 3
Snake.3: 35 - 5
Snake.4: 50 - 34
Snake.5: 59 - 46
Snake.6: 66 - 24
Snake.7: 73 - 12
Snake.8: 97 - 86
--------------------------------------------
Ladders position:

Ladder.1:  2 - 23
Ladder.2:  7 - 29
Ladder.3: 22 - 41
Ladder.4: 28 - 77
Ladder.5: 54 - 69
Ladder.6: 70 - 90
Ladder.7: 80 - 83

-------------------------------------------------------------

Snake and Ladder 3.2.0
*******MENU*******
1.Create Game_board
2.Display Game_Board
3.Start New Game
4.Exit
Enter your choice code:3

**CHOOSE mode: **
1.Player1 v/s Player2
2.Player1 v/s Computer
Enter choice code:1

Player1 enter your Name: Tushar
Player2 enter your Name: Shivanshu

Let's begin time for the toss
!!!!!!!!************ALL THE BEST***************!!!!!!!!
Shivanshu Won the toss
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
WOW!! ladder detected :22 steps earned
Shivanshu Your position is 29
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Tushar No Threat detected your position is:6
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Shivanshu No Threat detected your position is:34
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
Tushar No Threat detected your position is:12
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 36 steps..
Shivanshu Your position is 3
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Tushar No Threat detected your position is:13
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:4
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Tushar No Threat detected your position is:18
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
WOW!! ladder detected :22 steps earned
Shivanshu Your position is 29
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
Tushar No Threat detected your position is:24
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 30 steps..
Shivanshu Your position is 5
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
Tushar No Threat detected your position is:26
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Shivanshu No Threat detected your position is:9
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
WOW!! ladder detected :49 steps earned
Tushar Your position is :77
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
Shivanshu No Threat detected your position is:15
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
Tushar No Threat detected your position is:79
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
Shivanshu No Threat detected your position is:18
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Tushar No Threat detected your position is:83
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:19
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Tushar No Threat detected your position is:87
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:20
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
Tushar No Threat detected your position is:90
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Shivanshu No Threat detected your position is:24
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Tushar No Threat detected your position is:95
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Shivanshu No Threat detected your position is:29
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Tushar No Threat detected your position is:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
Shivanshu No Threat detected your position is:32
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
Shivanshu No Threat detected your position is:38
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 36 steps..
Shivanshu Your position is 3
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:4
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Shivanshu No Threat detected your position is:9
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
Shivanshu No Threat detected your position is:11
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:12
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Shivanshu No Threat detected your position is:16
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Shivanshu No Threat detected your position is:20
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
Shivanshu No Threat detected your position is:23
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
Shivanshu No Threat detected your position is:25
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Shivanshu No Threat detected your position is:30
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
Shivanshu No Threat detected your position is:33
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
Shivanshu No Threat detected your position is:37
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 36 steps..
Shivanshu Your position is 3
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
WOW!! ladder detected :22 steps earned
Shivanshu Your position is 29
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
Shivanshu No Threat detected your position is:34
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
Shivanshu No Threat detected your position is:40
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
WaitTushar your score can't be more 100
Tushar Your position remains:99
-------------------------------------------------------------------
Shivanshu Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Shivanshu No Threat detected your position is:41
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
Tushar No Threat detected your position is:100
Congratulations Tushar YOU WON!!!!
***************************************************************
---------------------------------------------------------
-------------------------------------------------------------

Snake and Ladder 3.2.0
*******MENU*******
1.Create Game_board
2.Display Game_Board
3.Start New Game
4.Exit
Enter your choice code:3

**CHOOSE mode: **
1.Player1 v/s Player2
2.Player1 v/s Computer
Enter choice code:2

Player1 enter your Name:  Tushar

Let's begin time for the toss
!!!!!!!!************ALL THE BEST***************!!!!!!!!
Tushar Won the toss
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
No Threat detected your position is:6
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
No Threat detected Computer's position is:4
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
No Threat detected your position is:11
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:9
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
No Threat detected your position is:14
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
No Threat detected Computer's position is:13
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
No Threat detected your position is:17
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
No Threat detected Computer's position is:17
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
WOW!! ladder detected :19 steps earned
Your position is :41
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
No Threat detected Computer's position is:20
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
No Threat detected your position is:42
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
No Threat detected Computer's position is:24
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:46
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 20 steps..
Computer's position is 7
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 16 steps..
Your position is 34
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      6
Time to move 6 steps ahead
No Threat detected Computer's position is:13
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 30 steps..
Your position is 5
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:18
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
No Threat detected your position is:6
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
No Threat detected Computer's position is:21
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
No Threat detected your position is:11
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
No Threat detected Computer's position is:24
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:17
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:29
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
No Threat detected your position is:18
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
No Threat detected Computer's position is:33
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
No Threat detected your position is:21
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      2
Time to move 2 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 30 steps..
Computer's position is 5
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 20 steps..
Your position is 7
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:10
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
No Threat detected your position is:10
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:11
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:14
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      6
Time to move 6 steps ahead
No Threat detected Computer's position is:17
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:18
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      6
Time to move 6 steps ahead
No Threat detected Computer's position is:23
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      2
Time to move 2 steps ahead
No Threat detected your position is:20
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:24
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
No Threat detected your position is:21
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:25
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:25
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      3
Time to move 3 steps ahead
WOW!! ladder detected :49 steps earned
Computer's position is 77
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:31
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:78
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:37
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      6
Time to move 6 steps ahead
No Threat detected Computer's position is:84
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      3
Time to move 3 steps ahead
No Threat detected your position is:40
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:89
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      1
Time to move 1 steps ahead
No Threat detected your position is:41
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
No Threat detected Computer's position is:93
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:47
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      4
Time to move 4 steps ahead
OOPS!! threat detected snake trap... snake trap..
Go back 11 steps..
Computer's position is 86
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:51
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:87
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      5
Time to move 5 steps ahead
No Threat detected your position is:56
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:88
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:62
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      1
Time to move 1 steps ahead
No Threat detected Computer's position is:89
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      6
Time to move 6 steps ahead
No Threat detected your position is:68
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      6
Time to move 6 steps ahead
No Threat detected Computer's position is:95
-------------------------------------------------------------------
Tushar Your chance PRESS 1 to throw the dice:1

Dice says:      4
Time to move 4 steps ahead
No Threat detected your position is:72
-------------------------------------------------------------------
Wait it's Computer's turn:
Dice says:      5
Time to move 5 steps ahead
No Threat detected Computer's position is:100
Sorry Tushar You lost Computer WON!!!!
***************************************************************
---------------------------------------------------------
-------------------------------------------------------------

Snake and Ladder 3.2.0
*******MENU*******
1.Create Game_board
2.Display Game_Board
3.Start New Game
4.Exit
Enter your choice code:3

**CHOOSE mode: **
1.Player1 v/s Player2
2.Player1 v/s Computer
Enter choice code:
*/