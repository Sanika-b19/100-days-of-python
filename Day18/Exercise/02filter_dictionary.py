# Exercise 2: Filter a Dictionary by Values

scores = {'John': 45, 'Emily': 67, 'Kate': 49, 'Mike': 88}
filtered_scores = {key: value for key, value in scores.items() if value >= 50}
print(filtered_scores)
