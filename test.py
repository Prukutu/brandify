import numpy as np
import matplotlib.pyplot as plt
import brandify

plt.style.use('usl-presentations')

logo_file = 'usl-black.png'
x = np.linspace(0, 6*np.pi)
y = np.sin(x)

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(x, y)
ax.set_title('This is my sine wave', loc='left')

fig = brandify.embed_logo(fig, logo_file, loc='upper left')

fig.savefig('sample-logo.png', bbox_inches='tight')
