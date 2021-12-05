<h1>The Snake Game  <img src="https://media3.giphy.com/media/KbUEFowFNOLSAsHT7u/giphy.gif?cid=ecf05e47511r4uttayzwitfjif67w9se04hg6jlc2ss4xhij&rid=giphy.gif&ct=s" width="75"></h1>
<p>Classic <a href="https://en.wikipedia.org/wiki/Snake_(video_game_genre)">Snake Game</a> coded in Python using the <a href="https://docs.python.org/3/library/turtle.html"> Turtle module</a>.<br><br>
Concepts include: OOP (Class, Inheritance), turtle module, List, Tuple, Loops, Slicing.</p>

<h2>About the Game 👾 </h2>
<p>Honestly this section is just a formality, not a single soul, who doesn't know about this game exists. Well if you are one rare gem, living under the rock, let me help you pick it up and shine some light on you.<img src="https://media1.giphy.com/media/5TKJMlt11zlgFi52CZ/giphy.gif?cid=ecf05e47of6829a0r43qg4gm5z4a9ygeowmykwxds5g3mvjx&rid=giphy.gif&ct=s" width="50">
<br></p>

- The player controls a long, thin creature, resembling a snake, which roams around on a bordered plane, picking up food (or some other item), trying to avoid hitting its own tail or the "walls" that surround the playing area.
- Each time the snake eats a piece of food, its tail grows longer, making the game increasingly difficult.
- The user controls the direction of the snake's head (up, down, left, or right), and the snake's body follows. The player cannot stop the snake from moving while the game is in progress.
- The final score is based on the food eaten by the snake.

<div align="center">
<img src="https://github.com/Sikta2002/Snake-Game-Using-Python/blob/main/Img1.png" width="400" height="350">
</div>

<h2>Setup <img src="https://camo.githubusercontent.com/63371d36886ee658f5a97401f393e1ab1684b2fd3de674b8f5efc7d410b2a3d0/68747470733a2f2f6d656469612e67697068792e636f6d2f6d656469612f57556c706c634d704f43456d5447427442572f67697068792e676966" width= "50"></h2>
<div align="center">
<table>
  <tr>
    <th>main.py</th>
    <th>scoreboard.py</th>
    <th>snake.py</th>
    <th>food.py</th>
  </tr>
  <tr>
    <td align="center"><img src="https://media2.giphy.com/media/IzvZmVKH1rgkeZ7QUr/giphy.gif?cid=790b7611493fdbb6f6ffcd9ac9c2121da27f082b8b2308aa&rid=giphy.gif&ct=s" width="90"></td>
    <td align="center"><img src="https://media4.giphy.com/media/JpqVNHqb72TDUgwoSq/giphy.gif?cid=ecf05e47kdgodbw9o6lne4ffvh72wg4xn86lbntisx6nuahb&rid=giphy.gif&ct=s" width="90" align="center"></td>
    <td align="center"><img src="https://media1.giphy.com/media/XzM8kUtzwZV4ywN5ta/giphy.gif?cid=ecf05e47xfxs292syc3pnab1e9pjmaer51guba4c9bz9w97c&rid=giphy.gif&ct=s" width="90"></td>
    <td align="center"><img src="https://media3.giphy.com/media/bX1DoTLLNj7Y4bWq3a/giphy.gif?cid=ecf05e47x9u339d2aab8x32z0bg3rglmr0mq22iv75wp4cfr&rid=giphy.gif&ct=s" width="90"></td>
  </tr>
</table>
</div>
<h2>Let's Build 🏗️</h2>
<h3>Task - 0 🛠️ Let's get ready ! <img src="https://media3.giphy.com/media/jVI7aSgbflOHVEzVDD/giphy.gif?cid=ecf05e47ccmzw80220r7ifv9qzg5ilwytnxuvsvnn0ouhb7m&rid=giphy.gif&ct=s" width="50"></h3>

- In the main.py, we import the Screen class from the turtle module, set up the screen size (600 X 600), make the background color black and set a title for the screen.

<h3>Task - 1 🛠️ Create a snake body : <img src="https://media3.giphy.com/media/Sw14xev09vWveK4OsJ/giphy.gif?cid=ecf05e477dqf6tp90xurhtp8nrbeualfkdmbboy4aexs8p70&rid=giphy.gif&ct=s" width="50"></h3>

