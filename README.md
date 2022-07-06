# 100 Prisoners Escape Puzzle
*Inspiration taken from* https://www.youtube.com/watch?v=iSNsgj1OCLA <br>
*Description taken from* https://datagenetics.com/blog/december42014/index.html <br>
*I encourage anyone interested in this to check out these sources for further analysis into the probability and underlying math behind the solution*


In this puzzle there are 100 prisoners, each given a distinct number 1-100. The jailer has decided to give all the prisoners a chance to escape. He prepares a challenge, and if every single one of the prisoners passes, they are all free to go. If even one of them fails, they all die.

## The Challenge

The jailer goes into a secret room and prepares 100 boxes with lids. He labels these boxes 1-100. Then he prepares 100 tickets, one for each prisoner, and labels these tickets 1-100. Finally, he shuffles the tickets thoroughly, and puts one ticket in each box, closing the lid behind it. The prisoners cannot see any of these preparations.
<img width="790" alt="Screen Shot 2022-07-05 at 7 20 13 PM" src="https://user-images.githubusercontent.com/62193488/177432493-56f1f411-dbc0-4061-9240-f993b22671ca.png"> 
<img width="165" alt="Screen Shot 2022-07-05 at 7 21 55 PM" src="https://user-images.githubusercontent.com/62193488/177432657-a164090c-ea9b-490f-8367-c51aea0ac161.png"> <br>
The challenge is now on. He fetches each prisoner, one-by-one, into the box room and tells the prisoner that they must find the box that contains their ticket. They attempt to do this by opening boxes. They are allowed to open up to half the boxes in their search. If they succeed in finding their own number, they win. If they have not found their ticket after examining 50 boxes, they fail.
In order for the prisoners to escape, all prisoners have to win. What are their chances of escape?

After opening a box and examining its contents, the lid is closed again. The position of tickets cannot be changed. No messages can be left behind for prisoners yet to come to decode.

The prisoners are allowed to confer before the challenge begins. What is their optimal strategy?

## Pretty Unlikely
At first glance, this seems a pretty hopeless problem. In fact, it appears that the chances of all the prisoners finding their own tickets is microscopically small. After all, there is no way for the prisoners to communicate any information to each other.

With just one prisoner, he has a 50:50 chance. There are 100 boxes, and he gets to open (up to) 50 boxes looking for his ticket. If he opens the boxes at random he’ll open half the boxes, and his ticket will, or, will not be in the half he opens. His chance of success is ½.

With two prisoners, if both select at random, it would also by ½ chance of success each, so for two prisoners, it is ½ × ½ = ¼.
(They will succeed one time in four).


For three prisoners it’s ½ × ½ × ½ = ⅛.


With 100 prisoners, it’s ½ × ½ × … ½ × ½ (100 times).


This is:

Pr ≈ 0.000000000000000000000000000008

That’s a pretty small chance. It appears as though the prisoners are as good as dead.

## Solution
The strategy is amazingly simple. First of all you open up the box corresponding to your own number. If you find your ticket, great!, if not you look up the number on the ticket in your box and that is the box your check next. You carry on this strategy … daisy-chaining your way through the boxes. That's it! <br>
<img width="768" alt="Screen Shot 2022-07-05 at 7 28 04 PM" src="https://user-images.githubusercontent.com/62193488/177433223-a08d92eb-566b-4dd4-82bb-4d302a1a06e9.png"> <br>

31.18% of the time, the length of the maximum chains formed will be less than 50 boxes and so every prisoner will be able to find his ticket before hitting the 50 box limit.

# *The probability of all the prisoners getting their ticket is 31.18%*

## On to the Code

To run the program as is, there are no third party packages needed <br> 
change directories to file and run *I am using macOS* <br>

(base) andybialy$ *python3 prisoners.py* <br>
Percent of time all 100 prisoners were correct with 50 guesses over 100 runs: <br>
32.0% <br>

You can alter the runs however you like with: <br>
-p to change the amount of prisoners, default=100 <br>
-g to change the amount of guesses each prisoner gets to find their number, default=50 <br>
-r to change the number of runs, default=100 <br>

(base) andybialy$ python3 prisoners.py -p 100 -g 75 -r 200 <br>
Percent of time all 100 prisoners were correct with 75 guesses over 200 runs: <br>
71.5% <br>
