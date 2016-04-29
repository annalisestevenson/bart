dublin_to_powell = 6.15
fruitvale_to_union_city = 3.80
orinda_to_richmond = 3.35
hayward_to_concord = 5.20
fremont_to_colma = 6.60

def load_card(one, five, ten, twenty):
	return one + 5*five + 10*ten + 20*twenty
	return load_card(0,0,0,1)
	
# clipper_card1 = 6.60
# clipper_card2 = 20
# clipper_card3 = 6
# clipper_card4 = 12
clipper_card5 = 4



def travel_to_destination(fare_price, card_value):
	if clipper_card5 >= fare_price:
		return "Welcome aboard"
	else:
		return "not enough money"
# print travel_to_destination(fremont_to_colma, clipper_card1)
# print travel_to_destination(hayward_to_concord, clipper_card2)
# print travel_to_destination(dublin_to_powell, clipper_card3)
# print travel_to_destination(fruitvale_to_union_city, clipper_card4)
print travel_to_destination(orinda_to_richmond, clipper_card5)