- Aim is to create a starting snake body (using 3 turtles lined up next to each other). We also need to extend our snake body every time it eats food, which we will deal with later in another task.
- In the snake.py under the Snake class, we create a new segment (shape = square, color = white).
- We need to position the squares next to each other, for that we create a list STARTING_POSITIONS as constant, containing tuples representing the position of each square.
- We append the new_segment to the segments list.

<h3>Task - 2 🛠️ Move the snake : <img src="https://media3.giphy.com/media/cZRV5iQPg7dh2Ffsgg/giphy.gif?cid=790b7611a1fa2708942f22fe728d4350b9975da4452ac4ce&rid=giphy.gif&ct=s" width ="60"></h3>

- Goal is to move our snake automatically across the screen without having to do anything.
- One might think of an obvious way, i.e. using a while loop to move the turtle forward by a certain distance.
<div align="center">
<img src="https://github.com/Sikta2002/Snake-Game-Using-Python/blob/main/Img2.png" width="400" height="350">
</div>

- Just by looking at this we know, this is not the outcome we are aiming for. We go ahead by first pulling the penup (to disperse the drawn line).
- We use the <a href = "https://docs.python.org/3.3/library/turtle.html?highlight=turtle#turtle.tracer">tracer, update,</a> and <a href = "https://www.journaldev.com/15797/python-time-sleep">sleep (time module)</a> to make the segments move together in a straight path (and not piece by piece).
- We might think that we have successfully made our snake move forward, but not yet. We need to link our segments together cause, when we change direction, all segments will act independently.<br>
To fix this, we can use the concept of moving forward, as in our 3rd segment can to move to the position of the 2nd segment, 2nd to the 1st and the 1st to a new forward position. For this we are going to create a for loop in<br>
<p align="center"><b>range(start = len(self.segments) - 1, stop = 0, step = -1)</b></p>

- Move method (snake.py) tells the last segment to move to the position of the 2nd last segment and so on. 

<h3>Task - 3 🛠️ Control the snake : <img src="https://media4.giphy.com/media/ej15KjYzfDdxckdVS2/giphy.gif?cid=790b7611baa63c79d6f2932b30622b0837c5e02169e37d32&rid=giphy.gif&ct=s" width ="40"></h3>

- We control the snake by using the concept of key binding which is going to get the screen to listen for Up, Down, Left ,and Right keystrokes. It is going to call the desired methods in the snake class.
- We need to consider the exception that the snake can't go back on itself. The head is not permitted to change to opposite directions as in the official snake game. 

<h3>Task - 4 🛠️ Detect collision with food :  <img src="https://media3.giphy.com/media/l0ExqU7rlzaFUSicw/giphy.gif?cid=790b76113a78af591eb48d64132d5a9e4f4e4857a98b620c&rid=giphy.gif&ct=s" width ="50"></h3>

- We make our Food class (food.py) to inherit from the turtle class, such that the food class posses all the capabilities of the turtle class, along with additional properties, such that it behaves like an actual piece of food. We use the concept of inheritance.
- We define the methods shape, shapesize (10 X 10), penup, color, speed(fastest), goto etc.
- Additionally, we use the random module to generate food at a random position within the screen dimension (refresh method).
- We use the distance method to check if the distance between the head of the snake & the food are less than a certain amount, then it is pretty likely that the snake head is now colliding with the food. Everytime this happens, we call the refresh method from the food class.

<h3>Task - 5 🛠️ Create a scoreboard & keep score :<img src="https://media3.giphy.com/media/eerYQwIuHp36dV5Umk/giphy.gif?cid=ecf05e47ajxkza7khy9ggdlvd6t58v64ardbm1p606szsst3&rid=giphy.gif&ct=s" width="70"></h3>

- We desire to write some text in our program that keeps track of the score, of how many pieces of food we have actually managed to eat.
- We make our Scoreboard class (scoreboard.py) to inherit from the turtle class.
- With the help of write(), we can print the score. clear() is used to prevent the score from writing on top of the previous scores, everytime it gets updated.
- We use the functions update_scoreboard() & increase_score().

