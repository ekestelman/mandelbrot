# The Mandelbrot Set

## Definition

Consider the following sequence of complex numbers:

$$\begin{cases}
z_0 &=& 0 \\ 
z_{n} &=& z_{n-1}^2 + c \quad\text{ for }\quad n > 0
\end{cases}$$

where $c$ is a complex number. The Mandelbrot set is the set of all complex numbers $c$ such the sequence $\left(z_n\right)$ is bounded.

Example 1: Take $c=-1$. $z_0 = 0$ by definition. Then

$$\begin{align}
z_1 &=& 0^2 - 1 &=& -1\\
z_2 &=& (-1)^2 - 1 &=& 0.
\end{align}$$

We immediately see that $\left(z_n\right)$ alternates between $0$ and $-1$, so the sequence is bounded. $-1$ is therefore in the Mandelbrot set.

Example 2: Take $c = 1$. $z_0 = 0$ by definition. Then

$$\begin{align}
z_1 &=& 0^2 + 1 &=& 1\\
z_2 &=& 1^2 + 1 &=& 2\\
z_3 &=& 2^2 + 1 &=& 5.
\end{align}$$

It should be apparent that $\left(z_n\right)$ goes to infinity, and is thus unbounded. $1$ is therefore _not_ in the Mandelbrot set.

