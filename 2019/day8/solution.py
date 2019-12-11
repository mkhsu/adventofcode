data = None
with open('day8.txt') as f:
    data = [int(i) for i in f.read().strip()]

per_layer = 6*25

num = len(data) // per_layer
layers = [data[i*per_layer:i*per_layer+per_layer] for i in range(num)]

least_0 = min(layer.count(0) for layer in layers)
layer_w_least_0 = filter(lambda x: x[1].count(0) == least_0, enumerate(layers))
layer_w_least_0 = next(iter(layer_w_least_0))[1]
print(layer_w_least_0.count(1) * layer_w_least_0.count(2))

for i in range(len(layers[0])):
    k = 1
    while k < len(layers) and layers[0][i] == 2:
        layers[0][i] = layers[k][i]
        k+=1

#print(layers)
# print(layers[0])

for i,j in enumerate(layers[0]):
    if j == 0:
        layers[0][i] = ' '
    elif j == 1:
        layers[0][i] = '■'
    else:
        layers[0][i] = ' '
for i in range(6):
    for j in range(25):
        print(layers[0][i*25+j], end='')
    print()