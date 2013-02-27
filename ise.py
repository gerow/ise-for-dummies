#!/usr/bin/python

def fpin(P, i, N):
  return P * (1 + i)**N

def pfin(F, i, N):
  return F * (1 + i)**(-N)

def fain(A, i, N):
  return A * ( ( (1 + i)**N - 1) / (i) )

def afin(F, i, N):
  return F * ( (i) / ( (1 + i)**N - 1))

def pain(A, i, N):
  return A * ( ( (1 + i)**N - 1) / (i * (1 + i)**N) )

def apin(P, i, N):
  return P * ( (i * (1 + i)**N) / ( ( 1 + i)**N - 1) )

def pgin(G, i, N):
  return G * ( ( (1 + i)**N - i * N - 1) / (i**2 * (1 + i)**N))

def agin(G, i, N):
  return G * ( ( (1 + i)**N - i * N - 1) / ( i * ( (1 + i)**N - 1)))

def pagin(A, g, i, N):
  if i == g:
    return A * ( (N) / (1 + i))
  return A * ( (1 - (1 + g)**N * (1 + i)**-N) / (i - g))
