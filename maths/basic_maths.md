# Basic Math

This guide covers four main domains: **Geometry**, **Algebra & Word Problems**, **Number Theory**, and **Combinatorics & Probability**.

---

## Section 1: Geometry & Spatial Logic

### 1. The Pythagorean Theorem & Special Triangles

- **Formula:**

  $$a^2+b^2=c^2$$

- **45°–45°–90° Triangle:** Side ratio is $1:1:\sqrt{2}$.
- **30°–60°–90° Triangle:** Side ratio is $1:\sqrt{3}:2$.
- **Common Pythagorean Triples:** $(3,4,5)$, $(5,12,13)$, $(8,15,17)$, $(7,24,25)$, and their integer multiples.

### 2. Area of Planar Figures & Dissection

- **Triangle:** $A=\frac12 bh$
- **Heron's Formula:** $A=\sqrt{s(s-a)(s-b)(s-c)}$, where $s=\frac{a+b+c}{2}$.
- **Trapezoid:** $A=\frac{a+b}{2}\times h$
- **Circle:** $A=\pi r^2$
- **Sector:** $A=\frac{\theta}{360^\circ}\pi r^2$
- **Regular Hexagon:** $A=\frac{3\sqrt3}{2}s^2$

### 3. Similar Triangles & Area Ratios

If the side-length scale factor is $k=\frac{a_1}{a_2}$:

- **Ratio of perimeters:** $k$
- **Ratio of areas:** $k^2$
- **Ratio of volumes for similar 3D solids:** $k^3$

### 4. Polygon Properties & Angles

- **Sum of Interior Angles:** $S=(n-2)\times180^\circ$
- **Each Interior Angle of a Regular Polygon:** $\frac{(n-2)\times180^\circ}{n}$
- **Sum of Exterior Angles:** $360^\circ$
- **Number of Diagonals:** $D=\frac{n(n-3)}{2}$

### 5. Coordinate Geometry & Distance

- **Distance Formula:** $d=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2}$
- **Midpoint Formula:** $M=\left(\frac{x_1+x_2}{2},\frac{y_1+y_2}{2}\right)$
- **Slope:** $m=\frac{y_2-y_1}{x_2-x_1}$

### 6. Pick's Theorem

$$A=I+\frac{B}{2}-1$$

- $I$ = number of interior lattice points.
- $B$ = number of boundary lattice points.

---

## Section 2: Algebra, Sequences & Word Problems

### 1. Speed, Distance, and Time

- **Distance:** $d=v\times t$
- **Average Speed:** $v_{\text{avg}}=\frac{\text{Total Distance}}{\text{Total Time}}$
- **Average Speed for Equal Distances:** $v_{\text{avg}}=\frac{2v_1v_2}{v_1+v_2}$

**Important:** Do not average speeds directly.

### 2. Ratios, Percentages, and Mixtures

- **Percentage Increase or Decrease:** $\frac{|\text{New}-\text{Old}|}{\text{Old}}\times100\%$
- **Weighted Average:** $C_{\text{final}}=\frac{m_1c_1+m_2c_2}{m_1+m_2}$

### 3. Arithmetic and Geometric Sequences

- **Arithmetic Sequence:** $a_n=a_1+(n-1)d$
- **Sum of an Arithmetic Series:** $S_n=\frac{n}{2}(a_1+a_n)$
- **Geometric Sequence:** $a_n=a_1r^{n-1}$

### 4. Algebraic Identities & Manipulation

- **Square of a Sum:** $(a+b)^2=a^2+2ab+b^2$
- **Square of a Difference:** $(a-b)^2=a^2-2ab+b^2$
- **Difference of Squares:** $a^2-b^2=(a-b)(a+b)$

### 5. Vieta's Formulas

For $ax^2+bx+c=0$ with roots $r_1$ and $r_2$:

- **Sum of Roots:** $r_1+r_2=-\frac{b}{a}$
- **Product of Roots:** $r_1r_2=\frac{c}{a}$

---

## Section 3: Number Theory & Modular Systems

