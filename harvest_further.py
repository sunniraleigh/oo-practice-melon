############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless 
        self.is_bestseller = is_bestseller
                 

        

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        self.pairings.append(pairing)
        # Fill in the rest

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""
        self.code = new_code
        # Fill in the rest


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk',1998,'green',True,True,"Muskmelon")
    muskmelon.add_pairing("mint")
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas',2003,'orange',False,False,"Casaba")
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren',1996,'green',False,False,"Crenshaw")
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)
    
    yellow_watermelon = MelonType('yw',2013,'yellow',False,True,"Yellow Watermelon")
    yellow_watermelon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermelon)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"- {pair}")
        print(" ")
    

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_dictionary = {}

    for melon in melon_types:
        # melon_dictionary[melon.code] = {'first_harvest': melon.first_harvest, 'color': melon.color, 
        #                                 'is_seedless': melon.is_seedless, 'bestseller': melon.is_bestseller,
        #                                 'pairs_with': melon.pairings}
        melon_dictionary[melon.code] = melon
    
    return melon_dictionary
        


############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from = harvested_from
        self.harvested_by = harvested_by
    
    def is_sellable(self):
        return self.color_rating > 5 and self.shape_rating > 5 and self.harvested_from != 3

def make_melons(melon_types,logfile):
    """Returns a list of Melon objects."""
    harvest_list = []
    melon_ids = make_melon_type_lookup(melon_types)

    melon_file = open(logfile)
    for line in melon_file:
        line = line.rstrip().split(" ")
        
        new_melon = Melon(melon_ids[line[5]], int(line[1]), int(line[3]), int(line[11]), line[8])
        harvest_list.append(new_melon)
        
    return harvest_list


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    # Harvested by Sheila from Field 2 
    # Harvested by Sheila from Field 2 (NOT SELLABLE)
    for each_melon in melons:
        if each_melon.is_sellable():
            sell_message = "(CAN BE SOLD)"
        else:
            sell_message = "(NOT SELLABLE)"

        print(f'Harvested by {each_melon.harvested_by} from Field {each_melon.harvested_from} {sell_message}')



all_melons = make_melon_types() # Parent Class
all_harvest_melons = make_melons(all_melons,"harvest_log.txt")
get_sellability_report(all_harvest_melons)

#print(all_harvest_melons)
#print_pairing_info(all_melons)
#print(make_melon_type_lookup(all_melons))