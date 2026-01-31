import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Create a tiny dataset
x = np.linspace(0, 2 * np.pi, 50)
y = np.sin(x) + 0.1 * np.random.randn(len(x))

df = pd.DataFrame({"x": x, "y": y})

# Basic stats
stats = df.describe()
print(stats)

# Plot and save
plt.figure(figsize=(6, 3))
plt.plot(df['x'], df['y'], marker='o', linestyle='-')
plt.title('Demo: sin(x) + noise')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout()
plt.savefig('examples/out.png')
print('Saved examples/out.png')
