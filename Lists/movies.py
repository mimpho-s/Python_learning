best_pictures = [
  '2019 - Parasite',
  '2018 - Green Book',
  '2017 - The Shape of Water',
  '2016 - Moonlight',
  '2015 - Spotlight',
  '2014 - Birdman',
  '2013 - 12 Years a Slave',
  '2012 - Argo',
  '2011 - The Artist'
]

new_list = [
  '2024 - Anora',
  '2023 - Oppenheimer', 
  '2022 - Everything Everywhere All at Once',
  '2021 - CODA',
  '2020 - Nomadland'
]

for x in new_list:         # best_pictures = new_list + best_pictures(this method will get you the same results)
  best_pictures.insert(0,x)

print(best_pictures)