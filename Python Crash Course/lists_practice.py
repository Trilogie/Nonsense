from typing import List

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1].title())

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append('honda')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

motorcycles.insert(0, 'ducati')
print(motorcycles)

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

motorcycles.remove('honda')
print(motorcycles)

too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

cars: List[str] = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print(sorted(cars))

cars.reverse()
print(cars)

cars.sort(reverse=True)
print(cars)

len(cars)


