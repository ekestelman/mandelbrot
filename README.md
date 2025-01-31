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

## Complex Numbers

A complex number $z_n$ may be expressed in the form $r_ne^{i\theta_n}$ where $r_n = \left|z_n\right|$ is the magnitude and $\theta_n$ is the argument. From the definition of our sequence, we have $z_n = z_{n-1}^2 + c = r_{n-1}^2e^{i2\theta_{n-1}} + r_1e^{i\theta_1}$. Then $\left|z_n\right| = r_n \ge r_{n-1}^2 - r_1$.

## Unboundedness

We can show that for any given $c,$ if the sequence $\left(z_n\right)$ has any element whose magnitude $\left|z_n\right| > 2,$ then the sequence is unbounded. That is, for any $c \in \mathbb{C}$, if $\exists N \in \mathbb{N}$ such that $\left|z_N\right| > 2$, then $\left|z_n\right|$ goes to infinity as $n$ goes to infinity.

For convenience we will define $r_n \coloneqq \left|z_n\right|$

Proof: First we show that for any $c$, if $\exists N \in \mathbb{N}$ such that $r_N > 2$ and $r_N \ge r_1$, then $\forall n>N, r_n > r_{n-1}$.

^Can we just make this for all $n>2$?

By definition, $z_{N+1} = z_{N}^2 + c$.  Then by assumption $r_{N+1} \ge r_{N}^2 - r_1 \ge r_N^2 - r_N = r_N\left(r_N - 1\right) > r_N.$

Corollary: if $r_1 > 2$ then $r_n > r_1 > 2 \forall n>1$.

Next we will show that that for $n>N$, the sequence of magnitudes $r_n$ is always increasing by at least some minimum value $\delta>0$.

As established, $r_{N+1} > r_{N} \ge r_1$. Then $r_{N+1} - r_{N} \ge r_N^2 - r_1 - r_N \ge r_N^2 - 2r_N = r_N\left(r_N - 2\right) \eqqcolon \delta > 0.$ Then $r_{N+2} \ge r_{N+1}^2 - r_1 - r_{N+1} \ge r_{N+1}^2 - 2r_{N+1} = r_{N+1}\left(r_{N+1} - 2\right) > \delta$, as desired.

This is useful in designing our program. When testing points to see if they are in the Mandelbrot set, we can run the sequence for a chosen number of iterations. If $z_n$ ever "escapes" outside of a radius of 2, we know that the test point $c$ is not in the set.
