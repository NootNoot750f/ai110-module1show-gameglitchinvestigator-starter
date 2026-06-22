# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The issues that I noticed were

1. When hitting the reset button, it didnt work, like it would say at the top that
   there were more attempts, but in the dev notes it showed 0. The expected behavior is that
   the screen would reset and I would be able to play the game again.
2. The secret number was 65, but when I when I attempted:
   50 = Go Lower!
   25 = Go Lower!
   12 = Go Lower!
   6 = Go Lower!
   3 = Go Lower!
   1 = Go Lower!
   0 = Go Lower!
   When you submit a number below the secret number, it says GO LOWER
   But when you do a number above, it says GO HIGHER! So it is telling you to do the opposite thing. The expected behavior was to say Go Lower! when the number was lower and Go Higher! when the number was higher.

3. The score becomes more and more negative with each attempt. The expected behavior is for the score to stop at 0

4. When doing the correct number, you need to submit the number 2x times. The expected behavior is for when submitting the number you need click the button only once.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                                     | Expected Behavior                                                      | Actual Behavior                                                                             | Console Output / Error |
| --------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | ---------------------- |
| Reset Button                                              | Screen resets and game restarts with full attempts                     | Attempts counter displayed more attempts, but dev notes showed 0; game did not reset        | None                   |
| Guess below secret number (e.g., secret = 65, guess = 50) | "Go Higher!" when guess is too low, "Go Lower!" when guess is too high | Directions are inverted — guessing low says "Go Lower!" and guessing high says "Go Higher!" | None                   |
| Score after multiple wrong attempts                       | Score stops decrementing at 0                                          | Score continues into negative values with each attempt                                      | None                   |
| Submitting the correct number                             | Game registers win on first submission                                 | Correct number must be submitted twice before the game recognizes it                        | None                   |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  That the logic was backwards, with the guess > secret return too high go higher! It was able to correctly identifty the logic issue in the code. I verified this by going into the code and seeing the logic issue. Then I used the suggestion and changed the code, then ran and played the game to make sure it worked.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When we were debugging why when the game over displayed when you had one attempt left, we were arguing over the logic of >= over > or adding 1 to the comparison. However what Claude didn't recognize that I did is that the results were displaying before the calculation happened, so it was behind and delayed. Also, there were 2 game over messages, which claude did not flag. I told it to combine them and put them at the end. This solved the issue of telling game over with one attempt left, as well as not registering the correct amount of attempts, due to the update happening in the cycle after the button was clicked, not in the same cycle.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I played the game to make sure that it worked as intented and that the bug was fixed. For example I would make sure that when I submitted each guess, I would count my own clicks to make sure that it was accepting 8 entries before displaying gameover.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  When the pytests ran, they displayed that all 5 ran without fault

- Did AI help you design or understand any tests? How?
  I already have some knowledge about tests from C++, and I applied it here. I asked claude to explain to me the syntax for these python tests and how it worked, then I ran the code by hand in my head, to make sure that the logic made sense.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

  Streamlit is like a python script that runs in yuor browser. Streamlit reruns the script from the very top, which means that it just starts over, like a fresh copy of the program every time you interact with it. But since it resets each time, you wouldnt be able to store any data, things would always start at 0. This is where session states come in. Session states are like allocated memory for the user's session. When you store a value in st.session_state Streamlit keeps it stored despite having reruns.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  To double check the code that Claude gives, and if I am trying to debug with it, and it still isn't fixing the issue, why. Like earlier I was like "Hmm there is something that Claude is not seeing" and I was right, it didn't detect the issue of having 2 game over messages instead of one since it didn't
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
  I think that I would provide more context. When we were trying to debug I would tell it what's happening and it would get confused or just make non meaningful changes. If I add more context in a structured way, less tokens could be used and we could progress faster.

- In one or two sentences, describe how this project changed the way you think about AI generated code.
  That it definetly needs to be monitored. When I was looking over what it was doing, I realized that it could definetly just be wrong. It's not some all knowing being. AI models are trained on correct things, but they also can learn from wrong things or wrong practices, which is why it's important for me to learn how things work, so that I can make sure that I can catch if an AI is doing something wrong. AI is more of an accelerator, you don't need to write everything perfectly by hand anymore, all the syntax and small things, you can (if you really want) just monitor outputs, make sure they're correct, and continue.
