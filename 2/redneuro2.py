import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.2):
        # Inicialización de pesos
        self.learning_rate = learning_rate
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        
    def step_function(self, x):
        return np.where(x >= 0, 1, 0)
    
    def forward(self, inputs):
        # Propagación hacia adelante
        self.hidden_input = np.dot(inputs, self.weights_input_hidden)
        self.hidden_output = self.step_function(self.hidden_input)
        
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output)
        self.final_output = self.step_function(self.final_input)
        
        return self.final_output
    
    def train(self, inputs, targets):
        # Propagación hacia adelante
        outputs = self.forward(inputs)
        
        # Calcula el error
        output_errors = targets - outputs
        
        # Retropropagación del error y ajuste de pesos
        hidden_errors = np.dot(output_errors, self.weights_hidden_output.T)
        
        # Actualización de pesos
        self.weights_hidden_output += self.learning_rate * np.dot(self.hidden_output.T, output_errors)
        self.weights_input_hidden += self.learning_rate * np.dot(inputs.T, hidden_errors)
        
    def predict(self, inputs):
        return self.forward(inputs)

# Datos de entrada
inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
targets = np.array([[0], [1], [1], [0]])  # Ejemplo XOR

# Inicializar la red neuronal
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Entrenar la red
for epoch in range(10000):
    nn.train(inputs, targets)

# Predicciones
for input_data, target_data in zip(inputs, targets):
    predicted_output = nn.predict(input_data)
    print(f"Entrada: {input_data}, Salida esperada: {target_data}, Salida predecida: {predicted_output}")
