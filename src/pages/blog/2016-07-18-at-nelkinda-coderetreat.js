import React from "react";
import Page from "../../components/page";
export const data = {
    tags: ['event', 'coding', 'programming', 'test driven deveopment', 'behaviour driven development'],
    desc: 'A review and my feeling about a coding event called as Coderetreat which was held at Nelkinda Software Craft Pvt Ltd. Also, this post describes how the whole event went and how good it was and what someone can possibly learn from a Coderetreat.',
    title: 'At Nelkinda Coderetreat',
    description: 'A review and my feeling about a coding event called as Coderetreat which was held at Nelkinda Software Craft Pvt Ltd. Also, this post describes how the whole event went and how good it was and what someone can possibly learn from a Coderetreat.'
}

export default () => {
    return (
        <Page
        content={
           <div>
               <p>Completely unexpected of what is there, I registered for
                   <a href="http://nelkinda.com/events/2016-07-16-4th-Nelkinda-Coderetreat">Coderetreat that’s held at Nelkinda</a>
                   which was on 16th of July 2016. Facilitated by <a href="https://twitter.com/SiddheshNikude">Siddhesh Nikude</a> and
                   <a href="https://twitter.com/ShwetaSadawarte">Shweta Sadawarte</a> it was a long but a really nice event. More than
                   anything else I got to learn a lot from that event and I will write some of my experience here.</p>
   
               <p>The session was split into code sprints and retrospectives. There was a 45 minute of code sprint followed by a
                   30-minute retrospective. For every code sprint and retrospective cycle, they kept two people to write one code to
                   enforce pair programming. For the first code sprint retrospective cycle, the pairing was done by splitting people
                   into two types, one were the ones who had done TDD before and the others who had not done TDD and/or had heard
                   about TDD before. We were given a problem to solve. The aim of the code sprint was not to solve the given problem
                   but to focus on the practices such as clean code, writing tests and following TDD. We were also free to choose the
                   language of our choice rather than enforcing a language upon us.</p>
   
               <img alt="code_retrospective" class="center" src="/res/images/code_retrospective_nelkinda/code_retrospective_nelkinda.jpg" />
   
               <h4>One of the retrospective, me in yellow telling what happened in the code sprint</h4>
   
   
               <h3>The way the whole event went</h3>
   
               <p>Initially, I was paired with another student who was not very familiar with TDD. I started by introducing him the
                   red-green-refactor cycle. But these are the things that I have learnt on my own and have not worked in an industry
                   and/or done any projects this way to do it the right way. So I was not knowing if I am doing this the right way or
                   not. Finally, at the retrospective session I came to know that I was doing this at least 90% of times the right
                   way. The problem that was given to us was tic tac toe. We had to design a two player tic tac toe game. For eg: if
                   player 1 plays, then, player 2 will play, then the player 1 and it will keep alternating till either of the players
                   wins or if the board is full. So, we started from initially deciding how the board is structured and so on what
                   kinds of methods to use to design this. At the retrospective session, we came to know about each other’s approaches
                   and shared a lot of knowledge about the right way to do things and not so right way to do things. The initial
                   discussion was about what data structure was chosen for the board. The people using Java chose ArrayList the others
                   chose two-dimensional array. I chose Python List since I was using Python as my language.</p>
   
               <p>For every subsequent code sprint, we had to delete the code and start from scratch. The approaches took a totally
                   different turn when the discussion went to the clarity of code in the subsequent code retrospective. The expert
                   programmers started bashing loops and how it makes the code unreadable. Even I like to avoid using loops, esp. in
                   Python it’s really easy to use lambdas and different types of comprehensions. Hence, things that need multiple
                   loops can be reduced to just a couple of lines of readable code.</p>
   
               <p>In between, I switched from Python to Java because I was paired with a person who was unaware of Python and knew
                   only Java. In Java, I had to go through the JUnit framework and tried to use functional programming concepts. As I
                   come from a Python background, I am used to lambdas and comprehensions. I tried to do the same using the Java 8
                   lambdas and ArrayList on which I could run the lambdas. It was a crazy experience and a pretty steep learning curve
                   since I’ve never used lambdas in Java before. Also, my partner was not very comfortable with lambdas and quite a
                   lot of time was spent in both of us learning how it works.</p>
   
               <p>Later I was paired with my friend <a href="https://twitter.com/Mistcrafter">Douglas Vaz</a> who introduced me to a
                   new way of writing code that is BDD. “BDD is TDD done right” this is the statement most of the blogs and or
                   websites all over the internet contain. From what I’ve learnt, in BDD you don’t have to think about the
                   implementation of the feature that you are going to test. Instead, just write a test about the behaviour or the
                   flow of the feature that you are testing and then go on modifying the main code to pass all the tests.</p>
   
               <p>This all was a very wonderful experience, what I’ve written here is barely scratching the surface, in reality, you
                   have to be there to feel the way clean coding is done, esp. when you are paired with others. Finally, we sat and
                   refactored all the code till we finished off the whole problem. The code on tic-tac-toe is really messy in spite of
                   using multiple techniques and hence I’ve decided to rewrite the code in the right way and then post it here or
                   maybe write another blog on that and put the link here.</p>
           </div>
        } />
    )
}
