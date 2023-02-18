motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)    # ['honda', 'yamaha', 'suzuki', 'ducati']
# motorcycles[0] = "理想L9"
# print(motorcycles)    # ['理想L9', 'yamaha', 'suzuki', 'ducati']
# motorcycles.append('BMW')
# print(motorcycles) # ['honda', 'yamaha', 'suzuki', 'ducati', 'BMW']
motorcycles.insert(1, "benz")
print(motorcycles)  # ['honda', 'benz', 'yamaha', 'suzuki', 'ducati']

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
