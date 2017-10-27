from util import db

db.create_story(0, "The Angry Hare", "Once there was a meme that lived.", "It Was Funny")
db.create_story(1, "Sasketchuan", "Bigfoot lived in Canadia.", "He is Hairy")
print "============get_ids============"
print db.get_ids()
"============get_story============"
print db.get_story(0)
"============get_last============"
print db.get_last(0)
db.update_story(0, "Then it died.")
"============get_ids============"
print db.get_ids()
"============get_story============"
print db.get_story(0)
"============get_last============"
print db.get_last(0)
