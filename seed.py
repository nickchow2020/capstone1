from modals import User,db,Vocabulary,Grammar,Studyplan
from app import app

db.drop_all()
db.create_all()

user1 = User.register(
    first="nick",
    last="zhou",
    username="nickzhou",
    password="shuminzhou",
    email="smz111@gmail.com",
    native_language="chinese",
    second_language="english"
    )

user2 = User.register(
    first="stephen",
    last="zhou",
    username="stephenzhou",
    password="shuminzhou",
    email="smz112@gmail.com",
    native_language="chinese",
    second_language="english"
    )

db.session.add(user1)
db.session.add(user2)

db.session.commit()


vocal1 = Vocabulary(
    vocabulary="verbal",
    category="healthcare",
    definition_en="verbal",
    definition_ch="口头的",
    part_of_speech = "noun",
    user_id = 1
    )

vocal2 = Vocabulary(
    vocabulary="encompass",
    category="healthcare",
    definition_en="encompass",
    definition_ch="包围，包含",
    part_of_speech = "noun",
    user_id = 1
    )

vocal3 = Vocabulary(
    vocabulary="diagnostic",
    category="healthcare",
    definition_en="diagnostic",
    definition_ch="诊断",
    part_of_speech = "noun",
    user_id = 1
    )

vocal4 = Vocabulary(
    vocabulary="pace",
    category="healthcare",
    definition_en="pace",
    definition_ch="速度",
    part_of_speech = "noun",
    user_id = 1
    )

vocal5 = Vocabulary(
    vocabulary="stomach cramp",
    category="healthcare",
    definition_en="stomach cramp",
    definition_ch="胃痛",
    part_of_speech = "noun",
    user_id = 1
    )

vocal6 = Vocabulary(
    vocabulary="eliminating",
    category="healthcare",
    definition_en="eliminating",
    definition_ch="消除",
    part_of_speech = "noun",
    user_id = 2
    )

vocal7 = Vocabulary(
    vocabulary="periodically",
    category="healthcare",
    definition_en="periodically",
    definition_ch="定期的",
    part_of_speech = "noun",
    user_id = 1
    )

vocal8 = Vocabulary(
    vocabulary="tabulating",
    category="healthcare",
    definition_en="tabulating",
    definition_ch="制表",
    part_of_speech = "noun",
    user_id = 1
    )

vocal9 = Vocabulary(
    vocabulary="forgery",
    category="healthcare",
    definition_en="forgery",
    definition_ch="伪造品",
    part_of_speech = "noun",
    user_id = 1
    )

vocal10 = Vocabulary(
    vocabulary="distintion",
    category="healthcare",
    definition_en="distintion",
    definition_ch="区别",
    part_of_speech = "noun",
    user_id = 2
    )

db.session.add(vocal1)
db.session.add(vocal2)
db.session.add(vocal3)
db.session.add(vocal4)
db.session.add(vocal5)
db.session.add(vocal6)
db.session.add(vocal7)
db.session.add(vocal8)
db.session.add(vocal9)
db.session.add(vocal10)

db.session.commit()



grammar1 = Grammar(
    term="present simple",
    description="We use the present simple to talk about routines, e.g. what we do every day,We can use the adverbs always, often and never",
    example1="always clean my teeth before bed.",
    example2="I often eat pasta for dinner.",
    example3="I never watch football on television.",
    user_id = 1)

grammar2 = Grammar(
    term="present simple",
    description="We also use the present simple to talk about things that are generally true and for facts. If something is generally true, it is true now but maybe it will change in the future. A fact is true forever.",
    example1="always clean my teeth before bed.",
    example2="aWater boils at 100 degrees centigrade.",
    example3="I love chocolate.",
    user_id = 1)

grammar3 = Grammar(
    term="He,She,It in the present simple",
    description="When we define present simple with he,the verb we need to use goes",
    example1="It goes to the beach every weekend",
    example2="She goes to the beach every weekend",
    example3="He goes to the beach every weekend",
    user_id = 1)

grammar4 = Grammar(
    term="The present continuous",
    description="We use the present continuous to talk about things that are happening now,We make the present continuous with be + -ing,We can use the words now, at the moment and look!",
    example1="I am playing now.",
    example2="She is eating at the moment.",
    example3="Look! He is singing.",
    user_id = 1
)

db.session.add(grammar1)
db.session.add(grammar2)
db.session.add(grammar3)
db.session.add(grammar4)

db.session.commit()




plan1 = Studyplan(plan="10 word per day",repeat="daily",start_date="08-01-2021",end_date="10-01-2022",user_id=1)
plan2 = Studyplan(plan="runs 30 mins daily",repeat="daily",start_date="08-01-2021",end_date="10-01-2022",user_id=1)
db.session.add(plan1)
db.session.add(plan2)
db.session.commit()