<h3>Task - 6 🛠️ When should the game end ? <img src="https://media0.giphy.com/media/8v7YgcIe9S676Y5486/giphy.gif?cid=ecf05e47g56xs9upztytvv3iyx6v6hy4oa2r2z56o7snooyo&rid=giphy.gif&ct=s" width="50"></h3>
<h4>Task - 6.1 🛠️ Detect collision with wall : <img src="https://media3.giphy.com/media/3EkGMb61KiDdC7PmhM/giphy.gif?cid=ecf05e47y7eexb0ma5s9hc1vhdckna4tfd6ty2l3u9bd1b28&rid=giphy.gif&ct=s" width="85"></h4>

- Aim is to create a boundary along the screen dimension, such that as soon as the snake head touches that position, it should detect collision, hence game over.
- With the help of xcor() & ycor(), we create a boundary. When the snake hits the boundary, basically meaning the snake has hit the wall, the game_is_on flag is set to false.
- We use the game_over method (scoreboard.py), inorder to display "GAME OVER" message on the screen.
<div align="center">
<img src="https://github.com/Sikta2002/Snake-Game-Using-Python/blob/main/Img3.png" width="400" height="350">
</div>

<h4>Task - 6.2 🛠️ Detect collision with tail : <img src="https://media2.giphy.com/media/L4aQFYRCkz4DVKPHpk/giphy.gif?cid=790b7611c247db66c11afeda6783ae1a4d642ca695e06100&rid=giphy.gif&ct=s" width="50"></h4>

- We need to figure out how to detect when the snake collides with its own tail.

<h4>Hold up ! We are yet to figure out "how to make my snake grow longer ? "<img src="https://media1.giphy.com/media/1yNfVG94Zuy2Rqt6My/giphy.gif?cid=790b761166ad353e76e104d2134afc7d3c5f280f1ac7a8c1&rid=giphy.gif&ct=s" width="65"></h4>
<p>In the snake game, the snake gets longer each time it eats food. As the snake gets longer & longer, its more likely that at some point, the head might hit some part of the tail. This means "GAME OVER". Hence, first we need to extend the snake everytime it eats.</p>

1. In the snake.py, we create extend(), which gets hold, the position of the last segment using the segments list. It is in this position where a new segment gets added. 
2. In the main.py, everytime snake head collides with the food, not only do we refresh the food, but also call the extend(), inorder to extend the snake.

<h4>Let's get back to tail collision :  <img src="https://media3.giphy.com/media/60XzbpMZMF4yYr88BK/giphy.gif?cid=ecf05e47d78vbcgdhc820rc8jez8y8oto0sa898qbsw9rr69&rid=giphy.gif&ct=s" width="75"></h4>

- In the main.py, using the slicing concept on our segments list, we get hold of everything that starts off at position 1 till the end.
- Then we can use that segment to loop through it & then check every segment in the tail against the distance to the head.
- We do not start from position 0 as we don't want to check head colliding with itself.
<div align="center">
<img src="https://github.com/Sikta2002/Snake-Game-Using-Python/blob/main/Img4.png" width="400" height="350">
</div>

<h4 align = "center"><img src="https://media0.giphy.com/media/jpEE9SqP7NAVyK87EQ/giphy.gif?cid=ecf05e472a170odx1xlz2phyfhyhc1xir42jangj5f7srey7&rid=giphy.gif&ct=s" width="70">OUR GAME IS READY !<img src="https://media0.giphy.com/media/jpEE9SqP7NAVyK87EQ/giphy.gif?cid=ecf05e472a170odx1xlz2phyfhyhc1xir42jangj5f7srey7&rid=giphy.gif&ct=s" width="70"></h4>
<h2>Things we learnt 🕮️</h2>

- How to break down a large project into smaller different tasks, making the project easier to understand and implement. 🧐
- How amazing the turtle module is ! 🐢
- How Object - Oriented Programming concepts make our lives easier. 😝
- How the <b>Snake Game</b> can never get old. ✨

<h3 align = "center">🏃 Will add more features soon 🏃<br><br>🦄 Thanks for Visiting ! 🦄</h3>
