import pickle, os.path, gender

### Edit Here ###

# [x] 1
# [x] 2
# [x] 3
# [x] 4

split = 1 # <- edit this number (1,2,3,4) [CHANGE to : for 4]
split_size = 900
list_file = 'name_list.pckl'
dict_file = 'name_dict.pckl'

### ### ### ### #


# load the list of names to iterate through
with open(list_file, 'rb') as fp:
    name_list = pickle.load(fp)

# load or instantiate a dictionary of name:gender pairs
if os.path.isfile(dict_file):
    with open(dict_file, 'rb') as fp:
        name_dict = pickle.load(fp)
else:
    name_dict = {}

# lookup genders for each name
start = (split-1)*split_size
stop = split*split_size

names_to_lookup = name_list[start:stop]
#names_to_lookup = name_list[start:] # only use for final split

for name in names_to_lookup:
    sex = gender.getgender(name)
    name_dict[name] = sex
    #print(name + ' -> ' + sex)

# Finish up - write dictionary to file
with open(dict_file, 'wb') as fp:
    pickle.dump(name_dict, fp)
