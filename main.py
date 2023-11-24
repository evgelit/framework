from attribute.attribute_set_collection import AttributeSetCollection

collection = AttributeSetCollection()
collection.load_collection()

for attribute_set in collection:
    print(attribute_set.name)
    for attribute in attribute_set.attribute_collection:
        print("    ",attribute.name)
