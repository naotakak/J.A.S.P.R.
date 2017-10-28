from util import db

print "\n======ADD STORIES======"
db.create_story(0, "The Angry Hare", "Once there was a meme that lived. It Was Funny.")
db.create_story(1, "Sasketchuan", "Bigfoot lived in Canadia. He is Hairy.")
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
