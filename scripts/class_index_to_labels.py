def load_class_index(fname):
  import json
  data = open(fname, 'r').read()
  return json.loads(data)

cindex = load_class_index('../data/imagenet_class_index.json')
lblFile = open('labels.txt', 'w')
for i in range(1000):
  lblFile.write(cindex[str(i)][1] + '\n')
lblFile.close()

