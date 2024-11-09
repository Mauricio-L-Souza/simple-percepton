weights = [0, 0]

inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
outputs = [0, 0, 0, 1]

lr = 0.1
error = 0
epochs = 10
threshold = 0.5


def degrau(sum):
    if (sum >= threshold):
        return 1
    return 0


def criterion(sum):
    return degrau(sum)


def calculate_error(neuron_out):
    error = 0
    for i in range(len(outputs)):
        error += outputs[i] - neuron_out[i]

    return error


def update_weights(error):
    for inp in inputs:
        for i in range(len(inp)):
            weights[i] = weights[i] + (inp[i] * lr * error)


def inference(inp):
    sum = 0
    for i in range(len(inp)):
        sum += inp[i] * weights[i]
    return criterion(sum)


for epoch in range(epochs):
    out = []
    for inp in inputs:
        y = inference(inp)
        out.append(y)

    error = calculate_error(out)
    update_weights(error)

    print(f'epoch: {epoch} error: {error}')

print(f'Resultado para 1 && 0: {inference([1,0])}')
print(f'Resultado para 0 && 1: {inference([0,1])}')
print(f'Resultado para 0 && 0: {inference([0,0])}')
print(f'Resultado para 1 && 1: {inference([1,1])}')

print('\nPESOS DO NEURONIO\n')
print(weights)
