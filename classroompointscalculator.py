# ============================================================
# Classroom Points Calculator
# ============================================================
 
# --- Assignment Operator (=) ---
# Store the points earned by 5 classroom teams
team1 = 120
team2 = 95
team3 = 140
team4 = 110
team5 = 85
 
# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average points
total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Total points       :", total)
print("Average per team   :", average)
 
# Each point gives 2 reward stars
stars_per_point = 2
reward_stars = total * stars_per_point
print("Total reward stars :", reward_stars)
 
# --- Floor Division (//) and Modulus (%) ---
# Pack reward stars into boxes of 25 stars each
boxes = reward_stars // 25
leftover = reward_stars % 25
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover)
 
# --- Comparison Operators (>, <, ==, >=) ---
# Compare this week's points with last week's points
last_week = 500
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 
# --- Assignment Operators (+=, -=) ---
# Bonus challenge adds 30 points to the total
total += 30
print("After bonus points :", total)
 
# 15 points are removed for missed tasks
total -= 15
print("After missed tasks :", total)
 
# Final reward box count after all changes
reward_stars = total * stars_per_point
boxes = reward_stars // 25
 
print("Final boxes packed :", boxes)
