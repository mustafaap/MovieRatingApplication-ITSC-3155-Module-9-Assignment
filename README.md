# ITSC 3155 Module 9 Assignment

This repository houses the scaffolding for a movie rating application. By the end, this application will fulfill the following user stories / features to realize a full CRUD (create, read, update, delete) application:

1. As a user, I should be able to view all saved movie ratings in a visually appealing table
2. As a user, I should be able to save a movie rating with the movie's name, director, and a 1-5 rating
3. As a user, I should be able to search for a specific movie rating using the movie's title
4. As a user, I should be able to view a movie in isolation and have access to edit and delete that movie.
5. As a user, I should be able to edit a movie.
6. As a user, I should be able to delete a movie.

## Python Version

You must have Python 3.10+ installed to run this application.

![movierating](https://github.com/mustafaap/MovieRatingApplication-ITSC-3155-Module-9-Assignment/assets/123131622/21e419da-fa03-4896-a1be-a997feba9157)


## Instructions

1. Have ***exactly one*** member of your team fork this repository. This team member should also add every other team member as write-access contributors to the fork.
2. ***Every*** member of your team should clone the forked repository. **DO NOT** clone this repository, only clone the forked one. If you clone this repository, the remote will point here and not to the forked repository where you are allowed to make changes.
3. Create a virtual environment with `python -m venv venv`, activate it, and then install the project dependencies in this environment with `pip install -r requirements.txt`. This will install everything you need to run `flask` and `pytest`.
4. ***Every*** team member should be assigned a feature to work on and each team member should work on a different feature. If your group has fewer than 6 members, you will assign and complete the first n stories, where n is the number of people in your group (ex. if you have 4 group members, you will only turn in stories 1-6).
5. Create a new feature branch for your feature (ex. `implement-create-movies`).
6. Implement the feature and make commits as you go (no strict rules on when to make a commit as long as all your work is commited when you finish).
7. Add appropriate `pytest` tests for your feature. Cover at least the "happy" path and, where applicable, test for "bad" input and edge cases. You should include both unit tests and end-to-end / integration / functional tests (tests that test the API directly, however you want to classify them). Note that you can write the tests before or during the actual feature work. Also note that you may need to create "mock" data in each test by pulling the repository singleton into your test and calling methods directly. Lastly, note that you may need to clear the DB before running certain tests, which is a method on the repository singleton object.
8. Push your branch with all its commits up to your remote.
9. Make a pull request from your feature branch to the `main` branch.
10. Review another team member's PR. Remember to leave good feedback in comments and request changes if needed. If everything looks good, go ahead and approve it.
11. Merge your PR into `main` once it has been approved by another team member.
12. Verify that your changes look good in `main`.

Some things to note:

- Each team member needs to make a PR and approve another PR to get full credit.
- You can and should make comments or request changes when appropriate. Remember that if you approve code that does not work, everyone loses points, so review seriously.
- Some stories may be blocked by other stories. To work around this, you can add fake starting data to the DB manually, as long as you do not end up merging in the fake data in a PR. Coordinate with your team properly to make sure everyone completes their stories in a timely fashion so as not to block others until the last minute.
- You are welcome to make multiple PRs if you do your story in stages, have part of a story blocked, or need to fix something. You need at least one to get full credit.
- Coordinate with your team and complete your stories **early** to ensure nobody is blocked until the last minute and does not have sufficient time to complete their ticket.

*This assignment was created for the ITSC 3155 Software Engineering course, taught by Jacob Kedar Krevat, at the College of Computing and Informatics at UNC Charlotte*
