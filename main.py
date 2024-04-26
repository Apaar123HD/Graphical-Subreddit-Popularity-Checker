import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(
    client_id="", #put your client id here
    client_secret="", #put your client secret here
    user_agent="", #put your user agent here
)



list1 = []
list2 = []
checkSub1 = input("Subreddit 1: ")
checkSub2 = input("Subreddit 2: ")
subreddit = reddit.subreddit(checkSub1)
subreddit2 = reddit.subreddit(checkSub2)
for submission in subreddit.hot(limit=100):
    list1.append(submission.score)
for submission in subreddit2.hot(limit=100):
    list2.append(submission.score)


title = "r/" + checkSub1 + " vs " + "r/" + checkSub2
print(title)

avg1 = sum(list1)/100
avg2 = sum(list2)/100
print("Average r/" + checkSub1, "post has", avg1, "upvotes")
print("Average r/" + checkSub2, "post has", avg2, "upvotes")

plt.plot(list1, linewidth=1, label=checkSub1)
plt.plot(list2, linewidth=1, label=checkSub2)
plt.plot([avg1, avg1])
plt.plot([avg2, avg2])

plt.xlabel("Posts")
plt.ylabel("Upvotes")

plt.xlim([0, 99])
plt.ylim([0, max(list1 or list2)])

plt.grid(False)

plt.title(title)

plt.legend()

plt.show()
