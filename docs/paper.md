---
author:
- furkzel
date: 2025-10-25
title: Formal Analysis of a Recursive Sequence Involving Triangular
  Numbers
---

# Problem Statement

Let $(a_n)_{n\ge0}$ be a sequence defined by $$a_0 = 3, \qquad
    a_{n+1} =
    \begin{cases}
        a_n + 1,            & \text{if } a_n \text{ is a triangular number}, \\[4pt]
        2a_n - a_{n-1} + 1, & \text{otherwise.}
    \end{cases}$$ Define the triangular numbers
$$T_j = \frac{j(j+1)}{2}, \qquad j\in\mathbb{N}.$$ Let
$(a_{n_k})_{k\ge1}$ denote the subsequence of $(a_n)$ consisting of
those terms that are triangular. The indices $(n_k)$ satisfy
$a_{n_k} = T_{j_k}$ for some $(j_k) \in \mathbb{N}$, with $n_1=0$ and
$j_1=2$.

Given $$n_{10}=2964,$$ find $n_{70}$, the index of the $70$-th
triangular number appearing in the sequence.

# Preliminary Definitions and Lemmas

::: definition
**Definition 1**. Define the difference sequence $d_n := a_{n+1} - a_n$.
:::

::: lemma
**Lemma 2** (Difference Recurrence). For all $n\ge1$, $$d_n =
        \begin{cases}
            1,           & \text{if } a_n \text{ is triangular}, \\[4pt]
            d_{n-1} + 1, & \text{otherwise.}
        \end{cases}$$
:::

::: proof
*Proof.* If $a_n$ is not triangular, then
$$a_{n+1} = 2a_n - a_{n-1} + 1 \implies d_n = (a_n - a_{n-1}) + 1 = d_{n-1} + 1.$$
If $a_n$ is triangular, then $a_{n+1} = a_n + 1$, so $d_n = 1$. ◻
:::

::: lemma
**Lemma 3** (Cumulative Increment Between Successive Triangular Terms).
Let $m_k = n_{k+1} - n_k$. Then
$$a_{n_{k+1}} - a_{n_k} = \sum_{i=1}^{m_k} i = T_{m_k}.$$
:::

::: proof
*Proof.* After encountering a triangular number, $d$ resets to $1$ and
increases by $1$ at each subsequent step. Hence the total increase after
$m_k$ steps is $\sum_{i=1}^{m_k} i = T_{m_k}$. ◻
:::

# Algebraic Characterization

An integer $x$ is triangular if and only if $$8x + 1 = (2j + 1)^2.$$

::: lemma
**Lemma 4** (When the Sum of Two Triangular Numbers Is Triangular). The
following are equivalent for integers $j,m,r$:

1.  $T_j + T_m = T_r$,

2.  $w^2 = u^2 + v^2 - 1$, where $u = 2j + 1$, $v = 2m + 1$,
    $w = 2r + 1$,

3.  There exist positive integers $x,y$ such that
    $$xy = j(j+1), \quad y-x \text{ is odd and } y-x>1,$$ and
    $v = y - x = 2m + 1$.
:::

::: proof
*Proof.* $(1)\Leftrightarrow(2)$: from $8T_j + 1 = (2j+1)^2$, we have
$$8(T_j + T_m) + 1 = (2j + 1)^2 + (2m + 1)^2 - 1 = (2r + 1)^2.$$
$(2)\Leftrightarrow(3)$: from $w^2 - v^2 = u^2 - 1 = 4j(j+1)$, define
$x = \frac{w - v}{2}$, $y = \frac{w + v}{2}$. Then $xy = j(j+1)$ and
$v = y - x$ is odd and $>1$. ◻
:::

# Existence and Minimal Step Between Triangular Numbers

::: proposition
**Proposition 5** (Existence). For every $j\ge1$, there exists $m>0$
such that $T_j + T_m$ is triangular.
:::

::: proof
*Proof.* Taking $x=1$, $y=j(j+1)$ gives $xy = j(j+1)$ and
$y-x = j(j+1)-1$, which is odd and $>1$. ◻
:::

::: definition
**Definition 6** (Minimal Step Function). $$m(j) = \min \left\{
        \frac{y - x - 1}{2}
        :\ xy = j(j+1),\ y-x\text{ odd and }y-x > 1
        \right\}.$$
:::

# Main Theorem

$$\boxed{
        \begin{aligned}
            n_1         & = 0, \quad j_1 = 2,  \\[4pt]
            m_k         & = m(j_k)
            = \min_{\substack{xy=j_k(j_k+1)    \\ y-x\ \text{odd},\ y-x>1}}
            \frac{y-x-1}{2},                   \\[6pt]
            n_{k+1}     & = n_k + m_k,         \\[4pt]
            T_{j_{k+1}} & = T_{j_k} + T_{m_k}.
        \end{aligned}
    }$$

::: proof
*Proof.* By Lemma 2.3, the total increase between triangular terms is
$T_{m_k}$. By Lemma 3.1, $T_{j_k} + T_{m_k}$ is triangular iff
$xy = j_k(j_k+1)$ with $y - x$ odd. Choosing minimal $y-x$ gives the
earliest next triangular term. ◻
:::

# Corollaries and Computational Verification

The recurrence ensures existence and uniqueness of each next triangular
term. Using $$(j_1,n_1) = (2,0), \qquad
    (j_{k+1},n_{k+1}) = (r_k, n_k + m_k), \quad
    T_{r_k} = T_{j_k} + T_{m_k},$$ we find $n_{10}=2964$. Further
computation yields $$n_{70} = 6{,}795{,}261{,}671{,}274.$$

# Final Result {#final-result .unnumbered}

$$\boxed{n_{70} = 6{,}795{,}261{,}671{,}274.}$$
