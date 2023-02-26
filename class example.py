variable_1 = "original_value"
variable_2 = variable_1
variable_1 = "new_value"

print(variable_2)  # => "original_value"
# the data is copied over to the new variable for str, int, bool, etc

variable_1 = ["some_data", "more_data"]
variable_2 = variable_1
variable_1.append("even_more_data")

print(variable_2)  # => ["some_data", "more_data", "even_more_data"]
# the data is referenced in the new variable and stored somewhere in memory for array, object, etc


class DataStructure:
    class_variable = "default_value"

    def __init__(self, initial_values):
        self.attributes = initial_values

    def change_default_attribute(self, new_value):
        self.class_variable = new_value

    def change_initial_attributes(self, new_values):
        self.attributes = new_values

    def get_info_about_instance(self):
        instance_type = type(self)  # => <type: DataStructure>
        attributes = self.attributes  # => initial_values or new_values
        default_attributes = self.class_variable  # => "default_value" or new_value
        return instance_type, attributes, default_attributes

    def set_instance_friends(self, other_objects):
        self.friends = other_objects  # self.friends references the friend objects and changes when they change

    def get_friends_info(self):
        friends_info = list()
        for friend in self.friends:
            friends_info.append(friend.attributes)
        return friends_info

    def set_type_method(self, info):
        new_info = do_stuff(info)
        self.new_attribute = new_info

    def get_type_method(self):
        info = do_stuff(self)
        return info


main_object = DataStructure("initial_values")  # DataStructure-type object

main_object.change_initial_attributes("new_value")  # does action on an object using a method
main_object.attributes = "new_value"  # does action on object without needing a method

print(main_object.get_info_about_instance())  # gets info about an object using a method
instance_type = type(main_object)                     #
attributes = main_object.attributes                   # gets info about an object without needing a method (painfully)
default_attributes = main_object.class_variable       #
print(instance_type, attributes, default_attributes)  #

new_objects = list()
for i in range(5):
    # creates lots of instances of DataStructure at once, referenced in the list
    new_objects.append(DataStructure("changeable_values"))
    # type doesnt have to be the same DataStructure

for general_object in new_objects:
    general_object.change_default_attribute("different_attribute_to_other_class_members")
    # general_object becomes each object in list, so is useless after the for loop

main_object.set_instance_friends(new_objects)
print(main_object.get_friends_info())  # => gets info about friends

new_objects[4].attributes = "changed_attributes"
main_object.friends[4].attributes = "changed_attributes"
print(main_object.get_friends_info())  # => gets info with changed attributes on 4th friend

main_object.friends.remove(new_objects[2])
del new_objects[2]
print(main_object.get_friends_info())  # => gets info without 2nd friend
print(new_objects[2].attributes)  # => past 2nd friend is also gone