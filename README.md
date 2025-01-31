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

We can show that for any given $c,$ if the sequence $\left(z_n\right)$ ever "escapes" outside a radius of 2 from the origin, then the sequence is unbounded. That is, for any $c \in \mathbb{C}$, if $\exists N \in \mathbb{N}$ such that $\left|z_N\right| > 2$, then $\left|z_n\right|$ goes to infinity as $n$ goes to infinity.

Proof: We will make use of the following properties of complex numbers. Given $a,b\in\mathbb{C}$,

$$\left|a + b\right| \ge |a| - |b|$$

$$\left| a^2\right| = \left|a\right|^2.$$

The first is given by the triangle inequality. The second is easy to see when we express the complex number $a$ in the form $re^{i\theta}$. Then $a^2 = r^2e^{i2\theta}$ and $\left|a^2\right| = r^2 = |a|^2.$

Now we can observe that for a sequence element

$$z_{n+1} = z_n^2 + c$$

we have

$$\left|z_{n+1}\right| \ge \left|z_n\right|^2 - \left|c\right|.$$

By assumption, $|z_N| > 2.$ Therefore if $|c| \le 2$ we have $|z_N| > |c|$. If $|c| > 2,$ then choose $N=1$ so that $z_N = c$ and $|z_N| = |c|$. Together we have $|z_N| \ge |c|$.

We will use induction to show that $\forall n \ge N,|z_{n+1}| > |z_{n}| \ge |c|.$ Take as base case $z_{N}.$ Then $|z_{N+1}| \ge |z_{N}|^2 - |c| \ge |z_N|^2 - |z_N|$ as shown previously. Then because $|z_N| > 2$ by assumption, we have $|z_N|^2 - |z_N| = |z_N|\left(|z_N| - 1\right) > |z_N| \ge |c|,$ as desired.

Suppose for inductive hypothesis that for some $k \ge N$ we have $|z_{k+1}| > |z_{k}| \ge |c|$ and $|z_k| \ge 2.$ Then $|z_{k+2}| \ge |z_{k+1}|^2 - |c| > |z_{k+1}|^2 - z_{k+1}$ by our inductive assumption. Then $|z_{k+1}|^2 - |z_{k+1}| = |z_{k+1}|\left(|z_{k+1}| - 1\right) > |z_{k+1}|$ (another substitution using inductive assumption) as desired. By the principle of induction, we have $|z_{n+1}| > |z_n| \ge |c|, \forall n \ge N.$

We are now ready to show that $\forall n \ge N$, the difference in magnitude between consecutive sequence elements $|z_{n+1}| - |z_n|$ has a minimum.

We will again use induction. Take as base case $n=N$. Then

$$
\begin{align*}
    |z_{N+1}| - |z_N| \ge |z_N|^2 - |c| - |z_N| \ge |z_N|^2 - 2|z_N| = |z_N|\left(|z_N| - 2\right).
\end{align*}
$$

By assumption, $|z_N| > 2$, so we have

$$|z_N|\left(|z_N| - 2\right) > 0.$$

Suppose for inductive hypothesis that $\exists k \ge N$ such that $|z_{k+1}| - |z_k| \ge |z_k|\left(|z_k|-2\right) \ge |z_N|\left(|z_N| - 2\right) > 0.$ Then $|z_{k+2}| - |z_{k+1}| \ge |z_{k+1}|^2 - |c| - |z_{k+1}| \ge |z_{k+1}| - 2|z_{k+1}| = |z_{k+1}|\left(|z_{k+1}| - 2\right) > |z_k|\left(|z_k| - 2\right)$ (recall that we have previously shown that $|z_n| \ge |c|$ and $|z_n| > 2$ $\forall n \ge N$). By inductive assumption we have $|z_k|\left(|z_k| - 2\right) \ge |z_N|\left(|z_N| - 2\right) > 0.$ By the principle of induction we have $|z_{n+1}| - |z_n| \ge |z_{N+1}| - |z_N|$ $\forall n \ge N$ as desired. We conclude that there is no upper bound to $|z_n|$, so $\left(z_n\right)$ is unbounded. $\blacksquare$

This is useful in designing our program. When testing points to see if they are in the Mandelbrot set, we can run the sequence for a chosen number of iterations. If $z_n$ ever "escapes" outside of a radius of 2, we know that the test point $c$ is not in the set.
