from matplotlib import pyplot as plt
import numpy as np

fig = plt.figure()
ax = plt.axes(projection='3d')
x =y =z =x1 =y1 =z1 = 0

# 1) Party followers Vote: 20%
total_polls_result = 74
labor_current_poll = 48
conservative_current_poll = 26
weightage_for_poll = 20/100

conservative_poll_pred = (conservative_current_poll / total_polls_result) * weightage_for_poll
labor_poll_pred = (labor_current_poll / total_polls_result) * weightage_for_poll

x+=conservative_poll_pred
x1+=labor_poll_pred

# 2) Policies: 60%
weight_of_policies = 0.6
# (i) Economic + Tax crisis - Contributes to 46% overall
Economy_weight = 0.46
conservative_economic_poll_raw = 33
labor_economic_poll_raw = 29

scaled_up_economy_conservative = conservative_economic_poll_raw / (conservative_economic_poll_raw + labor_economic_poll_raw)
scaled_up_economy_labor = labor_economic_poll_raw / (conservative_economic_poll_raw + labor_economic_poll_raw)

conservative_economic = scaled_up_economy_conservative * Economy_weight
labor_economic = scaled_up_economy_labor * Economy_weight
# (ii) Health + Environment crisis
Health_weight = 0.35
conservative_Health_poll_raw = 21
labor_Health_poll_raw = 42

scaled_up_Health_conservative = conservative_Health_poll_raw / (conservative_Health_poll_raw + labor_Health_poll_raw)
scaled_up_Health_labor = labor_Health_poll_raw / (conservative_Health_poll_raw + labor_Health_poll_raw)

conservative_Health = scaled_up_Health_conservative * Health_weight
labor_Health = scaled_up_Health_labor  * Health_weight
# (iii) Social + Immigration crisis
Immigration_weight = 0.19
conservative_Immigration_poll_raw = 21
labor_Immigration_poll_raw = 42

scaled_up_Immigration_conservative = conservative_Immigration_poll_raw / (conservative_Immigration_poll_raw + labor_Immigration_poll_raw)
scaled_up_Immigration_labor = labor_Immigration_poll_raw / (conservative_Immigration_poll_raw + labor_Immigration_poll_raw)

conservative_Immigration = scaled_up_Immigration_conservative * Immigration_weight
labor_Immigration = scaled_up_Immigration_labor * Immigration_weight

y = (conservative_Immigration + conservative_Health + conservative_economic) * weight_of_policies
y1 = (labor_Immigration + labor_Health + labor_economic) * weight_of_policies


# 3) Popularity: 20% 
## Social Media
#Instagram
insta_Rishi = 1400 # 1400k followers
insta_Keir = 197 # 197k followers
# Facebook
fb_Rishi = 448 # 448k followers
fb_Keir = 190 # 190k followers

social_popularity_Rishi = ((insta_Rishi / (insta_Rishi+ insta_Keir)) + (fb_Rishi / (fb_Rishi+ fb_Keir)))/2
social_popularity_Keir = ((insta_Keir / (insta_Rishi+ insta_Keir)) + (fb_Keir / (fb_Rishi+ fb_Keir)))/2

## Leader Popularity Polls
Popularity_Polls_Rishi = 32 # 32%
Popularity_Polls_Keir = 36 # 36%

Leader_Popularity_Polls_Rishi = Popularity_Polls_Rishi / (Popularity_Polls_Rishi + Popularity_Polls_Keir)
Leader_Popularity_Polls_Keir = Popularity_Polls_Keir / (Popularity_Polls_Rishi + Popularity_Polls_Keir)

# Total Popularity:
Popularity_Rishi = social_popularity_Rishi * 0.1 + Leader_Popularity_Polls_Rishi * 0.1
Popularity_Keir = social_popularity_Keir * 0.1 + Leader_Popularity_Polls_Keir * 0.1


z+=Popularity_Rishi
z1+=Popularity_Keir

# x1=x1-0.2
# y1=y1-0.6
# z1=z1-0.2

# Final Plot
print(x,x1,y,y1,z,z1)
print(x+x1+y+y1+z+z1)

print(x+y+z, x1+y1+z1)

ax.scatter3D(x, y, z, color='b')
ax.scatter3D(1/2, 1/2, 1/2, marker='x')
ax.scatter3D(x1, y1, z1, color='r')
plt.show()