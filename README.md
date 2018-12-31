# Pass the Pigs strategy tournament simulator

![screenshot](https://raw.githubusercontent.com/syntaxaire/pigsapp/master/screenshot.png)
Pass the Pigs is a game of rolling pig-shaped dice with uneven side chances. The two pigs can be worth more or less depending on which side they land on, or may force you to lose your turn score by landing on opposite flanks. The object of the game is to reach a score of 100 first.

Some scholarly work has been done on statistical analysis of this game:
[Pig Data and Bayesian Inference on Multinomial Probabilities](http://jse.amstat.org/v14n3/datasets.kern.html)

From the paper above:
> As our final suggestion for further analysis, we point out that sampling from the posterior predictive distribution provides an endless stream of “next roll” scores that can be used to ascertain the effectiveness of any strategy-even those conditional upon the scores of other players. This is perhaps the most engaging analysis for students, as the personal strategy of each student can be combined in a program that simulates an entire game. Several game simulations reveal the student with the most successful strategy.

As suggested in the paper, this app allows you to compete strategies against each other. It's easy to extend with basic Python skills by editing `strategies.py`. In the single-executable version, created with PyInstaller, `strategies.py` is kept outside the `.exe` for easy editing. It's still loaded on startup.

In 1998, a Grade 6 math class [ran and wrote up a strategy tournament](http://passpigs.tripod.com/index.html) that inspired this simulator. The "Jonah", "Morgen", and "Julia" strategies are from these Grade 6 students, and the "Jonah" strategy in particular is capable of easily beating the best built-in "naive" strategy, "Go for 25", which tries to achieve a score of 25 on each turn.

## Strategies to explore
- Can you write a strategy to beat Jonah?
- Basic: The logic of "Go for 25" is a one-line method. Is it possible to write a better strategy that still only checks one thing?
```
def keep_rolling(self):
    return self.turnscore < 25
```
- Advanced: Can you write a program to find the optimal one-line strategy?

## Tips
- You can run more exhaustive tournaments quickly by decreasing the number of
contestants. Try unselecting the weakest strategies to devote more processing
time to worthy opponents.
- Running a small number of tournaments may not find the strongest strategy.
- The default game was designed around a win score of 100. Some strategies 
do handle other values well. In particular, if the win score is too high, 
strategies can deadlock against each other, effectively freezing the match. 
> For example, "Greedy roller" and "Julia" can deadlock if pitted against each
other. "Greedy roller" will try to win the game outright on every single turn,
requiring an incredible stroke of luck to win at higher win scores. Meanwhile,
"Julia" will never see her opponent exceed 80% of the win score, and thus pass
immediately after rolling. *(This is why "Greedy roller" is turned off in
`strategies.py`.)*

## Requirements
`PySide2` to run, `pyinstaller` to build `.exe`.

## Building executable version
`pyinstaller PigsApp.spec`, copy `strategies.py` and `pig-nose-48x48.png` to `dist/` directory, and run `dist/PigsApp.exe`.

## Game Copyright
The version of the dice game Pig branded as "Pass the Pigs" is copyrighted by Hasbro.
