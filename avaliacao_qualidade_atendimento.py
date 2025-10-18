# Célula 1: Importar bibliotecas
import numpy as np
import matplotlib.pyplot as plt

# Configurar gráficos para melhor visualização
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 8)

# Célula 2: Definir os dados de treinamento para a função XOR
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# Célula 3: Implementar a Rede Neural Simples (COM CORREÇÃO)
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.W1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * 0.1
        self.b2 = np.zeros((1, output_size))

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_derivative(self, x):
        return x * (1 - x)

    def feedforward(self, X):
        self.hidden_sum = np.dot(X, self.W1) + self.b1
        self.hidden_output = self._sigmoid(self.hidden_sum)
        self.output_sum = np.dot(self.hidden_output, self.W2) + self.b2
        self.output = self._sigmoid(self.output_sum)
        return self.output

    def backpropagate(self, X, y, learning_rate):
        output_error = y - self.output
        output_delta = output_error * self._sigmoid_derivative(self.output)
        
        hidden_error = output_delta.dot(self.W2.T)
        hidden_delta = hidden_error * self._sigmoid_derivative(self.hidden_output)
        
        self.W2 += self.hidden_output.T.dot(output_delta) * learning_rate
        self.b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate
        self.W1 += X.T.dot(hidden_delta) * learning_rate
        self.b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate
        
    # <<< ALTERAÇÃO PRINCIPAL AQUI >>>
    def train(self, X, y, epochs, learning_rate):
        """
        Função de treinamento corrigida para atualizar os pesos a cada exemplo (SGD).
        """
        errors = []
        for epoch in range(epochs):
            # Itera sobre cada exemplo de treinamento individualmente
            for i in range(len(X)):
                # Pega um exemplo de cada vez
                xi = X[i:i+1]
                yi = y[i:i+1]
                
                # Realiza o feedforward e backpropagation para esse único exemplo
                self.feedforward(xi)
                self.backpropagate(xi, yi, learning_rate)
            
            # A cada 100 épocas, calcula e armazena o erro médio para o conjunto de dados completo
            if epoch % 100 == 0:
                full_output = self.feedforward(X)
                loss = np.mean(np.square(y - full_output))
                errors.append(loss)
        return errors

    def predict(self, X):
        return self.feedforward(X)

# Célula 4: Treinar a Rede Neural
print("Iniciando o treinamento da rede neural...")
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)
epochs = 10000
learning_rate = 0.1
errors = nn.train(X, y, epochs, learning_rate)
print("Treinamento concluído!")

# Célula 5: Gerar Gráfico do Erro de Treinamento
plt.figure(figsize=(10, 6))
plt.plot(errors)
plt.title('Evolução do Erro Durante o Treinamento (Corrigido)')
plt.xlabel('Épocas (x100)')
plt.ylabel('Erro Quadrático Médio')
plt.grid(True)
plt.show()

# Célula 6: Análise dos Resultados e Teste
print("\n=== TESTANDO A REDE NEURAL TREINADA ===\n")
total_correct = 0
for i in range(len(X)):
    prediction = nn.predict(X[i])
    expected = y[i][0]
    predicted_class = 1 if prediction > 0.5 else 0
    is_correct = "CORRETO" if predicted_class == expected else "INCORRETO"
    if is_correct == "CORRETO":
        total_correct += 1
    print(f"Entrada: {X[i]} | Esperado: {expected} | Saída da Rede: {prediction[0][0]:.4f} | Classe: {predicted_class} ({is_correct})")

accuracy = (total_correct / len(X)) * 100
print(f"\nAcurácia do modelo: {accuracy:.2f}%")


# Célula 7: Visualizar a Superfície de Decisão
print("\nGerando visualização da superfície de decisão...")
x_min, x_max = -0.5, 1.5
y_min, y_max = -0.5, 1.5
h = 0.01
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = nn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.figure(figsize=(10, 8))
plt.contourf(xx, yy, Z, cmap=plt.cm.RdYlBu, alpha=0.8)
plt.scatter(X[:, 0], X[:, 1], c=y.ravel(), s=100, edgecolors='k', cmap=plt.cm.RdYlBu)
plt.title('Superfície de Decisão para o Problema XOR')
plt.xlabel('Entrada 1')
plt.ylabel('Entrada 2')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.show()