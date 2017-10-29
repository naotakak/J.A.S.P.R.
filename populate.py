from util import db

print "\n======ADD STORIES======"
db.create_story("The Angry Hare", "Once there was a meme that lived. It Was Funny.")
db.create_story("Sasketchuan", "Bigfoot lived in Canadia. He is Hairy.")
db.create_story("Kobe Bryant", "We all know about it, and we all see it. It's obvious. Nobody ever wants to admit it, but it's there. People hate Kobe Bryant. The first question to ask: why? Why do you all hate him? The obvious answer: you didn't watch him in his prime. Likely explanation: I know that most of you are around 14 or 15 years old. That means you only got into basketball in the last couple years. So you never watched Mamba in his prime. And because you didn't watch him in his prime, you try to compensate for that by diving into stat sheets and analyzing box scores. But here's the thing: basketball isn't played on Excel spreadsheets. The moment somebody brings up 'true shooting percentage' or 'win shares' I know they know nothing about basketball. Kobe's game cannot be encapsulated by one stat. He's the second greatest SG ever, and one of the 5 best players to ever play the game. So when I hear somebody say that LeBron James is better than Kobe Bryant, I laugh, because I know that anybody who watched Kobe in his prime wouldn't think that. Unlike you guys, I have watched basketball for a significant amount of time, so I know that Kobe is better. You might be jealous of Kobe's five rings, or jealous of his status as the greatest scorer in NBA history, or whatever. Unless you're a Bulls fan who watched basketball in the 90s, or a Lakers fan who watched basketball in the 2000s, you don't know what real, cold-blooded, killer instinct, will-to-win basketball looks like. And there's nothing wrong with that. Some people would make you think that Kobe isn't even a top 100 player ever. So don't go spouting bs about players you didn't watch. Talk about your 'greats' like LeBron James, but leave the Kobe talk to the adults. Fair?")
print "============get_ids============"
db.get_ids()
print "============get_story============"
db.get_story(0)
db.get_story(1)
print "============get_last============"
db.get_last(0)
db.get_last(1)
print "============update_story========"
db.update_story(0, "Then it died.")
db.update_story(1, "He is also big.")
db.get_story(0)
db.get_story(1)
print "============print_stories========"
db.print_stories()

print "\n======ADD ACCOUNTS======"
db.create_account("admin", "password")
db.create_account("admin2", "password")
