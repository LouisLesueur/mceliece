#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 10:06:11 2020

@author: sebastien

Injection d'erreur
"""
import numpy as np
from sympy import GF, Poly, Pow, Add, Symbol

def Hamming_weight(p):
    """
    Calcul le poids de Hamming de notre message.
    Renvoie ce poids ainsi que la liste des indices 
    des composantes non nulles de p
    """
    w = 0
    Ip = []
    for i in range(len(p)):
        if not p[i] == 0:
            w += 1
            Ip.append(i)
            
    return w, Ip

def Hamming_distance(p1, p2):
    """
    Calcule la distance de Hamming entre deux mots
    """
    p3 = p1 - p2
    return Hamming_weight(p3)


def Constant_injection_fault(i1, i2, n, m, etc):
    """
    Calcul un polynôme annulé par alpha de notre
    Goppa Code
    """
    p = np.zeros(n)
    p[i1] = 1
    p[i2] = 1
    find_it = False
    while (not find_it):
        #######
        pbis = injection_faute(p, 0)
        #######
        w, Ip = Hamming_weight(pbis)
        if w == 2 and Hamming_distance(p, pbis) > 0:
            find_it = True
            i3 = Ip[0]
            i4 = Ip[1]
            poly = lambda x: x[i1] + x[i2] + x[i3] + x[i4]
    return poly

def Quadratic_injection_fault(i, n, m, etc):
    """
    Calcul un polynôme annulé par alpha de notre
    Goppa Code
    """
    p = np.zeros(n)
    p[i] = 0
    find_it = False
    while(not find_it):
        ######
        pbis = injection_faute(p, 2)
        ######
        w, Ip = Hamming_weight(pbis)
        if w > 1 and i in Ip:
            find_it = True
            poly = lambda x: x[i]
        elif w == 2:
            j1 = Ip[0]
            j2 = Ip[1]
            find_it = True
            poly = lambda x: x[i]*x[j1] + x[i]*x[j2] + x[j1]*x[j2]
    return poly


def injection_erreur_systeme(L):

    L_lin = []
    for f in L:
        if deg(f) == 1:
            L_lin.append(f)
