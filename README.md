# ThreeXPlusOne: Sequence Growing

## Assigned: Friday, 1 March 2024

## Due: Friday, 1 March 2024

## Project Goals

Build a sequence as described by the Collatz Conjecture.

## Rules

```
	 If f(x) is odd,
       f(f(x)) = 3(f(x)) + 1,
	 else f(x) = f(x) /2

	 Repeat until f(x) = 4, then f(x) = 2 then f(x) = 1 (stop!)
```

## Instructions

Edit the File `threeXPlusOne/threexplusone/main.py` to allow for the following;

* Remove the To-Dos after writing filling-in the code.
* Determine that the program runs without errors.

Note: See slides for more information about the sequence.

## Execution

* Get into the virtual environment:
   + `poetry install`
* To get online help for the project
   + `poetry run threexplusone --help`. 
* To input a seed and run the project with a seed (such as 9)
   + `poetry run threexplusone --seed 9`

## Deliverables

   * `threeXPlusOne/threexplusone/main.py`
   * `writing/reflection.md`

## Submission

As you are working, you are to commit and push regularly. The commands are the following.

```bash
git add -A
git commit -m ``Your notes about commit here''
git push
```

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Project Assessment

This is a check mark grade.

## More Information

+ [Wikipedia: Collatz Conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)

+ [The Simplest Math Problem No One Can Solve - Collatz Conjecture](https://www.youtube.com/watch?v=094y1Z2wpJg)

+ [UNCRACKABLE? The Collatz Conjecture - Numberphile](https://www.youtube.com/watch?v=5mFpVDpKX70)

## GatorGrade Checking

You can also use `gatorgrade` to check the baseline requirements of this assignment by running the following command in your terminal:

`gatorgrade --config config/gatorgrade.yml`

If `gatorgrade` shows that all checks pass, you will know that you have met baseline requirements of this project.

After you have pushed your work to your repository, please visit the repository at the GitHub website (you may have to log-in using your browser) to verify that your files were correctly sent.

## Seeking Assistance

Students who have questions about this project outside of the lab time are invited to ask them in the course's Discord channel or during instructor's or TL's office hours.