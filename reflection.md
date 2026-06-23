# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  Firstly, I entered 1 but the hint told me to go lower, which makes no sense because the range is between 1 and 100. Next, I noticed that I was able to enter negative numbers and numbers above 100 which shouldn't be possible. The hints are logically wrong, when I submit a number lower than the secret number, it tells me to go even lower. Whenever I click play a new game and I try to submit a new guess, it just doesn't work. The game seems to break when the user tries to restart. I noticed that the history doesn't show my attempts unless I click submit twice.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input    |Expected Behavior | Actual Behavior | Console Output / Error |
|guess of 1|"Go higher".      |"Go lower".      | none|
|guess of 90|"Go lower".      | "Go higher".    | none|
|clicking new game button| starts a new game | nothing happens| none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude code. When I first asked Claude to fix the logic error in check_guess(), it claimed it did but I played the game and there was no change. So I asked Claude to recheck if it actually implemented the fix.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Firstly I played the game to make sure everything ran was expected. I asked Claude to write a pytest to test if a new game was started when the user clicked new game. This showed me that the original code was broken, specifically the attempts counter, status, and history. I prompted Claude to write tests for different functions.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Session_state is a persistent dictionary that lets you preserve your state and variables because streamlit reruns the python script for every user interaction.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

I want to get into the habit of writing tests for my code or even when coding with AI assistants asking them to check if they actually implemented intended changes. Next time, I'd experiment with different models, perhaps CodeEx and try to build something from scratch using it. I think AI generated code can be a hit or miss, I've heard of stories of vibe coded apps having awful security or being outright illegal. It's ultimately up to the person who's prompting the models to code responsibly with AI.