### 1. Divisibility Rules

- **2, 4, and 8:** Check the last 1, 2, or 3 digits.
- **3 and 9:** Check the sum of the digits.
- **5:** The number ends in 0 or 5.
- **10:** The number ends in 0.
- **6:** The number is divisible by 2 and 3.
- **11:** The alternating sum of the digits is divisible by 11.

### 2. Prime Factorization, LCM & GCD

- **Prime Factorization:** $n=p_1^{e_1}p_2^{e_2}\cdots p_k^{e_k}$
- **Number of Positive Divisors:** $d(n)=(e_1+1)(e_2+1)\cdots(e_k+1)$
- **GCD–LCM Relationship:** $\gcd(a,b)\times\operatorname{lcm}(a,b)=a\times b$

### 3. Modular Arithmetic & Cyclic Patterns

- **Congruence:** $a\equiv b\pmod m$
- **Units-Digit Cycle for Powers of 7:** $7,9,3,1$, repeating.

### 4. Euclidean Algorithm

$$\gcd(a,b)=\gcd(b,a\bmod b)$$

Repeat until the remainder becomes zero.

---

## Section 4: Combinatorics, Logic & Probability

### 1. Fundamental Counting Principle & Arrangements

- **Multiplication Rule:** $m\times n$
- **Permutations:** $P(n,r)=\frac{n!}{(n-r)!}$
- **Combinations:** $\binom{n}{r}=\frac{n!}{r!(n-r)!}$

### 2. Complementary & Casework Counting

- **Complementary Rule:** Desired Outcomes = Total Outcomes − Undesired Outcomes.
- **Casework:** $\text{Total}=\text{Case}_1+\text{Case}_2+\cdots+\text{Case}_k$

### 3. Principle of Inclusion–Exclusion (PIE)

- **For Two Sets:**

  $|A\cup B|=|A|+|B|-|A\cap B|$

- **For Three Sets:**

  $|A\cup B\cup C|=|A|+|B|+|C|-|A\cap B|-|B\cap C|-|C\cap A|+|A\cap B\cap C|$

### 4. Theoretical & Geometric Probability

- **Discrete Probability:** $P(E)=\frac{\text{Favorable Outcomes}}{\text{Total Possible Outcomes}}$
- **Geometric Probability:** $P(E)=\frac{\text{Favorable Area or Length}}{\text{Total Area or Length}}$

### 5. Pigeonhole Principle & Parity Logic

- **Pigeonhole Principle:** If $n>m$ objects are placed into $m$ containers, at least one container holds more than one object.
- **Even + Even = Even**
- **Odd + Odd = Even**
- **Even ± Odd = Odd**
- **Odd × Odd = Odd**
- **Any product containing an even factor is even.**

---

## Quick Reference Summary Table

| Domain | High-Yield Topic | Key Equation / Idea | Primary Shortcut / Tip |
|---|---|---|---|
| **Geometry** | Pythagorean Theorem | $a^2+b^2=c^2$ | Look for common Pythagorean triples. |
| **Geometry** | Interior Angles | $S=(n-2)\times180^\circ$ | Exterior angles sum to $360^\circ$. |
| **Algebra** | Average Speed | Total Distance / Total Time | Never average speeds directly. |
| **Algebra** | Arithmetic Series | $S_n=\frac{n}{2}(a_1+a_n)$ | Multiply the number of terms by their average. |
| **Number Theory** | Divisor Count | $d(n)=\prod_i(e_i+1)$ | Add 1 to each exponent and multiply. |
| **Number Theory** | Last Digit | $a^b\bmod10$ | Find the repeating units-digit cycle. |
| **Combinatorics** | Combinations | $\binom{n}{r}=\frac{n!}{r!(n-r)!}$ | Use $\binom{n}{r}=\binom{n}{n-r}$. |
| **Probability** | Complement | $P(A)=1-P(A')$ | For "at least one," calculate 1 minus the probability of none. |

---

**Revision Tip:** Memorize the core formulas and practice recognizing which formula applies to each problem.