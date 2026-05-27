# Workings and Solution Notes for Erdős Problem 132

## Problem statement

Let $A\subset \mathbb{R}^2\), \(|A|=n$.  
For each realized distance value $d>0$, let

$m_d := \#\{\{a,b\}\subset A: |a-b|=d\}$.

Define **light distances** by $1\le m_d\le n$.

Questions:

1. Must there exist two distinct light distances?
2. Must the number of light distances tend to infinity with \(n\)?

---

## Stage 1: Reformulation

Let
\[
P := \binom n2,\qquad D:=\#\{d:m_d>0\},\qquad
L:=\#\{d:1\le m_d\le n\},\qquad H:=D-L.
\]
Then heavy classes satisfy $m_d>n$, and
\[
\sum_d m_d = P.
\]
So:

- Q1 becomes: is \(L\ge 2\)?
- Q2 becomes: does \(L\to\infty\) as \(n\to\infty\)?

Graph language: each distance value \(d\) gives a distance graph \(G_d\) on \(A\), with \(|E(G_d)|=m_d\).  
Light distances are exactly those with at most \(n\) edges.

---

## Stage 2: Immediate inequalities

From \(\sum_d m_d=P\):

- Since each heavy class contributes \(>n\), we get
  \[
  P>nH\;\Rightarrow\; H<\frac{P}{n}=\frac{n-1}{2}.
  \]
- Hence
  \[
  L=D-H\ge D-\frac{n-1}{2}.
  \]

Using only Guth-Katz \(D\gtrsim n/\log n\) gives
\[
L\gtrsim \frac{n}{\log n}-\frac n2,
\]
which is asymptotically useless (can be negative). So distinct-distance lower bounds alone do not force \(L\ge 1\), \(L\ge 2\), or \(L\to\infty\).

---

## Stage 3: Consequences of known bounds

### 3.1 One unconditional light distance

Let \(\Delta\) be the diameter of \(A\).  
The diameter graph in \(\mathbb R^2\) has at most \(n\) edges (Hopf-Pannwitz / Vazsonyi theorem). Therefore
\[
m_\Delta\le n,
\]
so \(L\ge 1\) always (for \(n\ge 2\)).

### 3.2 Maximum multiplicity bounds

Let \(M:=\max_d m_d\). Known unit-distance type upper bounds give \(M\lesssim n^{4/3}\). Then
\[
D\ge \frac{P}{M}\gtrsim n^{2/3},
\]
still far too weak to imply many light classes.

### 3.3 Distance energy

Define \(E_2:=\sum_d m_d^2\). Known upper bounds are of order \(n^3\log n\), while Cauchy gives \(E_2\ge P^2/D\).  
These are compatible with spectra in which almost all classes have multiplicity near \(n\) or moderately above \(n\), so they do not force many \(m_d\le n\).

---

## Stage 4: Testing canonical configurations

1. **Regular \(n\)-gon:** each chord-length class has multiplicity \(O(n)\), in fact \(\le n\). So many light distances.
2. **Square lattice \(N\times N\) (\(n=N^2\))**: many boundary displacement vectors produce classes with multiplicity \(\le n\); at least \(\Omega(N)=\Omega(\sqrt n)\) light values.
3. **Triangular lattice patches:** analogous behavior; many near-boundary classes are light.
4. **Cartesian products / parallel-line constructions:** many classes with multiplicity \(\le n\).
5. **Many points on circles:** regular/near-regular placements still yield many light chord classes.
6. **Random point sets:** almost surely all pair distances distinct, so \(L=P=\Theta(n^2)\).

No standard extremal family gives bounded \(L\).

---

## Stage 5: Contradiction attempt from \(L\le 1\)

Assume at most one light distance.
Then at least \(D-1\) classes are heavy:
\[
P=\sum_d m_d \ge 1 + (D-1)(n+1),
\]
so
\[
D \le \frac{P-1}{n+1}+1 = \frac n2 + O(1).
\]
This does not contradict known lower bounds \(D\gtrsim n/\log n\).

Energy constraints are also compatible:
minimal heavy-scale contribution is \(\Theta(n^3)\), still below known \(O(n^3\log n)\) upper bounds.

So this line stalls.

---

## Stage 6: Attempt toward \(L\to\infty\)

Dyadic stratification \(S_j=\{d:2^jn < m_d \le 2^{j+1}n\}\), combined with incidence machinery, controls only very rich classes and yields at best \(O(n)\)-type global counts for heavy classes.

That still allows all but \(O(1)\) classes to lie just above the threshold \(n\), consistent with all currently quoted bounds.

Therefore current standard tools do not prove \(L\to\infty\).

---

## Stage 7: Exact obstruction and partial theorems

### Proven partials

- \(L\ge 1\) for every \(n\ge 2\) (diameter argument).
- Universal claim \(L\ge 2\) for every \(n\) is false (see Stage 8 finite counterexample).

### Obstruction

The missing ingredient is a sharp theorem controlling the number of distance values in the near-threshold band
\[
m_d \asymp n,
\]
not just very high multiplicity tails.

---

## Stage 8: Final verdict

- **Rigorous counterexample to literal Q1 (all \(n\))**: \(n=3\), equilateral triangle.  
  There is exactly one distance value \(d\), with \(m_d=3=n\). Hence \(L=1\), not \(2\).
- **Asymptotic form (large \(n\))**:
  - \(L\ge 2\) eventually: unresolved by current derivations.
  - \(L\to\infty\): unresolved by current derivations.

So the strongest justified conclusion is:

1. one light distance always exists;
2. two-light-distance universal statement is false in finite generality;
3. asymptotic growth of light distances remains open under currently available bounds.
