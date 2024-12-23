from aima.logic import FolKB , expr
# Initialize the knowledge base
kb = FolKB()

# Add facts
kb.tell(expr("Hobby(Mummy, Yoga)"))
kb.tell(expr("Hobby(Mummy, Monday)"))
kb.tell(expr("Hobby(Mummy, Thursday)"))
kb.tell(expr("Likes(Betty, Marmalade)"))
kb.tell(expr("Eats(Mummy, Marshmallows)"))
kb.tell(expr("¬Likes(Peter, Cream)"))
kb.tell(expr("Prepares(Mummy, NapoleonCake)"))
kb.tell(expr("Prepares(Mummy, Marmalade)"))
kb.tell(expr("Prepares(Mummy, Waffles)"))

# Add rules
kb.tell(expr("Dreams(X, Paris) <=> Likes(X, IceCream)"))
kb.tell(expr("Dreams(Mummy, NewYearWish)"))
kb.tell(expr("Dreams(Daddy, NewYearWish)"))

# Query 1: Who likes the Napoleon cake?
result1 = kb.ask(expr("Likes(X, NapoleonCake)"))[0]
print(f"Who likes the Napoleon cake? {result1}")

# Query 2: Who dreams of going to Paris?
result2 = kb.ask(expr("Dreams(X, Paris)"))
print(f"Who dreams of going to Paris? {result2}")