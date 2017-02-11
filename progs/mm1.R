N <- 1000
lambda <- 3
mu <- 5

A <- rep(0, N)
D <- rep(0, N)
W <- rep(0, N)

for(k in 2:N){
  Xk <- rexp(1,lambda)
  Sk <- rexp(1,mu)
  A[k] <- A[k-1] + Xk
  D[k] <- max(A[k], D[k-1]) + Sk
  W[k] <- D[k] - A[k]
}
print(mean(W))

print(quantile(W, prob = c(0.8, 0.9, 0.95)))
