  f = open("train.csv", "r")
  tokyo = f.readlines()
  f.close()
   
  count = 0
  all_male = 0
  all_female = 0

  t = []
  for i in range(1, len(tokyo)):
      t = a[i].strip().split(',')
      if t[1] == '1' and t[5] == 'male':
          male += 1
      if t[1] and t[5] == 'female':
          female += 1
   
  count = all_male + all_female
  print ("total number of survivors:",  count)
  print ("number of surviving men:",  all_male)
  print ("number of surviving women:",  all_female)
